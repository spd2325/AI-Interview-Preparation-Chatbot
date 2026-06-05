import streamlit as st
import google.generativeai as genai

# Gemini API Key
GEMINI_API_KEY = "YOUR_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("AI Interview Preparation Chatbot")

question_type = st.selectbox(
    "Choose Interview Type",
    ["HR Interview", "Python", "SQL", "Java"]
)

if st.button("Generate Question"):
    prompt = f"Ask one {question_type} interview question."

    response = model.generate_content(prompt)

    st.session_state["question"] = response.text

if "question" in st.session_state:
    st.subheader("Interview Question")
    st.write(st.session_state["question"])

    answer = st.text_area("Your Answer")

    if st.button("Get Feedback"):
        feedback_prompt = f"""
        Interview Question:
        {st.session_state['question']}

        Candidate Answer:
        {answer}

        Evaluate the answer and provide:
        1. Score out of 10
        2. Strengths
        3. Improvements
        4. Better sample answer
        """

        feedback = model.generate_content(feedback_prompt)

        st.subheader("AI Feedback")
        st.write(feedback.text)
