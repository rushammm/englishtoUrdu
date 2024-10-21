import streamlit as st
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

# Load the Hugging Face model for English-to-Roman Urdu translation
@st.cache_resource
def load_model():
    model_name = "your-hf-model-name"  # Replace this with your actual Hugging Face model name
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return pipeline("translation", model=model, tokenizer=tokenizer)

translator = load_model()

# Streamlit app layout
st.title("English to Roman Urdu Translator")

# Input field for the English prompt
input_text = st.text_area("Enter English text to translate:", height=100)

# Button to trigger translation
if st.button("Translate"):
    if input_text:
        # Translate English text to Roman Urdu
        try:
            translation = translator(input_text)
            roman_urdu_text = translation[0]['translation_text']
            st.subheader("Roman Urdu Translation:")
            st.write(roman_urdu_text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.write("Please enter some text to translate.")
