# 🏙️ London Property Investment Opportunity Finder

> **Business Question:** Which London boroughs represent the best investment opportunities based on price trends, growth potential, and risk indicators?

This project mirrors the analytical workflow of a real investment data team — from raw open data to a scored, ranked investment recommendation engine with an interactive dashboard.

---

## Key Findings

| Rank | Borough | Score | Price | 5-yr CAGR | Signal |
|------|---------|-------|-------|-----------|--------|
| 1 | **Bexley** | 92.4 | £403,541 | 3.5% | 🟢 BUY |
| 2 | **Sutton** | 87.7 | £447,784 | 2.9% | 🟢 BUY |
| 3 | **Barking & Dagenham** | 78.7 | £355,594 | 2.5% | 🟢 BUY |
| 4 | **Harrow** | 78.2 | £532,666 | 2.6% | 🟢 BUY |
| 5 | **Havering** | 77.7 | £432,963 | 2.6% | 🟢 BUY |

**Bottom line:** Outer South-East and Outer East London boroughs dominate the buy list — offering above-median growth with 20–33% price discounts to the London average and improving safety metrics.

---

## Methodology — Investment Scoring Model

Three independently normalised signals combined into a composite 0–100 score:

```
Investment Score = Growth Score × 0.40
                + Safety Score × 0.30
                + Affordability Score × 0.30
```

| Component | Weight | Metric | Normalisation |
|-----------|--------|--------|---------------|
| Growth Score | 40% | 5-year Price CAGR (2019–2024) | Min-max 0–100 |
| Safety Score | 30% | Inverse of avg annual crimes (2020–2024) | Min-max 0–100 |
| Affordability Score | 30% | % below London median price | Min-max 0–100 |

**Scoring rationale:** Growth is weighted highest as the primary return driver. Safety is weighted next — crime reduction precedes buyer demand and price appreciation. Affordability captures entry-point risk and headroom for capital gains.

Boroughs scoring in the top 5 receive a **BUY** signal; bottom 5 receive **AVOID**; remainder **HOLD**.

---

## Dataset Sources

| Dataset | Source | Coverage |
|---------|--------|----------|
| HM Land Registry House Price Index | [gov.uk Open Data](https://www.gov.uk/government/statistical-data-sets/uk-house-price-index-data-downloads-january-2024) | 2004–2024, borough-level |
| Metropolitan Police Crime Data | [data.london.gov.uk](https://data.london.gov.uk/dataset/recorded_crime_summary) | 2010–2024, monthly borough-level |
| GLA London Borough Profiles | [data.london.gov.uk](https://data.london.gov.uk/dataset/london-borough-profiles-and-atlas) | Socioeconomic indicators |

All datasets are **free and open** — no API keys or subscriptions required.

---

## Project Structure

```
london_property_investment/
├── data/
│   ├── raw/                          # Original downloaded datasets
│   │   ├── crime_historical.csv
│   │   ├── crime_recent.csv
│   │   ├── hm_land_registry.csv
│   │   └── london_borough_profiles.csv
│   └── processed/                    # Cleaned, merged outputs
│       ├── borough_investment_scores.csv
│       ├── master_borough_data.csv
│       └── price_history_london.csv
├── notebooks/
│   └── london_property_analysis.ipynb   # Full analysis notebook
├── dashboard/
│   └── app.py                           # Streamlit interactive dashboard
├── outputs/
│   └── charts/                          # All visualisations (PNG)
└── README.md
```

---

## Running the Dashboard

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/london-property-investment.git
cd london-property-investment

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the Streamlit dashboard
streamlit run dashboard/app.py
```

The dashboard runs at `http://localhost:8501` and includes:
- KPI cards: London median price, best growth borough, top-scored borough
- Interactive borough selector with full investment profile
- Price trend chart vs comparators
- Investment score ranking table with BUY/HOLD/AVOID signals
- Crime vs Price quadrant scatter
- Investment factor correlation heatmap

---

## Visualisations

Seven investment-focused charts generated in the analysis notebook:

1. **Price Trajectory** — Top 8 growth boroughs, 2015–2024
2. **CAGR Ranking** — All boroughs vs London median growth rate
3. **Crime vs Price Quadrant** — Risk/return scatter with growth colour coding
4. **Price Distributions** — Inner vs Outer London box plot + CAGR histogram
5. **Correlation Matrix** — Investment factors including transport, education, unemployment
6. **Crime Trend** — 2018–2024 for 6 target investment boroughs
7. **Investment Score Ranking** — All boroughs with BUY/HOLD/AVOID colour coding

---

## SQL Analysis (8 Investment Queries)

All queries executed via SQLite in Python — reproducible without a database server:

1. Top boroughs by 5-year CAGR
2. Undervalued boroughs (below London median price)
3. Crime vs Price investment category matrix
4. Price-to-growth ratio ranking
5. Price acceleration — last 12 months
6. Fastest-falling crime 2020→2024
7. Inner vs Outer London investment profile comparison
8. **The Alpha Zone** — above-average growth AND below-average entry price

---

## Investment Thesis — Top 3 Boroughs

**1. Bexley** — *Highest composite score (92.4)*
Entry price 24% below London median with the highest 5-yr CAGR in our dataset (3.5%). Outer South-East location with improving transport links and low crime density. Strongest risk-adjusted buy in the dataset.

**2. Sutton** — *Safety + growth convergence (87.7)*
Top safety score in the outer borough cohort combined with 2.9% CAGR. Attractive for buy-to-let given strong rental demand from professional renters priced out of Inner London. Council tax among lowest in London.

**3. Barking & Dagenham** — *Maximum affordability headroom (78.7)*
Largest price discount to London average (33.2%) in the dataset. Barking Riverside regeneration (10,000+ homes) and Elizabeth Line connectivity provide structural long-run demand drivers. Crime improving year-on-year since 2020.

---

## Tech Stack

| Tool | Use |
|------|-----|
| Python 3.12 | Core analysis language |
| Pandas / NumPy | Data wrangling & feature engineering |
| SQLite (via Python) | Reproducible SQL investment queries |
| Matplotlib / Seaborn | Investment-grade visualisations |
| Streamlit | Interactive investment dashboard |
| Jupyter Notebook | Reproducible analysis with narrative |
| Git / GitHub | Version control & portfolio hosting |

---

## 📧 Contact

Built by **[La Yaung Linn Lett]**
