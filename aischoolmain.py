import streamlit as st
import finance_naver

#사이드바 화면

st.sidebar.header("로그인")
user_id = st.sidebar.text_input("ID 입력", value='streamlit', max_chars=15)
user_pass = st.sidebar.text_input("PASSWORD 입력", value="", type='password')

if user_pass == '1234':
    st.sidebar.header("포트폴리오")
    opt_data = ['',"환율조회", '따릉이', "유성우"]
    menu = st.sidebar.selectbox("메뉴 선택", opt_data, index=0)
    st.sidebar.write("선택한 메뉴:", menu)

    if menu == '환율조회':
        st.write("환율조회>>>>>")
        finance_naver.exchange_main()

    elif menu == "따릉이":
        st.write("따릉이 데이터 조회>>>>>")

    elif menu == "유성우":
        st.write("유성우 데이터 조회>>>>>")

    else:
        st.subheader("환영합니다!")
#메인 화면
