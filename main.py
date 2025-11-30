from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Solar Calculator")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create static and templates directories if they don't exist
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Default pricing parameters
PRICING = {
    "price_per_kwp": 2850,  # Price per kWp in ILS
    "production_per_kwp": 1550,  # Annual production per kWp in kWh
    "tariff_rate": 0.52,  # Tariff rate per kWh in ILS
    "trees_multiplier": 0.05,  # Trees equivalent per kWh
    "vat_rate": 0.18  # VAT rate (18%)
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Calculator page"""
    return templates.TemplateResponse("calculator.html", {"request": request})

@app.post("/api/calculate")
async def calculate_quote(
    system_size: float = Form(...),
):
    """Calculate quote based on system size"""
    total_price = system_size * PRICING["price_per_kwp"]
    annual_production = system_size * PRICING["production_per_kwp"]
    # Annual income: 900 ILS per kW
    annual_revenue = system_size * 900
    payback_period = round(total_price / annual_revenue, 2) if annual_revenue > 0 else 0
    # Trees: 120 trees per kW
    trees = int(system_size * 120)
    co2_saved = int(annual_production * 0.5)

    return {
        "total_price": total_price,
        "annual_production": annual_production,
        "annual_revenue": annual_revenue,
        "payback_period": payback_period,
        "environmental_impact": {
            "trees": trees,
            "co2_saved": co2_saved
        }
    }

@app.api_route("/health", methods=["GET", "HEAD"])
async def health_check():
    """Health check endpoint for UptimeRobot (supports GET and HEAD)"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
