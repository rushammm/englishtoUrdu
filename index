import streamlit as st
from transformers import pipeline

# Load the Hugging Face model for English-to-Roman Urdu translation
@st.cache_resource
def load_model():
    return pipeline("translation_en_to_roman_urdu", model="your-hf-model-name")

translator = load_model()

# Streamlit app layout
st.title("English to Roman Urdu Translator")

# Input field for the English prompt
input_text = st.text_area("Enter English text to translate:", height=100)

# Button to trigger translation
if st.button("Translate"):
    if input_text:
        # Translate English text to Roman Urdu
        translation = translator(input_text)
        roman_urdu_text = translation[0]['translation_text']
        st.subheader("Roman Urdu Translation:")
        st.write(roman_urdu_text)
    else:
        st.write("Please enter some text to translate.")

# To run the streamlit app, use the following command:
# streamlit run your_script_name.py
