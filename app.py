import streamlit as ui
import pandas as pd
from transformers import pipeline

# Initialize Streamlit application
ui.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")
ui.title("📊 Real-Time Sentiment Analysis Dashboard")
ui.write("Analyze public sentiment instantly using state-of-the-art NLP models.")

# Initialize NLP Pipeline
@ui.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

sentiment_pipeline = load_model()

# User input selection
input_mode = ui.radio("Select Input Method:", ("Single Text Analysis", "Bulk CSV Upload"))

if input_mode == "Single Text Analysis":
    text_input = ui.text_area("Enter text to analyze:", placeholder="Type something here...")
    if ui.button("Analyze Sentiment"):
        if text_input.strip():
            result = sentiment_pipeline(text_input)[0]
            label = result['label']
            score = result['score']
            
            if label == "POSITIVE":
                ui.success(f"😊 Positive Sentiment (Confidence: {score:.2%})")
            else:
                ui.error(f"😞 Negative Sentiment (Confidence: {score:.2%})")
        else:
            ui.warning("Please enter some text to analyze.")

elif input_mode == "Bulk CSV Upload":
    uploaded_file = ui.file_uploader("Upload a CSV file (Must contain a 'text' column)", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if 'text' in df.columns:
            with ui.spinner('Analyzing entries...'):
                results = sentiment_pipeline(df['text'].astype(str).tolist())
                df['Sentiment'] = [r['label'] for r in results]
                df['Confidence'] = [r['score'] for r in results]
            
            ui.write("### Analysis Results Summary")
            pos_count = (df['Sentiment'] == 'POSITIVE').sum()
            neg_count = (df['Sentiment'] == 'NEGATIVE').sum()
            
            col1, col2 = ui.columns(2)
            col1.metric("Positive Sentiments", pos_count)
            col2.metric("Negative Sentiments", neg_count)
            
            ui.dataframe(df)
            
            # Download result
            csv = df.to_csv(index=False).encode('utf-8')
            ui.download_button("Download Processed CSV", data=csv, file_name="sentiment_results.csv", mime="text/csv")
        else:
            ui.error("The uploaded CSV must contain a column named 'text'.")
