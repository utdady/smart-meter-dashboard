import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Smart Meter Data Dashboard")

df = pd.read_csv("smart_meter_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

st.sidebar.subheader("Filters")
selected_meter = st.sidebar.selectbox("Select Meter", df["meter_id"].unique())

filtered_df = df[df["meter_id"] == selected_meter]

st.subheader(f"Usage Over Time - {selected_meter}")
fig, ax = plt.subplots()
filtered_df.plot(x="timestamp", y="kWh", ax=ax)
st.pyplot(fig)

st.subheader("Hourly Usage Heatmap")
df["hour"] = df["timestamp"].dt.hour
heatmap_data = df.groupby(["meter_id", "hour"])["kWh"].mean().unstack()
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.heatmap(heatmap_data.sample(20), cmap="YlGnBu", ax=ax2)
st.pyplot(fig2)
