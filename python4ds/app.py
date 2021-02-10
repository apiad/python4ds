import streamlit as st
from lessons import lessons


st.set_page_config(page_title="Python 4 Data Science", page_icon="🐍")


lesson = st.sidebar.selectbox("Lesson", list(lessons))
st.title(lesson)
lessons[lesson].run()
