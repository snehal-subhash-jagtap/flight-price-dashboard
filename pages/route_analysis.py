import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("cleaned_flight_data.csv")

st.title("🌍 Route Analysis")

# ---------------- SOURCE CITY ----------------
st.subheader("🧭 Source City vs Price")

source = df.groupby("source_city")["price"].mean().sort_values().reset_index()

fig1 = px.bar(
    source,
    x="price",
    y="source_city",
    orientation="h",
    title="Average Price by Source City",
    text="price"
)

fig1.update_layout(
    xaxis_title="Average Price",
    yaxis_title="Source City"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- DESTINATION CITY ----------------
st.subheader("🎯 Destination City vs Price")

dest = df.groupby("destination_city")["price"].mean().sort_values().reset_index()

fig2 = px.bar(
    dest,
    x="price",
    y="destination_city",
    orientation="h",
    title="Average Price by Destination City",
    text="price"
)

fig2.update_layout(
    xaxis_title="Average Price",
    yaxis_title="Destination City"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- TOP ROUTES ----------------
st.subheader("🌍 Top 10 Expensive Routes")

route = df.groupby(["source_city", "destination_city"])["price"].mean().reset_index()
route = route.sort_values(by="price", ascending=False).head(10)

route["route"] = route["source_city"] + " → " + route["destination_city"]

fig3 = px.bar(
    route,
    x="price",
    y="route",
    orientation="h",
    title="Top Expensive Routes",
    text="price"
)

fig3.update_layout(
    xaxis_title="Average Price",
    yaxis_title="Route"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------- ROUTE POPULARITY ----------------
st.subheader("📊 Route Popularity vs Price")

pop = df.groupby("route_popularity")["price"].mean().reset_index()

fig4 = px.bar(
    pop,
    x="route_popularity",
    y="price",
    title="Route Popularity Impact",
    text="price"
)

fig4.update_layout(
    xaxis_title="Route Popularity",
    yaxis_title="Average Price"
)

st.plotly_chart(fig4, use_container_width=True)