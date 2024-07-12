# Korean Grammar Multiple Choice Quiz

This project is a Streamlit application designed to help users practice Korean grammar by answering multiple-choice questions. The app reads a CSV file containing Korean grammar patterns, their meanings, and similar expressions. It then generates quiz questions where users have to identify the correct similar word.

## Live Demo

You can access the live demo of the application here: [Korean Grammar Multiple Choice Quiz](https://nguphapgiongnhau.streamlit.app/)

## Features

- Reads and processes a CSV file with Korean grammar patterns.
- Groups words and their similar words based on their meanings.
- Generates multiple-choice questions to test the user's knowledge.
- Provides feedback on whether the selected answer is correct or incorrect.
- Displays the meaning of the correct answer and the selected answer if it's incorrect.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/korean-grammar-quiz.git
    cd korean-grammar-quiz
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure your CSV file is properly formatted and placed in the project directory. Update the file path in the script if necessary.

2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

3. Open your web browser and navigate to `http://localhost:8501` to interact with the application.

## CSV File Format

The CSV file should have the following columns:
- `WORD`
- `MEANINGS`
- `SIMILAR WORDS`
- `OTHERS`

Example:
```csv
WORD,MEANINGS,SIMILAR WORDS,OTHERS
-(으)ㄴ/는 것 같다,"Chỉ sự suy đoán, phỏng đoán => Có vẻ, dường như","-(으)ㄴ/는 듯하다\n-나보다\n-(으)ㄴ/는 모양이다",-(으)ㄴ/는 것 같다,"Chỉ sự suy đoán, phỏng đoán => Có vẻ, dường như
-----
-(으)ㄴ/는 듯하다
-나보다
-(으)ㄴ/는 모양이다"
