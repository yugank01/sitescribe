from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    # Use the Hugging Face model for sentiment analysis
    result = sentiment_pipeline(text)
    
    # Extract the label and score
    sentiment = result[0]["label"]  # "POSITIVE" or "NEGATIVE"
    score = result[0]["score"]      # Confidence score
    
    return {"sentiment": sentiment, "confidence": score}
