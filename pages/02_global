import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 글로벌 시가총액 TOP 10 (2024년 기준, 종목코드)
top10_stocks = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Saudi Aramco': '2222.SR',
    'Nvidia': 'NVDA',
    'Alphabet (Google)': 'GOOGL',
    'Amazon': 'AMZN',
    'Berkshire Hathaway': 'BRK-B',
    'Meta': 'META',
    'Eli Lilly': 'LLY',
    'TSMC': 'TSM',
}

# 시각화 시작
st.set_page_config(page_title="글로벌 시가총액 TOP10 주가 변화", layout="wide")
st.title("🌐 글로벌 시가총액 TOP 10 기업 최근 1년 주가 변화 🔥")

st.write(
    "아래 그래프는 세계에서 가장 시가총액이 높은 10대 기업의 최근 1년간 주가 변화를 보여줍니다. "
    "💸 Plotly를 활용한 인터렉티브 라인 차트로 되어 있어요!"
)

# 최근 1년 날짜 계산
end = datetime.today()
start = end - timedelta(days=365)

# 데이터 수집
data = {}
for name, code in top10_stocks.items():
    ticker = yf.Ticker(code)
    hist = ticker.history(start=start.strftime("%Y-%m-%d"), end=end.strftime("%Y-%m-%d"))
    if not hist.empty:
        data[name] = hist['Close']

# Plotly 그래프 그리기
fig = go.Figure()

for name, series in data.items():
    fig.add_trace(go.Scatter(
        x=series.index, y=series, mode='lines', name=name
    ))

fig.update_layout(
    title="글로벌 시가총액 TOP 10 기업 주가 변화 (최근 1년)",
    xaxis_title="날짜 📅",
    yaxis_title="종가 (USD, SR 등) 💰",
    legend_title="기업명",
    template="plotly_dark",
    hovermode="x unified",
    height=700
)

# Streamlit에서 출력
st.plotly_chart(fig, use_container_width=True)
