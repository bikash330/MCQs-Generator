# MCQ Generator

This project is a demo application that allows users to generate multiple-choice questions (MCQs) based on the grade, subject, and subtopic they input. It utilizes Google's Gemini LLM to create MCQs in real time and displays the generated questions in a user-friendly interface.

### Project Overview

- **Generate MCQs**: Users can input grade level, subject, and subtopic to generate MCQs with four options each and one correct answer.
- **Flexible Input**: Allows users to customize the number of questions they want to generate, ranging from 1 to 50.
- **LLM Integration**: Powered by Google's Gemini LLM for generating intelligent and context-aware MCQs based on the user's input.

### Tools and Technologies

- **LangChain**: Connects the language model (LLM) with document storage to enable document querying.
- **Google Gemini**: Provides natural language understanding and interaction with users.
- **Streamlit**: Used for building an interactive web-based user interface (Front-end).

### How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/bikash330/MCQs-Generator.git
   ```

2. **Create a virtual environment**:
    ```bash
    conda create -p venv python=3.10
    ```

3. **Activate the environment**:
    ```bash
    conda activate venv\
    ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Navigate to the project directory**:
    ```bash
    cd chatbot
    ```

6. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

### Future Enhancements

- Enhance the template for more detailed and contextually accurate questions.
- Expand the system to cover more subjects and specific curriculum topics.
- Allow users to select difficulty levels for the generated questions.
- Provide options to export the generated MCQs in different formats such as PDF or CSV.
- Improve the Streamlit interface to include interactive features like reviewing and editing generated MCQs.

