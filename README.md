# London Property Investment Opportunity Finder

Scores and ranks all 32 London boroughs on growth, safety, and affordability, using 30 years of HM Land Registry price data and 6 years of Metropolitan Police crime records.

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/) [![Pandas](https://img.shields.io/badge/Pandas-3.0-green)](https://pandas.pydata.org/) [![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red)](https://streamlit.io/)

---

**The problem:** property investors typically target Inner London "prestige" boroughs — Kensington, Westminster, Chelsea. The data says that's the wrong call.

I built a scoring engine that ingests the price and crime data, engineers three independently weighted signals (**growth 40%, safety 30%, affordability 30%**), and outputs a composite 0–100 score ranking every borough as BUY, HOLD, or AVOID. The headline result: a –0.83 Pearson correlation between 2024 entry price and 10-year CAGR across all 32 boroughs. The most expensive boroughs have historically produced the worst returns. Barking & Dagenham at £322,220 has outperformed Kensington & Chelsea at £1,197,249 by 5.77 percentage points a year over the last decade.

---

## Key Findings

- **Top-ranked borough: Barking & Dagenham (score 93.3).** Cheapest in the dataset at £322,220 (37% below the London median), 5.71% 10-year CAGR, and falling crime.
- **Westminster scores lowest overall (15.3, AVOID)** — not from weak growth (its 10-year CAGR is actually +0.92%) but from the highest crime volume in the dataset and a high entry price. **Kensington & Chelsea (25.3, AVOID)** is the genuine growth laggard, with a flat –0.06% 10-year CAGR despite an entry price above £1.19M.
- **–0.83 price/CAGR correlation** across all 32 boroughs. This is the model's foundation: prestige is already priced in, so there's no upside left.
- **17 of 32 boroughs sit in the "Alpha Zone"** — below-average entry price and above-average 10-year CAGR at the same time. The market hasn't corrected for this yet.
- **Outer London is Pareto dominant.** Cheaper on average entry price, higher average 10-year CAGR, and lower average crime than Inner London, all three at once.
- **29 of 32 boroughs fell in price over the 12 months to January 2024**, driven by the Bank of England rate cycle. Only Greenwich, Richmond upon Thames, and Hackney held positive momentum. For high-CAGR Outer East boroughs, that correction improved the entry price relative to the long-run trajectory.
- **London average 10-year CAGR: 3.77%.** Waltham Forest leads at 6.08%, 61% above the average.

| Rank | Borough | Score | Price (2024) | 10-yr CAGR | Signal |
|------|---------|-------|--------------|------------|--------|
| 1 | **Barking and Dagenham** | 93.3 | £322,220 | 5.71% | BUY |
| 2 | **Bexley** | 93.1 | £391,782 | 5.73% | BUY |
| 3 | **Havering** | 91.0 | £419,290 | 5.82% | BUY |
| 4 | **Waltham Forest** | 87.9 | £503,705 | 6.08% | BUY |
| 5 | **Sutton** | 85.8 | £420,223 | 4.54% | BUY |
| 28 | Islington | 53.1 | £659,560 | 1.87% | AVOID |
| 29 | Hammersmith and Fulham | 47.5 | £724,641 | 0.84% | AVOID |
| 30 | Camden | 41.4 | £797,248 | 1.38% | AVOID |
| 31 | **Kensington & Chelsea** | 25.3 | £1,197,249 | –0.06% | AVOID |
| 32 | **Westminster** | 15.3 | £936,715 | 0.92% | AVOID |

**Supporting correlations:**

| Finding | Value |
|---------|-------|
| Price ↔ Income correlation | +0.93 (price follows income, not crime) |
| PTAL score ↔ CAGR correlation | –0.82 (well-connected boroughs are already priced in) |
| Inner London median price (2024) | £597,973 |
| Outer London median price (2024) | £478,234 |
| Lowest CAGR | Kensington & Chelsea, –0.06% |

---

## Screenshots

**Chart 1 — Price Trajectory: Top 8 Growth Boroughs (2014–2024)**
![Chart 1](outputs/figures/chart1_price_trajectory.png)

**Chart 2 — 10-Year CAGR Ranking: All 32 Boroughs**
![Chart 2](outputs/figures/chart2_cagr_ranking.png)

**Chart 3 — Crime vs Price Quadrant Scatter (colour = CAGR)**
![Chart 3](outputs/figures/chart3_crime_price_quadrant.png)

**Chart 4 — Price Distributions: Inner vs Outer London**
![Chart 4](outputs/figures/chart4_price_distributions.png)

**Chart 5 — Investment Factor Correlation Matrix**
![Chart 5](outputs/figures/chart5_correlation_matrix.png)

**Chart 6 — Crime Trend: Top 6 Investment Boroughs (2020–2026)**
![Chart 6](outputs/figures/chart6_crime_trend.png)

**Chart 7 — Investment Score Ranking: All 32 Boroughs with BUY/HOLD/AVOID**
![Chart 7](outputs/figures/chart7_investment_ranking.png)

---

## Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.13 | Core analysis language |
| Pandas | 3.0.3 | Data wrangling, feature engineering, merging |
| SQLite (via `sqlite3`) | built-in | 8 investment queries, no database server needed |
| Matplotlib | 3.11.0 | Chart production |
| Seaborn | 0.13.2 | Statistical visualisations (heatmap, box plot) |
| Streamlit | 1.58.0 | Interactive dashboard |
| Jupyter Notebook | — | Analysis and write-up |

---

## Methodology

### Investment scoring model

Three independently normalised signals combined into one composite 0–100 score:

```
Investment Score = Growth Score × 0.40
                + Safety Score  × 0.30
                + Afford Score  × 0.30
```

| Component | Weight | Raw Metric | Normalisation |
|-----------|--------|-----------|---------------|
| Growth Score | 40% | 10-year CAGR (Jan 2014 → Jan 2024) | Min-max 0–100 |
| Safety Score | 30% | Avg annual crimes (2020–2024) | Min-max 0–100, inverted |
| Affordability Score | 30% | Average price (Jan 2024) | Min-max 0–100, inverted |

Growth gets the highest weight because capital appreciation is the main thing an investor is optimising for. Safety comes next: crime reduction tends to precede buyer demand and price appreciation by 12–18 months, so it acts as a leading indicator rather than a lagging one. Affordability captures entry-point risk and headroom — a cheaper entry point leaves more room for the price to move.

Top 5 boroughs by composite score get **BUY**, bottom 5 get **AVOID**, the remaining 22 get **HOLD**.

### Data sources

| Dataset | Source | Coverage |
|---------|--------|----------|
| HM Land Registry House Price Index | gov.uk Open Data | 1995–2024, monthly, borough-level |
| Metropolitan Police Crime Data | data.london.gov.uk | Jun 2020–May 2026, monthly |
| GLA London Borough Profiles | data.london.gov.uk | Socioeconomic baseline (2014) |

All three are free and open — no API keys or subscriptions needed.

---

## Project Structure

```
london_property_analysis/
│
├── data/
│   ├── raw/
│   │   ├── crime_historical.csv          # Metropolitan Police historical crime
│   │   ├── crime_recent.csv              # Metropolitan Police Jun 2020–May 2026
│   │   ├── hm_land_registry.csv          # not in git (56 MB) — see How to Run below
│   │   └── london_borough_profiles.csv   # GLA socioeconomic indicators
│   └── processed/
│       ├── borough_investment_scores.csv # final scored + ranked dataset (32 boroughs)
│       ├── master_borough_data.csv       # merged feature dataset pre-scoring
│       └── price_history_london.csv      # monthly price time series (all 32 boroughs)
│
├── notebooks/
│   └── london_property_analysis.ipynb    # full analysis: 6 sections, 124 cells
│
├── dashboard/
│   └── app.py                            # Streamlit interactive dashboard
│
├── outputs/
│   └── figures/                          # 7 charts saved at 150 DPI
│       ├── chart1_price_trajectory.png
│       ├── chart2_cagr_ranking.png
│       ├── chart3_crime_price_quadrant.png
│       ├── chart4_price_distributions.png
│       ├── chart5_correlation_matrix.png
│       ├── chart6_crime_trend.png
│       └── chart7_investment_ranking.png
│
├── src/                                  # reserved for helper scripts, empty for now
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run

### 1. Clone and install

```bash
git clone https://github.com/layaung-linnlett/london_property_analysis
cd london_property_analysis
pip install -r requirements.txt
```

### 2. Get the HM Land Registry file

`crime_historical.csv`, `crime_recent.csv`, and `london_borough_profiles.csv` are already in the repo under `data/raw/`. The HM Land Registry file is too large for git (56 MB) and needs a manual download:

1. Go to [the gov.uk House Price Index data page](https://www.gov.uk/government/statistical-data-sets/uk-house-price-index-data-downloads-february-2025)
2. Download the **"Average price by property type, local authority"** CSV
3. Save it to `data/raw/hm_land_registry.csv`

### 3. Run the analysis notebook

```bash
jupyter notebook notebooks/london_property_analysis.ipynb
```

Run all cells top to bottom. It will load and clean all three datasets, engineer the CAGR and crime features, run the 8 SQL queries in an in-memory SQLite database, save all 7 charts to `outputs/figures/`, score and rank the 32 boroughs, and write the results to `data/processed/`.

### 4. Launch the dashboard

```bash
python -m streamlit run dashboard/app.py
```

Opens at `http://localhost:8501`. It shows KPI cards (top-scored borough, best CAGR, London median price), the full ranking table with BUY/HOLD/AVOID signals, a borough selector, and an interactive price trajectory chart per borough.

---

## Limitations & Future Work

**Current limitations:**
- CAGR uses a single point-in-time comparison (Jan 2014 vs Jan 2024), so it's sensitive to which exact month you measure from — a rolling 12-month average would smooth this out
- Crime data lumps together every category — robbery, theft, violence, and anti-social behaviour affect residential demand differently, and treating them as one number hides that
- Socioeconomic data is from the 2014 GLA borough profiles vintage, so it may not reflect recent demographic shifts in Outer London
- No forward-looking signals — regeneration pipelines, transport investment, and planning approvals are leading indicators the model doesn't capture

**What I'd add next:**
- Rental yield data (Zoopla/Rightmove API) to compute total return as capital gain plus rental income
- Planning application volume as a regeneration signal
- A time-series forecast (ARIMA or Prophet) to project 3-year price trajectories
- Crime broken down by category (theft, violence, ASB) for a more granular safety score
- Monthly transaction volume as a liquidity/exit-risk signal

---

## Contact

Built by **La Yaung Linn Lett**

GitHub: [github.com/layaung-linnlett](https://github.com/layaung-linnlett)
