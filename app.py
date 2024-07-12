import streamlit as st
import pandas as pd
import random

# Function to load and process the CSV file
def load_data(file):
    df = pd.read_csv(file)
    grouped_data = {}
    meanings = {}

    for index, row in df.iterrows():
        word = row['WORD']
        meaning = row['MEANINGS']
        similar_words = row['SIMILAR WORDS'].split("\n")
        group_key = (meaning, row['OTHERS'])
        
        if group_key not in grouped_data:
            grouped_data[group_key] = []
        
        grouped_data[group_key].append(word)
        grouped_data[group_key].extend(similar_words)
        
        meanings[word] = meaning
        for similar_word in similar_words:
            meanings[similar_word] = meaning
    
    return grouped_data, meanings

# Function to generate a multiple choice question
def generate_question(grouped_data):
    group_key = random.choice(list(grouped_data.keys()))
    words = grouped_data[group_key]
    shown_word = random.choice(words)
    
    # Ensure that the correct word is different from the shown word
    correct_word = random.choice([word for word in words if word != shown_word])
    
    incorrect_words = []

    while len(incorrect_words) < 3:
        group_key_2 = random.choice(list(grouped_data.keys()))
        if group_key_2 != group_key:
            incorrect_word = random.choice(grouped_data[group_key_2])
            if incorrect_word not in incorrect_words:
                incorrect_words.append(incorrect_word)

    options = incorrect_words + [correct_word]
    random.shuffle(options)
    return shown_word, correct_word, options, group_key[0]

# Load the CSV file
file = 'nguphapgiongnhau.csv'  # Update with the path to your CSV file
grouped_data, meanings = load_data(file)

# Streamlit UI
st.title("Ôn Thi TOPIK: Chọn ngữ pháp giống nhau")
st.write("Chọn ngữ pháp giống nhau với ngữ pháp được hiển thị.")

if 'question' not in st.session_state:
    st.session_state.question = generate_question(grouped_data)
    st.session_state.correct = None
    st.session_state.selected_option = None

shown_word, correct_word, options, meaning = st.session_state.question

st.write(f"Chọn ngữ pháp giống với ngữ pháp sau đây: **{shown_word}**")
selected_option = st.radio("Options:", options, key="options")

if st.button("Kiểm tra"):
    st.session_state.selected_option = selected_option
    if selected_option == correct_word:
        st.session_state.correct = True
        st.success(f"Correct! Nghĩa của ngữ pháp này là: \n{meaning}")
    else:
        st.session_state.correct = False
        st.error(f"Sai rồi!! Ngữ pháp giống nhất là: {correct_word}")
        st.write(f"Nghĩa của ngữ pháp được chọn ({selected_option}) là: \n\n{meanings.get(selected_option, 'Meaning not found')}")

if st.button("Câu hỏi tiếp theo"):
    st.session_state.question = generate_question(grouped_data)
    st.session_state.correct = None
    st.session_state.selected_option = None
    st.experimental_rerun()  # Force a rerun to refresh the content
