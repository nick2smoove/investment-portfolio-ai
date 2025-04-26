import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from textblob import TextBlob

# --- AI-Powered Tax Strategy Suggestions ---
def recommend_tax_efficient_portfolio(risk, income):
    if risk == "High":
        if income > 100000:
            return "For high-income earners, invest in tax-efficient ETFs like Vanguard Tax-Managed Fund (VTCLX) or tax-exempt municipal bonds."
        else:
            return "Consider index funds like Vanguard S&P 500 ETF (VOO), which have low capital gains taxes due to their tax efficiency."
    elif risk == "Medium":
        return "For a moderate-risk portfolio, consider including tax-advantaged accounts like IRAs or Roth IRAs, and invest in tax-efficient funds like Vanguard Total Stock Market ETF (VTI)."
    else:
        return "For low-risk portfolios, invest in tax-exempt municipal bonds or tax-efficient bond ETFs like Schwab U.S. Aggregate Bond ETF (SCHZ) to minimize tax burdens."

def display_tax_strategy(risk, income):
    tax_efficiency = recommend_tax_efficient_portfolio(risk, income)
    st.subheader("💡 Tax-Efficient Portfolio Recommendations:")
    st.write(tax_efficiency)

# --- Portfolio Risk Visualization (Correlation and Heatmap) ---
def plot_portfolio_risk(assets):
    # Simulate stock data (for the sake of this example)
    data = pd.DataFrame({
        'Asset': assets,
        'Volatility': np.random.rand(len(assets)) * 20,  # Simulated volatilities
        'Correlation': np.random.rand(len(assets))  # Simulated correlation with a market index
    })
    
    # Correlation matrix (for simplicity, using random values)
    correlation_matrix = np.random.rand(len(assets), len(assets))
    np.fill_diagonal(correlation_matrix, 1)  # Diagonal should be 1, as assets are fully correlated with themselves
    
    # Create a heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, xticklabels=assets, yticklabels=assets, cmap="coolwarm", linewidths=0.5)
    plt.title("Portfolio Risk Correlation Heatmap")
    st.pyplot()

    # Plot volatility
    fig, ax = plt.subplots()
    ax.bar(data['Asset'], data['Volatility'], color='skyblue')
    ax.set_ylabel("Volatility")
    ax.set_title("Asset Volatility")
    st.pyplot()

# --- Streamlit Integration ---
st.title("💸 AI Investment Portfolio Recommender")

# User Inputs
income = st.number_input("Enter your annual income:", min_value=10000, value=50000)
age = st.number_input("Enter your age:", min_value=10, max_value=100, value=30)
risk = st.selectbox("Select your risk tolerance:", ["Low", "Medium", "High"])
goal = st.selectbox("Select your investment goal:", [
    "Emergency Fund", "Vacation", "Buying a Car", "Paying for a Wedding", 
    "Graduate School", "Down Payment on a House", "Retirement", "Wealth Accumulation"])

# Define a sample portfolio
portfolio = {
    "Stocks": 60,
    "Bonds": 30,
    "Real Estate": 5,
    "Cash": 5
}

if st.button("Generate My Portfolio"):
    # Display portfolio allocation
    st.subheader("📊 Recommended Portfolio Allocation:")
    for asset, percent in portfolio.items():
        st.write(f"**{asset}:** {percent}%")

    # Plot portfolio risk (correlation heatmap and volatility)
    plot_portfolio_risk(list(portfolio.keys()))

    # Display tax strategy
    display_tax_strategy(risk, income)
