import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="FORESIGHT",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📊 FORESIGHT")
st.subheader("AI-Powered Demand Forecasting & Inventory Intelligence")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("risk_analysis.csv")

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🔎 Filters")

store_options = ["All"] + sorted(df["Store ID"].unique().tolist())
selected_store = st.sidebar.selectbox("Select Store", store_options)

risk_options = ["All"] + sorted(df["Risk"].unique().tolist())
selected_risk = st.sidebar.selectbox("Select Risk", risk_options)

filtered_df = df.copy()

if selected_store != "All":
    filtered_df = filtered_df[
        filtered_df["Store ID"] == selected_store
    ]

if selected_risk != "All":
    filtered_df = filtered_df[
        filtered_df["Risk"] == selected_risk
    ]

# -----------------------------
# KPI Calculations
# -----------------------------
total_records = len(filtered_df)
total_inventory = filtered_df["Inventory Level"].sum()
total_predicted_demand = filtered_df["Predicted Demand"].sum()

stockout_risks = (
    filtered_df["Risk"] == "Stockout Risk"
).sum()

overstock_risks = (
    filtered_df["Risk"] == "Overstock Risk"
).sum()

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("📦 Total Records", f"{total_records:,}")

with col2:
    st.metric("📊 Total Inventory", f"{total_inventory:,}")

with col3:
    st.metric(
        "📈 Predicted Demand",
        f"{total_predicted_demand:,.0f}"
    )

with col4:
    st.metric("🔴 Stockout Risks", f"{stockout_risks:,}")

with col5:
    st.metric("🟠 Overstock Risks", f"{overstock_risks:,}")

st.divider()

# -----------------------------
# Chart 1: Risk Distribution
# -----------------------------
st.subheader("⚠️ Inventory Risk Distribution")

risk_counts = filtered_df["Risk"].value_counts().reset_index()
risk_counts.columns = ["Risk", "Count"]

fig_risk = px.pie(
    risk_counts,
    names="Risk",
    values="Count",
    hole=0.4,
    title="Inventory Risk Distribution"
)

st.plotly_chart(fig_risk, use_container_width=True)

# -----------------------------
# Chart 2: Inventory vs Demand
# -----------------------------
st.subheader("📦 Inventory vs Predicted Demand")

sample_df = filtered_df.head(1000)

fig_inventory = px.scatter(
    sample_df,
    x="Inventory Level",
    y="Predicted Demand",
    title="Inventory Level vs Predicted Demand",
    hover_data=["Store ID", "Product ID", "Risk"]
)

st.plotly_chart(
    fig_inventory,
    use_container_width=True
)

# -----------------------------
# Chart 3: Risk Count
# -----------------------------
st.subheader("📊 Risk Category Count")

fig_bar = px.bar(
    risk_counts,
    x="Risk",
    y="Count",
    title="Number of Products by Risk Category",
    text="Count"
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

# -----------------------------
# Recommendations
# -----------------------------
st.subheader("🛒 Inventory Recommendations")

st.dataframe(
    filtered_df[
        [
            "Store ID",
            "Product ID",
            "Inventory Level",
            "Predicted Demand",
            "Risk",
            "Recommendation"
        ]
    ].head(50),
    use_container_width=True
)
# -----------------------------
# Individual Product Analysis
# -----------------------------
st.divider()

st.subheader("🔮 Demand & Inventory Analysis")

st.write(
    "Select a product record to analyze its inventory position "
    "and predicted demand."
)

product_index = st.number_input(
    "Enter Record Number",
    min_value=0,
    max_value=len(filtered_df) - 1,
    value=0,
    step=1
)

selected_row = filtered_df.iloc[product_index]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Current Inventory",
        f"{selected_row['Inventory Level']:.0f}"
    )

with col2:
    st.metric(
        "Predicted Demand",
        f"{selected_row['Predicted Demand']:.2f}"
    )

with col3:
    st.metric(
        "Risk Level",
        selected_row["Risk"]
    )

st.info(
    f"Recommendation: {selected_row['Recommendation']}"
)
# -----------------------------
# Category Analysis
# -----------------------------
st.divider()

st.subheader("📊 Category-wise Demand Analysis")

if "Category" in filtered_df.columns:

    category_data = (
        filtered_df
        .groupby("Category")
        .agg(
            Actual_Demand=("Units Sold", "sum"),
            Predicted_Demand=("Predicted Demand", "sum")
        )
        .reset_index()
    )

    fig_category = px.bar(
        category_data,
        x="Category",
        y=["Actual_Demand", "Predicted_Demand"],
        barmode="group",
        title="Actual vs Predicted Demand by Category"
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )
    # -----------------------------
# Model Performance
# -----------------------------
st.divider()

st.subheader("🤖 Demand Forecasting Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "MAE",
        "12.76"
    )

with col2:
    st.metric(
        "RMSE",
        "17.01"
    )

with col3:
    st.metric(
        "R² Score",
        "0.869"
    )

st.caption(
    "Model: Random Forest Regressor"
)
# -----------------------------
# Download Risk Analysis
# -----------------------------
st.divider()

st.subheader("📥 Download Report")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Risk Analysis CSV",
    data=csv_data,
    file_name="foresight_risk_analysis.csv",
    mime="text/csv"
)