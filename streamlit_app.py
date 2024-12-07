import streamlit as st
import pandas as pd
import numpy as np


st.title("림버스 컴퍼니")
st.title("에고 기프트")
st.write(
    "오류 및 수정 문의는 해당 글에 댓글을 남겨주세요."
)

keyword = st.radio(
    "키워드 선택",
    [":red[화상]", ":orange[출혈]", ":orange[진동]", ":green[파열]", ":blue[침잠]", ":blue[호흡]", ":violet[충전]"],
    key="visibility",
    horizontal=True,
)



if keyword == ":red[화상]":
    st.write("화상")
    burn1 = ["융해된 파라핀", "재에서 재로", "타오르는 지성", "편광"]
    burn2 = ["만년 동안 끓는 솥", "만년 화톳불", "울화통", "일점타격논리회로", "작열우모", "지옥나비의 꿈"]
    burn3 = ["그을린 원반", "먼지에서 먼지로", "불빛꽃"]
    burn4 = ["불꽃의 편린", "업화 조각"]

    burn1_sec = st.segmented_control(
    "화상 1 티어", burn1, selection_mode="multi")
    burn2_sec = st.segmented_control(
    "화상 2 티어", burn2, selection_mode="multi")
    burn3_sec = st.segmented_control(
    "화상 3 티어", burn3, selection_mode="multi")
    burn4_sec = st.segmented_control(
    "화상 4 티어", burn4, selection_mode="multi")

    st.text("융해된 파라핀 + 만년 동안 끓는 솥 = 요리 비법 전서")
    st.text("재에서 재로 + 요리 비법 전서 + 먼지에서 먼지로 = 진혼")
    st.text("타오르는 지성 + 그을린 원반 + 만년 화톳불 = 훔쳐온 불꽃")
if keyword == ":orange[출혈]": 
    st.write("출혈")

if keyword == ":orange[진동]":
    st.write("진동")

if keyword == ":green[파열]":
    st.write("파열")

if keyword == ":blue[침잠]":
    st.write("침잠")

if keyword == ":blue[호흡]":
    st.write("호흡")

if keyword == ":violet[충전]":
    st.write("충전")
