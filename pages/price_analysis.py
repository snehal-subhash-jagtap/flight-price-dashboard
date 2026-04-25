import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("cleaned_flight_data.csv")

# ---------------- GLOBAL FILTERS ----------------
st.sidebar.header("🔍 Filters")

airlines = st.sidebar.multiselect(
    "Airline",
    df["airline"].unique(),
    default=df["airline"].unique()
)

classes = st.sidebar.multiselect(
    "Class",
    df["class"].unique(),
    default=df["class"].unique()
)

df = df[
    (df["airline"].isin(airlines)) &
    (df["class"].isin(classes))
]

# ---------------- TITLE ----------------
st.title("💰 Price Analysis")

# ---------------- PRICE BY AIRLINE ----------------
st.subheader("✈ Price by Airline")

airline = df.groupby("airline")["price"].mean().sort_values().reset_index()

fig1 = px.bar(
    airline,
    x="price",
    y="airline",
    orientation="h",
    title="Average Price by Airline",
    text="price",
    color="price",
    color_continuous_scale="Blues"
)

fig1.update_layout(
    xaxis_title="Average Price",
    yaxis_title="Airline",
    template="plotly_white"
)

st.plotly_chart(fig1, width="stretch")

# ---------------- PRICE BY STOPS ----------------
st.subheader("🛑 Price by Stops")

stops = df.groupby("num_stops")["price"].mean().reset_index()

fig2 = px.bar(
    stops,
    x="num_stops",
    y="price",
    title="Price vs Stops",
    text="price",
    color="price",
    color_continuous_scale="Viridis"
)

fig2.update_layout(
    xaxis_title="Number of Stops",
    yaxis_title="Average Price",
    template="plotly_white"
)

st.plotly_chart(fig2, width="stretch")

# ---------------- CLASS VS PRICE ----------------
st.subheader("💺 Class vs Price")

cls = df.groupby("class")["price"].mean().reset_index()

fig3 = px.bar(
    cls,
    x="class",
    y="price",
    title="Flight Class vs Price",
    text="price",
    color="price",
    color_continuous_scale="Teal"
)

fig3.update_layout(
    yaxis_title="Average Price",
    template="plotly_white"
)

st.plotly_chart(fig3, width="stretch")

# ---------------- PRICE TREND ----------------
st.subheader("📅 Price Trend by Month")

# Graph filter (month)
selected_months = st.multiselect(
    "Select Months",
    sorted(df["month"].unique()),
    default=sorted(df["month"].unique())
)

trend_df = df[df["month"].isin(selected_months)]

month = trend_df.groupby("month")["price"].mean().reset_index()
month = month.sort_values("month")

fig4 = px.line(
    month,
    x="month",
    y="price",
    markers=True,
    title="Monthly Price Trend"
)

fig4.update_layout(
    xaxis_title="Month",
    yaxis_title="Average Price",
    template="plotly_white"
)

fig4.update_traces(line=dict(width=3))

st.plotly_chart(fig4, width="stretch")

# Insight

# ---------------- TOP EXPENSIVE FLIGHTS ----------------
st.subheader("📊 Top 10 Expensive Flights")

top = df.sort_values(by="price", ascending=False).head(10)
st.dataframe(top)