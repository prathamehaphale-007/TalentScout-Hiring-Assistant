import pandas as pd
import os
from datetime import datetime
from textblob import TextBlob

DB_FILE = "candidates_db.csv"

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the candidate's response.
    Returns: 'Positive', 'Neutral', or 'Negative' and a score.
    """
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity
    
    if score > 0.1:
        return "Positive", score
    elif score < -0.1:
        return "Negative", score
    else:
        return "Neutral", score

def save_candidate_data(data_dict):
    """Saves candidate info to a CSV file."""
    data_dict['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df_new = pd.DataFrame([data_dict])
    
    if not os.path.exists(DB_FILE):
        df_new.to_csv(DB_FILE, index=False)
    else:
        df_new.to_csv(DB_FILE, mode='a', header=False, index=False)

def is_exit_command(text):
    """Checks for conversation ending keywords."""
    keywords = ['exit', 'quit', 'bye', 'end', 'stop', 'cancel']
    return text.lower().strip() in keywords