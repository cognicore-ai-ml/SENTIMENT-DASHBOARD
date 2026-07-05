# Sentiment Analysis Dashboard

A clean, responsive dashboard built with Streamlit and Hugging Face Transformers to perform single-text and bulk CSV sentiment analysis.

## Project Structure
```text
sentiment-dashboard/
├── app.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/sentiment-dashboard.git
   cd sentiment-dashboard
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Dashboard application:**
   ```bash
   streamlit run app.py
   ```

## Usage
- **Single Text Analysis:** Type text into the text area to evaluate whether it has positive or negative sentiment along with a confidence metric.
- **Bulk CSV Upload:** Upload a CSV file that includes a column named `text`. The application will evaluate all entries and provide a downloadable breakdown of the processed sentiment markers.
