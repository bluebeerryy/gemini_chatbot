# -*- coding: utf-8 -*-
import streamlit as st
import google.generativeai as genai

# 페이지 구성
st.set_page_config(page_title="Gemini 챗봇", layout="centered")

# 제목 및 설명
st.title("💬 Gemini-1.5 Flash 기반 챗봇")
st.markdown("👋 안녕하세요! Gemini 모델로 구동되는 챗봇입니다.")

# Gemini API 키 설정
genai.configure(api_key=st.secrets["gemini"]["api_key"])

# Gemini 모델 초기화
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# 세션 상태 초기화
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat = model.start_chat(history=[])

# 이전 대화 출력
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])

# 사용자 입력
user_input = st.chat_input("메시지를 입력하세요...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "text": user_input})

    response = st.session_state.chat.send_message(user_input)
    bot_reply = response.text

    st.chat_message("ai").markdown(bot_reply)
    st.session_state.chat_history.append({"role": "ai", "text": bot_reply})
