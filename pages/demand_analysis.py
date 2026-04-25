import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("cleaned_flight_data.csv")

st.title("🔥 Demand Analysis")


# ---------------- DEMAND LEVEL ----------------
st.subheader("🔥 Demand Level vs Price")

demand = df.groupby("demand_level")["price"].mean().reset_index()

fig1 = px.bar(
    demand,
    x="demand_level",
    y="price",
    title="Demand Level Impact on Price",
    text="price"
)

fig1.update_layout(
    xaxis_title="Demand Level",
    yaxis_title="Average Price"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- DAYS UNTIL FLIGHT ----------------
st.subheader("📅 Days Until Flight vs Price")

days = df.groupby("days_until_flight")["price"].mean().reset_index()

fig2 = px.line(
    days,
    x="days_until_flight",
    y="price",
    markers=True,
    title="Booking Time vs Price"
)

fig2.update_layout(
    xaxis_title="Days Before Flight",
    yaxis_title="Average Price"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- PEAK SEASON ----------------
st.subheader("📊 Peak Season vs Price")

peak = df.groupby("is_peak_season")["price"].mean().reset_index()

peak["Season"] = peak["is_peak_season"].map({0: "Off Season", 1: "Peak Season"})

fig3 = px.bar(
    peak,
    x="Season",
    y="price",
    title="Peak Season Effect",
    text="price"
)

fig3.update_layout(yaxis_title="Average Price")

st.plotly_chart(fig3, use_container_width=True)

# ---------------- WEEKEND ----------------
st.subheader("📊 Weekend vs Weekday")

weekend = df.groupby("is_weekend")["price"].mean().reset_index()

weekend["Day Type"] = weekend["is_weekend"].map({0: "Weekday", 1: "Weekend"})

fig4 = px.bar(
    weekend,
    x="Day Type",
    y="price",
    title="Weekend Effect on Price",
    text="price"
)

fig4.update_layout(yaxis_title="Average Price")

st.plotly_chart(fig4, use_container_width=True)