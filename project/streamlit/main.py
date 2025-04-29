# 실행 streamlit run main.py
# python -m streamlit run main.py
import streamlit as st

print(st.session_state)

st.title('회의록 관리 시스템')

# =======================================
# 0. Session state 활용 예제
# =======================================
# if "count" not in st.session_state:
#   st.session_state['count'] = 0

# count_button = st.button(label = '카운트 증가')
# if count_button:
#   st.session_state['count'] += 1

# st.write(st.session_state['count'])

# =======================================
# 1. File Uploader
# =======================================
uploaded_file = st.file_uploader(
  label='회의 음성 파일을 업로드 하세요',
  type=['mp3', 'wav'],
  key='upload_file'
)

# =======================================
# 2. 회의 정보 입력
# =======================================
import datetime

if "meeting_info" not in st.session_state:
  st.session_state['meeting_info'] = ""

with st.expander(label = '회의 정보', expanded=True):
  col1, col2 = st.columns(2)
  name = col1.text_input(label = '이름', value = "김현희")
  department = col2.text_input(label = '부서', value = "개발팀")
  meeting_date = st.date_input(label = '회의 날짜', value = datetime.date(2025, 4, 22))

  st.session_state.meeting_info = {
      "name": name,
      "department": department,
      "meeting_date": meeting_date.strftime(format="%Y-%m-%d %A")
  }

# =======================================
# 3. 버튼 만들기
# =======================================
col1, col2, col3, col4 = st.columns(4)
stt_button=col1.button(label='음성 텍스트 변환', use_container_width=True, type="primary")
summary_button=col2.button(label='회의록 요약', use_container_width=True, type="primary")
todo_button=col3.button(label='To Do List 생성', use_container_width=True, type="primary")
schedule_button=col4.button(label='일정 추출', use_container_width=True, type="primary")


if stt_button:
    st.session_state["stt_expander"] = True
    st.session_state["summary_expander"] = False
    st.session_state["todo_expander"] = False
    st.session_state["schedule_expander"] = False
if summary_button:
    st.session_state["stt_expander"] = False
    st.session_state["summary_expander"] = True
    st.session_state["todo_expander"] = False
    st.session_state["schedule_expander"] = False
if todo_button:
    st.session_state["stt_expander"] = False
    st.session_state["summary_expander"] = False
    st.session_state["todo_expander"] = True
    st.session_state["schedulle_expander"] = False
if schedule_button:
    st.session_state["stt_expander"] = False
    st.session_state["summary_expander"] = False
    st.session_state["todo_expander"] = False
    st.session_state["schedule_expander"] = True
# ========================================
# 4. 컨테이너 만들기
# =======================================
if "stt_expander" not in st.session_state:
    st.session_state["stt_expander"] = False
if "summary_expander" not in st.session_state:
    st.session_state["summary_expander"] = False
if "todo_expander" not in st.session_state:
    st.session_state["todo_expander"] = False
if "schedule_expander" not in st.session_state:
    st.session_state["schedule_expander"] = False

with st.expander(label="음성 텍스트 변환", expanded=st.session_state["stt_expander"]):
    # if stt_button:
        # whisper를 사용해서 음성 파일을 텍스트로 변환해주는 코드 입력
    st.text_area(label="회의록", height=300)

with st.expander(label="회의록 요약", expanded=st.session_state["summary_expander"]):
    # if summary_button:
        # summary_chain을 만들어서 invoke 하는 코드 입력
    st.text_area(label="회의록 요약", height=300)

with st.expander(label="To Do List 생성", expanded=st.session_state["todo_expander"]):
    # if todo_button:
        # todo_chain을 만들어서 invoke 하는 코드 입력
    st.text_area(label="To Do List 생성", height=300)

with st.expander(label="일정 추출", expanded=st.session_state["schedule_expander"]):
    # if schedule_button:
        # schedule_chain을 만들어서 invoke 하는 코드 입력
    st.text_area(label="일정 추출", height=300)


print(st.session_state)