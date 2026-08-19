# FORESIGHT
## AI-Powered Demand Forecasting & Inventory Intelligence

## 1. Project Overview

FORESIGHT is an AI-powered demand forecasting and inventory intelligence system designed to help businesses make better inventory planning decisions.

The system uses machine learning to predict product demand and analyzes inventory levels to identify:

- Stockout Risk
- Overstock Risk
- Healthy Inventory

Based on the identified risk, the system provides inventory recommendations such as reordering stock or reducing excess inventory.

The project also includes an interactive Streamlit dashboard for visualizing demand forecasts, inventory risks, recommendations, and model performance.

---

## 2. Problem Statement

Businesses need to maintain the right amount of inventory.

Too little inventory can result in stockouts and lost sales, while excessive inventory increases storage costs and the possibility of unsold products.

FORESIGHT uses historical sales and inventory-related information to forecast demand and identify potential inventory risks.

---

## 3. Objectives

The main objectives of FORESIGHT are:

1. Analyze historical sales and inventory data.
2. Clean and preprocess the dataset.
3. Identify important factors affecting demand.
4. Build a machine learning model for demand forecasting.
5. Evaluate the forecasting model.
6. Identify stockout and overstock risks.
7. Generate inventory recommendations.
8. Provide an interactive dashboard for business users.

---

## 4. Dataset

The dataset contains information related to stores, products, inventory, sales, pricing, promotions, weather, seasonality, and other demand-related factors.

Important features include:

- Store ID
- Product ID
- Category
- Region
- Inventory Level
- Units Sold
- Units Ordered
- Price
- Discount
- Weather Condition
- Promotion
- Competitor Pricing
- Seasonality
- Epidemic
- Demand

---

## 5. Data Processing

The project includes data preprocessing steps such as:

- Loading the dataset
- Checking missing values
- Checking duplicate records
- Converting categorical features into numerical values
- Processing date-related features
- Preparing features for machine learning

Date features such as:

- Year
- Month
- Day
- Day of Week

were extracted to help the model learn time-related patterns.

---

## 6. Machine Learning Model

A Random Forest Regressor was used for demand forecasting.

The model was trained using the processed dataset and evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 7. Model Performance

The current model produced the following results:

| Metric | Result |
|---|---:|
| MAE | 12.76 |
| MSE | 289.38 |
| RMSE | 17.01 |
| R² Score | 0.869 |

The R² score of 0.869 indicates that the model explains approximately 86.9% of the variation in the target demand values on the evaluated test data.

---

## 8. Feature Importance

The Random Forest model identified several important features for demand prediction.

The most influential features included:

- Units Sold
- Units Ordered
- Inventory Level
- Price
- Competitor Pricing
- Day
- Category
- Product ID
- Month
- Day of Week

---

## 9. Inventory Risk Analysis

The predicted demand is compared with the available inventory to identify inventory conditions.

### Stockout Risk

When inventory is lower than the expected demand, the system identifies a potential stockout risk.

Recommendation:

**Reorder Stock**

### Overstock Risk

When inventory is significantly higher than expected demand, the system identifies a potential overstock risk.

Recommendation:

**Offer Discount / Reduce Orders**

### Healthy

When inventory is within an appropriate range compared with predicted demand:

**No Action Required**

---

## 10. Dashboard

The project includes a Streamlit dashboard that provides:

- Total Records
- Total Inventory
- Predicted Demand
- Stockout Risks
- Overstock Risks
- Inventory Risk Distribution
- Inventory vs Predicted Demand
- Risk Category Analysis
- Inventory Recommendations
- Individual Product Analysis
- Category-wise Demand Analysis
- Model Performance
- CSV Report Download

The dashboard also provides filters for store and risk category.

---

## 11. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook

---

## 12. Project Structure

```text
project_foresight/
│
├── models/
├── data/
├── app/
├── notebooks/
├── risk_analysis.csv
├── streamlit_app.py
├── requirements.txt
└── README.md

## 13. Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>