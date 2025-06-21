import streamlit as st
import random

# MBTI별 추천 직업 사전
mbti_jobs = {
    "INTJ": ["🧠 데이터 과학자", "🧪 연구원", "📈 전략 컨설턴트"],
    "INTP": ["🖥️ 프로그래머", "📚 학자", "🤖 AI 엔지니어"],
    "ENTJ": ["💼 CEO", "📊 경영 컨설턴트", "🏛️ 정책 분석가"],
    "ENTP": ["🎤 크리에이터", "💡 스타트업 창업자", "🧭 혁신 전략가"],
    "INFJ": ["🌱 심리상담사", "📝 작가", "🌍 NGO 활동가"],
    "INFP": ["🎨 일러스트레이터", "🎭 예술가", "📖 시나리오 작가"],
    "ENFJ": ["🏫 교사", "🗣️ 커뮤니케이터", "📢 사회 운동가"],
    "ENFP": ["🎬 콘텐츠 크리에이터", "🎡 이벤트 플래너", "🦸‍♀️ 동기부여 연설가"],
    "ISTJ": ["📋 회계사", "🏦 은행원", "⚖️ 법률 전문가"],
    "ISFJ": ["👩‍⚕️ 간호사", "🏫 유치원 교사", "🏠 사회복지사"],
    "ESTJ": ["🚓 경찰관", "📊 관리자", "🧾 공무원"],
    "ESFJ": ["🧑‍🍳 요리사", "👩‍🏫 초등교사", "🤝 인사담당자"],
    "ISTP": ["🔧 정비사", "🕵️ 범죄 수사관", "🛠️ 엔지니어"],
    "ISFP": ["🎨 패션 디자이너", "📷 사진작가", "🌿 플로리스트"],
    "ESTP": ["📣 마케팅 담당자", "🚀 영업사원", "🏎️ 레이서"],
    "ESFP": ["🎤 가수", "📸 인플루언서", "💃 댄서"]
}

# 웹앱 꾸미기
st.set_page_config(page_title="✨ MBTI 진로 추천기 ✨", page_icon="🌈")

st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #FF69B4;'>🌟 MBTI별 직업 추천 웹앱 🌟</h1>
        <h3 style='color: #8A2BE2;'>나의 성격유형으로 어울리는 멋진 직업을 알아보자! 💖</h3>
    </div>
    <hr>
""", unsafe_allow_html=True)

# 사용자 입력
selected_mbti = st.selectbox("🔮 당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

if selected_mbti:
    st.markdown(f"### 🎯 {selected_mbti} 유형에게 어울리는 직업은...")
    job = random.choice(mbti_jobs[selected_mbti])
    st.markdown(f"<h2 style='color: #32CD32;'>👉 {job} 👈</h2>", unsafe_allow_html=True)
    st.balloons()

# 하단
st.markdown("""
<hr>
<p style='text-align: center;'>
    🧩 Made with ❤️ by 진로 선생님 🎓 | MBTI를 통해 나를 이해하고 미래를 그려보아요 🌈
</p>
""", unsafe_allow_html=True)
