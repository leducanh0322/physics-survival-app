
import streamlit as st

# Cấu hình page
st.set_page_config(page_title="EmoLearn", layout="wide")

# Ngôn ngữ
language = st.radio("Chọn ngôn ngữ/Choose language:", ("Tiếng Việt", "English"))

# Nội dung theo ngôn ngữ
if language == "Tiếng Việt":
    st.title("EmoLearn - Trò chơi Vật lý đại cương")
    st.markdown("Chào mừng bạn đến với EmoLearn - ứng dụng học vật lý qua trò chơi tương tác!")

    st.header("Chức năng")
    st.markdown("- Chơi game vật lý: trả lời câu hỏi trắc nghiệm có tính tương tác")
    st.markdown("- Theo dõi tiến độ học tập: điểm số, thời gian, chủ đề")
    st.markdown("- Chuyển đổi ngôn ngữ Tiếng Việt/English")

    # Giao diện game mẫu
    st.subheader("Bắt đầu chơi")
    question = "Vật nào sau đây có khối lượng lớn nhất?"
    options = ["Quả bóng bàn", "Quả táo", "Xe máy", "Tờ giấy"]
    answer = st.radio("Câu hỏi: " + question, options)
    if st.button("Trả lời"):
        if answer == "Xe máy":
            st.success("Chính xác!")
        else:
            st.error("Sai rồi! Đáp án đúng là Xe máy.")

elif language == "English":
    st.title("EmoLearn - General Physics Game")
    st.markdown("Welcome to EmoLearn - an interactive physics learning game!")

    st.header("Features")
    st.markdown("- Play physics quiz game with interactive questions")
    st.markdown("- Track learning progress: scores, time, topics")
    st.markdown("- Switch between Vietnamese and English")

    st.subheader("Start Game")
    question = "Which of the following has the greatest mass?"
    options = ["Ping pong ball", "Apple", "Motorbike", "Paper sheet"]
    answer = st.radio("Question: " + question, options)
    if st.button("Submit"):
        if answer == "Motorbike":
            st.success("Correct!")
        else:
            st.error("Incorrect! The correct answer is Motorbike.")
