import streamlit as st
import matplotlib.pyplot as plt
import random

# --- Helper Functions ---

# Risk Management: Stop-Loss & Take-Profit
def stop_loss_take_profit(stock_price, stop_loss_percentage, take_profit_percentage):
    stop_loss_price = stock_price * (1 - stop_loss_percentage / 100)
    take_profit_price = stock_price * (1 + take_profit_percentage / 100)
    
    return stop_loss_price, take_profit_price

# Goal Progress Tracker
def plot_goal_progress(current_amount, goal_amount):
    progress = (current_amount / goal_amount) * 100
    fig, ax = plt.subplots()
    ax.barh(['Investment Goal'], [progress], color='green' if progress >= 100 else 'orange')
    ax.set_xlim(0, 100)
    ax.set_xlabel('Progress (%)')
    ax.set_title('Goal Progress Tracker')
    return fig

def display_goal_tracker(current_amount, goal_amount):
    st.subheader("🎯 Investment Goal Tracker")
    st.write(f"Current Amount: ${current_amount}")
    st.write(f"Goal Amount: ${goal_amount}")
    
    fig = plot_goal_progress(current_amount, goal_amount)
    st.pyplot(fig)

# Portfolio Suggestions Based on Risk
def recommend_portfolio(age, risk, goal):
    portfolio = {}
    if risk == "High":
        portfolio["Stocks"] = 80
        portfolio["Bonds"] = 10
        portfolio["Cash"] = 10
    elif risk == "Medium":
        portfolio["Stocks"] = 60
        portfolio["Bonds"] = 30
        portfolio["Cash"] = 10
    else:
        portfolio["Stocks"] = 40
        portfolio["Bonds"] = 50
        portfolio["Cash"] = 10
    
    return portfolio

# Tax-Efficient Portfolio Recommendations
def recommend_tax_efficient_portfolio(risk, income):
    if risk == "High":
        if income > 100000:
            return "For high-income earners, invest in tax-efficient ETFs like Vanguard Tax-Managed Fund (VTCLX) or tax-exempt municipal bonds."
        else:
            return "Consider index funds like Vanguard S&P 500 ETF (VOO), which have low capital gains taxes due to their tax efficiency."
    elif risk == "Medium":
        return "Consider including tax-advantaged accounts like IRAs or Roth IRAs, and invest in tax-efficient funds like Vanguard Total Stock Market ETF (VTI)."
    else:
        return "Consider tax-exempt municipal bonds or tax-efficient bond ETFs like Schwab U.S. Aggregate Bond ETF (SCHZ) to minimize tax burdens."

# ESG Portfolio Recommendations
def recommend_esg_portfolio(risk):
    if risk == "High":
        return "For high-risk portfolios, consider ESG funds like iShares MSCI Global Impact ETF (SDG) or SPYG, which focus on sustainable growth sectors."
    elif risk == "Medium":
        return "For medium-risk portfolios, consider iShares ESG MSCI USA ETF (ESGU) for exposure to sustainable companies with moderate growth."
    else:
        return "For conservative investors, try Vanguard FTSE Social Index Fund (VFTSX) or iShares MSCI KLD 400 Social ETF (DSI) for a safe, socially responsible portfolio."

# Investment Strategy Suggestions
def suggest_investment_strategies(risk, goal):
    strategies = []
    if goal == "Retirement":
        if risk == "High":
            strategies.append("Consider increasing your stock allocation for long-term growth, especially in the tech and renewable energy sectors.")
        else:
            strategies.append("Rebalance your portfolio every year to ensure you're on track to meet retirement goals.")
    elif goal == "Emergency Fund":
        strategies.append("Keep at least 3-6 months of expenses in cash or short-term bonds for safety.")
    return strategies

# --- Streamlit Integration ---

st.title("💸 AI Investment Portfolio Recommender")

# User Inputs
income = st.number_input("Enter your annual income:", min_value=10000, value=50000)
age = st.number_input("Enter your age:", min_value=10, max_value=100, value=30)
risk = st.selectbox("Select your risk tolerance:", ["Low", "Medium", "High"])
goal = st.selectbox("Select your investment goal:", [
    "Emergency Fund", "Vacation", "Buying a Car", "Paying for a Wedding", 
    "Graduate School", "Down Payment on a House", "Retirement", "Wealth Accumulation"])

# Stock Price for Risk Management
stock_price = st.number_input("Enter stock price for risk management (e.g., 150):", value=150)

# Stop-Loss & Take-Profit Inputs
stop_loss_percentage = st.number_input("Enter stop-loss percentage:", min_value=1, value=10)
take_profit_percentage = st.number_input("Enter take-profit percentage:", min_value=1, value=15)

if st.button("Generate My Portfolio"):
    # Display Portfolio Allocation
    portfolio = recommend_portfolio(age, risk, goal)
    st.subheader("📊 Recommended Portfolio Allocation:")
    for asset, percent in portfolio.items():
        st.write(f"**{asset}:** {percent}%")
    
    # Visualizing Portfolio
    fig = plt.figure(figsize=(6, 4))
    plt.bar(portfolio.keys(), portfolio.values(), color=["blue", "orange", "green"])
    plt.title("Portfolio Allocation")
    st.pyplot(fig)

    # Goal Tracker
    current_amount = random.randint(1000, 5000)  # Randomized for the demo
    goal_amount = random.randint(10000, 50000)  # Randomized goal
    display_goal_tracker(current_amount, goal_amount)

    # Risk Management (Stop-Loss & Take-Profit)
    stop_loss, take_profit = stop_loss_take_profit(stock_price, stop_loss_percentage, take_profit_percentage)
    st.subheader("💡 Stop-Loss & Take-Profit Levels")
    st.write(f"Stop-Loss Price: ${stop_loss:.2f}")
    st.write(f"Take-Profit Price: ${take_profit:.2f}")
    
    # Tax-Efficient Portfolio Suggestions
    tax_efficiency = recommend_tax_efficient_portfolio(risk, income)
    st.subheader("📝 Tax-Efficient Portfolio Recommendations:")
    st.write(tax_efficiency)
    
    # ESG Portfolio Suggestions
    esg_recommendation = recommend_esg_portfolio(risk)
    st.subheader("🌱 ESG Portfolio Recommendations:")
    st.write(esg_recommendation)
    
    # Investment Strategy Suggestions
    investment_strategy = suggest_investment_strategies(risk, goal)
    st.subheader("💡 Investment Strategies:")
    for strategy in investment_strategy:
        st.write(f"- {strategy}")

# Optional: Add a news sentiment analysis, real-time data or other features here

