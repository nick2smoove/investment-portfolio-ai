def recommend_tax_efficient_portfolio(risk, income):
    if risk == "High":
        if income > 100000:
            return "For high-income earners, invest in tax-efficient ETFs like **Vanguard Tax-Managed Fund (VTCLX)** or tax-exempt municipal bonds."
        else:
            return "Consider index funds like **Vanguard S&P 500 ETF (VOO)**, which have low capital gains taxes due to their tax efficiency."
    elif risk == "Medium":
        return "For a moderate-risk portfolio, consider including tax-advantaged accounts like **IRAs** or **Roth IRAs**, and invest in tax-efficient funds like **Vanguard Total Stock Market ETF (VTI)**."
    else:
        return "For low-risk portfolios, invest in **tax-exempt municipal bonds** or tax-efficient bond ETFs like **Schwab U.S. Aggregate Bond ETF (SCHZ)** to minimize tax burdens."

def recommend_esg_portfolio(risk):
    if risk == "High":
        return "For high-risk portfolios, consider ESG funds like **iShares MSCI Global Impact ETF (SDG)** or **SPYG**, which focus on sustainable growth sectors."
    elif risk == "Medium":
        return "For medium-risk portfolios, consider **iShares ESG MSCI USA ETF (ESGU)** for exposure to sustainable companies with moderate growth."
    else:
        return "For conservative investors, try **Vanguard FTSE Social Index Fund (VFTSX)** or **iShares MSCI KLD 400 Social ETF (DSI)** for a safe, socially responsible portfolio."

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

def display_esg_and_tax(risk, income, goal):
    tax_efficiency = recommend_tax_efficient_portfolio(risk, income)
    esg_recommendation = recommend_esg_portfolio(risk)
    investment_strategy = suggest_investment_strategies(risk, goal)
    
    st.subheader("📝 Tax-Efficient Portfolio Recommendations:")
    st.write(tax_efficiency)
    
    st.subheader("🌱 ESG Portfolio Recommendations:")
    st.write(esg_recommendation)
    
    st.subheader("💡 Investment Strategies:")
    for strategy in investment_strategy:
        st.write(f"- {strategy}")

# --- Streamlit Integration ---

st.title("💸 AI Investment Portfolio Recommender")

# User Inputs
income = st.number_input("Enter your annual income:", min_value=10000, value=50000)
age = st.number_input("Enter your age:", min_value=10, max_value=100, value=30)
risk = st.selectbox("Select your risk tolerance:", ["Low", "Medium", "High"])
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

    display_esg_and_tax(risk, income, goal)
