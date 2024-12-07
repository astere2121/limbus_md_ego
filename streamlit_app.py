import streamlit as st
import pandas as pd
import numpy as np

keywords = {
    ':red[화상]': '화상',
    ':orange[출혈]': '출혈',
    ':orange[진동]': '진동',
    ':green[파열]': '파열',
    ':blue[침잠]': '침잠',
    ':blue[호흡]': '호흡',
    ':violet[충전]': '충전',
}

keyword_options = {
    '화상': {
        "없음": {},
        "헬스치킨": {
            3: ["닭다리살"]
        }
    }
}

ego_gift_lists = {
    '화상': [
        ["융해된 파라핀", "재에서 재로", "타오르는 지성", "편광"],
        ["만년 동안 끓는 솥*", ":green[만년 화톳불]", "울화통", "일점타격논리회로", "작열우모", "지옥나비의 꿈"],
        ["그을린 원반*", "먼지에서 먼지로", "불빛꽃"],
        ["불꽃의 편린", "업화 조각"]
    ]
}

ego_gift_recipes = {
    '화상': [
        "융해된 파라핀 + 만년 동안 끓는 솥 = 요리 비법 전서",
        "재에서 재로 + 요리 비법 전서 + 먼지에서 먼지로 = 진혼",
        "타오르는 지성 + 그을린 원반 + 만년 화톳불 = 훔쳐온 불꽃"
    ]
}


st.title("림버스 컴퍼니")
st.title("에고 기프트")
st.write(
    "오류 및 수정 문의는 해당 글에 댓글을 남겨주세요."
)

selected_keyword = st.radio(
    "키워드 선택",
    keywords.keys(),
    key="visibility",
    horizontal=True,
)

temp = []

keyword = keywords[selected_keyword]

pack_list = keyword_options[keyword][st.selectbox("특수 팩 선택", keyword_options[keyword])]

for i, ego_list in enumerate(ego_gift_lists[keyword]):
    result_list = ego_list
    if i + 1 in pack_list:
        result_list += pack_list[i + 1]
    st.segmented_control(f"{keyword} {i + 1} 티어", result_list, selection_mode="multi")

for recipe in ego_gift_recipes[keyword]:
    st.text(recipe)
