import streamlit as st
from transformers import pipeline

# Title
st.title("🚀 AI Content Generator")

# Load better model (faster & better than GPT-2)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="distilgpt2")

generator = load_model()

# User input
topic = st.text_input("Enter topic")

# Generate button
if st.button("Generate"):
    if topic:
        # Improved prompt
        prompt = f"Write a short, engaging Instagram caption about {topic}. Keep it clear, creative, and avoid repetition."

        # Generate output with better settings
        result = generator(
            prompt,
            max_new_tokens=80,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.9,
            repetition_penalty=1.5
        )

        # Clean output (remove prompt)
        output = result[0]['generated_text'].replace(prompt, "")

        st.subheader("✨ Generated Content:")
        st.write(output)

    else:
        st.warning("Please enter a topic")
        
#python -m streamlit run ui.py