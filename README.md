# Solar Calculator

A simple, elegant solar energy calculator built with FastAPI.

## Features

- Calculate solar system costs and returns
- Annual and 25-year revenue projections
- ROI and payback period calculations
- Environmental impact visualization
- Purchase vs. Leasing comparison
- Hebrew RTL interface

## Deployment on Render

1. Push this repository to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Render will automatically detect the configuration

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

Visit http://localhost:8000

## API Endpoints

- `GET /` - Calculator interface
- `POST /api/calculate` - Calculate quote
- `GET /health` - Health check

## Configuration

Default pricing parameters are set in `main.py`:
- Price per kWp: ₪2,850
- Production per kWp: 1,550 kWh/year
- Tariff rate: ₪0.52/kWh
- VAT: 18%
