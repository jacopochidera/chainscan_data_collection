import nltk
from nltk.sentiment import SentimentIntensityAnalyzer



# Ensure you run nltk.download('vader_lexicon') before using VADER

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(content: str):
    sentiment_scores = sia.polarity_scores(content)
    if sentiment_scores['compound'] >= 0.05:
        return "positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"