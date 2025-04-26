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

    if goal == "Retirement":
        tip += " Keep a long-term focus and maximize your retirement account contributions."
    elif goal == "Buying a House":
        tip += " Since your goal is nearer-term, protect your capital with safer investments."
    else:
        tip += " Growing wealth long-term means you can afford to be patient and let compounding work."

    return tip

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
risk = st.selectbox("Select your risk tolerance:", ["Low", "Medium", "High"])
goal = st.selectbox("Select your investment goal:", ["Retirement", "Buying a House", "Growing Wealth"])

if st.button("Generate My Portfolio"):
    portfolio = recommend_portfolio(age, risk, goal)
    
    st.subheader("📊 Recommended Portfolio Allocation:")
    for asset, percent in portfolio.items():
        st.write(f"**{asset}:** {percent}%")
    
    fig = plot_portfolio(portfolio)
    st.pyplot(fig)
    
    smart_tip = generate_tip(age, risk, goal)
    st.success(f"💡 AI Tip: {smart_tip}")

