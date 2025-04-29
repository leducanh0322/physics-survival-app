
import streamlit as st

st.set_page_config(page_title="EmoLearn", layout="centered")

st.title("EmoLearn - Trò chơi Vật lý đại cương")
st.write("Chào mừng bạn đến với EmoLearn - ứng dụng học vật lý qua trò chơi tương tác!")

language = st.radio("Chọn ngôn ngữ / Choose language:", ("Tiếng Việt", "English"))

if language == "Tiếng Việt":
    st.header("Chức năng")
    st.markdown("- **Chơi game vật lý:** trả lời câu hỏi trắc nghiệm có tính tương tác")
    st.markdown("- **Theo dõi tiến độ học tập:** điểm số, thời gian, chủ đề")
    st.markdown("- **Chuyển đổi ngôn ngữ:** Tiếng Việt / English")
    st.markdown("- **Giao diện mang thương hiệu HUST**")
elif language == "English":
    st.header("Features")
    st.markdown("- **Physics quiz game:** interactive multiple choice questions")
    st.markdown("- **Track your learning progress:** scores, time, topics")
    st.markdown("- **Language switch:** Vietnamese / English")
    st.markdown("- **HUST-branded interface**")
