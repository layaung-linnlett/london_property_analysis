import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

st.set_page_config(page_title="London Property Finder", layout="wide")

@st.cache_data
def load_data():
    scores = pd.read_csv('data/processed/borough_investment_scores.csv')
    prices = pd.read_csv('data/processed/price_history_london.csv', parse_dates=['date'])
    return scores, prices

df_scores, df_prices = load_data()

st.title("London Property Investment Opportunity Finder")
st.write("Scoring 32 London boroughs across growth, safety, and affordability.")

st.divider()

col1, col2, col3 = st.columns(3)

top_borough = df_scores.loc[df_scores['investment_score'].idxmax(), 'area_name']
best_cagr_borough = df_scores.loc[df_scores['cagr_10yr'].idxmax(), 'area_name']
best_cagr = df_scores['cagr_10yr'].max() * 100
london_median = df_scores['price_2024'].median()

col1.metric("Top Scored Borough", top_borough, "BUY signal")
col2.metric("Best 10-Year CAGR", f"{best_cagr:.1f}%", best_cagr_borough)
col3.metric("London Median Price (2024)", f"£{london_median:,.0f}")

st.divider()
st.subheader("Investment Score Ranking — All 32 Boroughs")

display_cols = ['area_name', 'price_2024', 'cagr_10yr', 
                'avg_annual_crimes', 'investment_score', 'signal']

df_display = df_scores[display_cols].sort_values('investment_score', ascending=False).copy()
df_display['cagr_10yr'] = (df_display['cagr_10yr'] * 100).round(2).astype(str) + '%'
df_display['price_2024'] = df_display['price_2024'].apply(lambda x: f'£{x:,.0f}')
df_display['investment_score'] = df_display['investment_score'].round(1)
df_display.columns = ['Borough', 'Price (2024)', 'CAGR', 'Avg Annual Crimes', 'Score', 'Signal']

st.dataframe(df_display, use_container_width=True, hide_index=True)

st.divider()
st.subheader("Borough Investment Profile")

selected = st.selectbox("Select a borough", 
                         df_scores.sort_values('investment_score', ascending=False)['area_name'])

row = df_scores[df_scores['area_name'] == selected].iloc[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Investment Score", f"{row['investment_score']:.1f}")
col2.metric("Signal", row['signal'])
col3.metric("10-Year CAGR", f"{row['cagr_10yr']*100:.2f}%")
col4.metric("Price (2024)", f"£{row['price_2024']:,.0f}")


st.subheader(f"Price Trajectory — {selected} (2014–2024)")

df_trend = df_prices[(df_prices['area_name'] == selected) & 
                      (df_prices['date'] >= '2014-01-01')]

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(df_trend['date'], df_trend['average_price'], color='#2ecc71', linewidth=2)
ax.set_xlabel('Date')
ax.set_ylabel('Average Price')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'£{x:,.0f}'))
plt.tight_layout()
st.pyplot(fig)
plt.close()