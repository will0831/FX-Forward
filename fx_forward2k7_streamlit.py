
import streamlit as st

# Title
st.title("FX Forward Rate Calculator")

# Inputs
st.subheader("Input Parameters")
spot = st.number_input("Spot FX Rate (e.g., 1.1000)", value=1.1000, step=0.0001, format="%.4f")
r_domestic = st.number_input("Domestic Interest Rate (%)", value=5.00, step=0.01)
r_foreign = st.number_input("Foreign Interest Rate (%)", value=2.00, step=0.01)
days = st.number_input("Days until Forward Contract Maturity", value=180, step=1)

# Calculate forward rate
if st.button("Calculate Forward Rate"):
    t = days / 360  # Assuming 360-day convention
    try:
        forward_rate = spot * (1 + r_domestic / 100 * t) / (1 + r_foreign / 100 * t)
        st.success(f"FX Forward Rate: {forward_rate:.4f}")
    except ZeroDivisionError:
        st.error("Foreign interest rate caused a division by zero. Please check your input.")

days_until_maturity = st.slider(
    "Days until Forward Contract Maturity",
    min_value=0,
    max_value=365,
    value=30,  # 預設值
    step=1
)

st.write(f"You selected {days_until_maturity} days.")

# Footer
st.markdown("---")
st.caption("Developed by William | FX Forward Model")
