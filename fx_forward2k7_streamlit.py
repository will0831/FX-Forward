import streamlit as st

st.title("FX Forward Contract Calculator")

# 拉條選擇：合約到期天數
days_until_maturity = st.slider(
    "Days until Forward Contract Maturity",
    min_value=1,
    max_value=365,
    value=30,
    step=1
)

# 輸入 spot rate
spot_rate = st.number_input(
    "Spot Rate (e.g., USD/EUR)",
    min_value=0.0001,
    value=1.10,
    step=0.0001
)

# 輸入 domestic interest rate
domestic_rate = st.number_input(
    "Domestic Interest Rate (Annual, %)",
    min_value=0.0,
    value=5.0,
    step=0.1
) / 100

# 輸入 foreign interest rate
foreign_rate = st.number_input(
    "Foreign Interest Rate (Annual, %)",
    min_value=0.0,
    value=2.0,
    step=0.1
) / 100

# 計算年期 (以天數換算)
time_to_maturity = days_until_maturity / 360  # 金融業常用360日基準

# 計算 forward rate
forward_rate = spot_rate * (1 + domestic_rate * time_to_maturity) / (1 + foreign_rate * time_to_maturity)

# 顯示結果
st.markdown(
    f"<h2 style='text-align: center; color: #2E8B57;'>🚀 Forward Rate after {days} days: <span style='font-size: 42px;'>{forward_rate:.4f}</span></h2>",
    unsafe_allow_html=True
)
# Footer
st.markdown("---")
st.caption("Developed by William | FX Forward Model")
