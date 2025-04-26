import streamlit as st
import matplotlib.pyplot as plt

def recommend_portfolio(age, risk, goal):
    if risk == "High":
        return {"Stocks": 80, "Bonds": 15, "Cash": 5}
    elif risk == "Medium":
        return {"Stocks": 60, "Bonds": 30, "Cash": 10}
    else:  # Low risk
        if age < 40:
            return {"Stocks": 50, "Bonds": 40, "Cash": 10}
        else:
            return {"Stocks": 30, "Bonds": 50, "Cash": 20}

def generate_tip(age, risk, goal):
    tip = ""
    
    if age < 30:
        tip += "You have time on your side! Focus on high-growth assets like stocks. "
    elif age > 55:
        tip += "Consider preserving your wealth with more bonds and cash. "
    else:
        tip += "Balance between growth and safety is key. "
    
    if risk == "High":
        tip += "Your high risk tolerance means you can pursue aggressive growth strategies."
    elif risk == "Medium":
        tip += "A balanced portfolio will help you ride out market ups and downs."
    else:
        tip += "Prioritize stability and steady returns to meet your goals."

    if goal == "Emergency Fund":
        tip += " For an emergency fund, focus on liquid, low-risk assets like cash or short-term bonds."
    elif goal == "Vacation":
        tip += " Vacation funds should be more liquid and safe, so consider low-risk investments."
    elif goal == "Buying a Car":
        tip += " For a car purchase, keep your investments low-risk to avoid price fluctuations."
    elif goal == "Paying for a Wedding":
        tip += " Weddings are a near-term goal, so stability is key. Invest in bonds and cash."
    elif goal == "Graduate School":
        tip += " For school, prioritize stability, but you might invest in moderate-risk bonds."
    elif goal == "Down Payment on a House":
        tip += " A down payment requires safety, so a mix of bonds and cash would be ideal."
    elif goal == "Retirement":
        tip += " Keep a long-term focus and maximize your retirement account contributions."
    elif goal == "Wealth Accumulation":
        tip += " For long-term growth, stock-heavy portfolios will help you accumulate wealth."

    return tip

def suggest_stocks(risk, goal):
    if risk == "High":
        if goal == "Retirement":
            return "Consider investing in growth stocks like Tesla (TSLA), Amazon (AMZN), or Alphabet (GOOGL) for long-term gains."
        elif goal == "Wealth Accumulation":
            return "You can look at tech stocks like NVIDIA (NVDA) and Meta (META), which have high growth potential."
        else:
            return "Look into high-growth sectors like tech, biotech, or renewable energy. Stocks like Tesla and Square could be promising."
    elif risk == "Medium":
        if goal == "Retirement":
            return "Consider a balanced mix of stocks like Apple (AAPL) and bonds like Vanguard Total Bond ETF (BND)."
        elif goal == "Wealth Accumulation":
            return "A blend of moderate-risk stocks such as Microsoft (MSFT) and dividends from consumer staples like Coca-Cola (KO)."
        else:
            return "Mix moderate-growth stocks with some defensive stocks like Procter & Gamble (PG) for stability."
    else:
        return "Low-risk options: Consider stable dividend stocks like Johnson & Johnson (JNJ) and utilities like Duke Energy (DUK) for steady returns."

def plot_portfolio(portfolio):
    labels = portfolio.keys()
    sizes = portfolio.values()
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio
    return fig

# --- Streamlit App ---

st.title("💸 AI Investment Portfolio Recommender")

st.write("Answer a few quick questions and get a smart, AI-personalized investment portfolio!")

age = st.number_input("Enter your age:", min_value=10, max_value=100, value=30)
risk = st.selectbox("How much risk you are willing to take on:", ["Low", "Medium", "High"])
goal = st.selectbox("Select your investment goal:", [
    "Emergency Fund", "Vacation", "Buying a Car", "Paying for a Wedding", 
    "Graduate School", "Down Payment on a House", "Retirement", "Wealth Accumulation"])

if st.button("Generate My Portfolio"):
    portfolio = recommend_portfolio(age, risk, goal)
    
    st.subheader("📊 Recommended Portfolio Allocation:")
    for asset, percent in portfolio.items():
        st.write(f"**{asset}:** {percent}%")
    
    fig = plot_portfolio(portfolio)
    st.pyplot(fig)
    
    smart_tip = generate_tip(age, risk, goal)
    st.success(f"💡 AI Tip: {smart_tip}")
    
    stocks = suggest_stocks(risk, goal)
    st.subheader("📈 Suggested Stocks to Invest In:")
    st.write(stocks)
