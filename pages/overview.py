import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- LOAD DATA ----------------
df = pd.read_csv("cleaned_flight_data.csv")

# ---------------- FILTERS ----------------
st.sidebar.header("🔍 Filters")

airlines = st.sidebar.multiselect(
    "Airline",
    df["airline"].unique(),
    default=df["airline"].unique()
)

df = df[df["airline"].isin(airlines)]

# ---------------- TITLE ----------------
st.title("📊 Overview")

# ---------------- KPI ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Flights", len(df))
col2.metric("Avg Price", f"₹{df['price'].mean():,.0f}")
col3.metric("Max Price", f"₹{df['price'].max():,.0f}")
col4.metric("Min Price", f"₹{df['price'].min():,.0f}")

# ---------------- PRICE TREND ----------------
st.subheader("📈 Price Trend by Month")

trend = df.groupby("month")["price"].mean().reset_index()
trend = trend.sort_values("month")   # FIX month order

fig1 = px.line(
    trend,
    x="month",
    y="price",
    markers=True,
    title="Average Flight Price Trend"
)

fig1.update_layout(
    xaxis_title="Month",
    yaxis_title="Average Price",
    template="plotly_white"
)

fig1.update_traces(line=dict(width=3))  # smoother line

st.plotly_chart(fig1, width="stretch")

# Insight
st.info("Flight prices vary across months, indicating seasonal demand patterns.")

# ---------------- PRICE DISTRIBUTION ----------------
st.subheader("📊 Price Distribution")

fig2 = px.histogram(
    df,
    x="price",
    nbins=30,
    title="Flight Price Distribution",
    color_discrete_sequence=["#636EFA"]
)

fig2.update_layout(
    xaxis_title="Price Range",
    yaxis_title="Number of Flights",
    template="plotly_white",
    bargap=0.05
)

fig2.update_traces(opacity=0.75)

st.plotly_chart(fig2, width="stretch")

# Insight
st.info("Most flights fall within mid-range prices, with fewer high-cost tickets.")