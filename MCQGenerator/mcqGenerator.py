import streamlit as st
import os
import google.generativeai as genai

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the LLM model
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)


#  Create a prompt template
def mcq_prompt(grade, subject, subtopic, num_questions):
    template = """
        Generate {num_questions} multiple-choice questions for grade {grade} in the subject {subject}.
        The topic is {subtopic}. Each question should have 4 options, and one correct answer.
    """
    variables = ["grade", "subject", "subtopic", "num_questions"]

    prompt = PromptTemplate(input_variables=variables, template=template)

    return prompt.format(
        grade=grade, subject=subject, subtopic=subtopic, num_questions=num_questions
    )


# streamlit
st.title("MCQ Generator using Gemini")
st.write("Generate MCQs based on grade, subject and topic that you will enter")

with st.sidebar:
    with st.form("mcq_form"):
        grade = st.selectbox("Select Grade", [str(i) for i in range(1, 13)])
        subject = st.text_input("Subject", value="Science")
        subtopic = st.text_input("Subtopic", value="Physics")
        num_questions = st.number_input(
            "Number of Questions", min_value=1, max_value=50
        )
        submitted = st.form_submit_button("Generate MCQs")

if submitted:
    prompt = mcq_prompt(grade, subject, subtopic, num_questions)

    message = [
        HumanMessage(content=prompt),
    ]

    response = llm(message)

    st.write(response.content)
