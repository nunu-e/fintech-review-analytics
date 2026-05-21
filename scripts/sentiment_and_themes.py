import pandas as pd
from transformers import pipeline

# Load dataset
df = pd.read_csv("data/processed/reviews_clean.csv")

# Create review_id
df.reset_index(inplace=True)
df.rename(columns={"index": "review_id"}, inplace=True)

# Rename column
df.rename(columns={"review": "review_text"}, inplace=True)

# Load sentiment model
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

labels = []
scores = []

# Sentiment prediction
for text in df["review_text"].fillna("").astype(str):

    result = sentiment_model(text[:512])[0]

    labels.append(result["label"])
    scores.append(result["score"])

# Save scores
df["sentiment_score"] = scores

# Better sentiment labels
final_labels = []

for label, score in zip(labels, scores):

    if score < 0.60:
        final_labels.append("neutral")

    elif label == "POSITIVE":
        final_labels.append("positive")

    else:
        final_labels.append("negative")

df["sentiment_label"] = final_labels

# Theme assignment
def assign_theme(text):

    text = text.lower()

    if "login" in text or "otp" in text or "password" in text:
        return "Account Access Issues"

    if "transfer" in text or "slow" in text or "delay" in text:
        return "Transaction Performance"

    if "crash" in text or "freeze" in text or "error" in text:
        return "App Stability"

    if "ui" in text or "design" in text or "interface" in text:
        return "UI & Design"

    if "feature" in text or "missing" in text:
        return "Feature Requests"

    return "General Feedback"

df["identified_theme"] = df["review_text"].apply(assign_theme)

# Sentiment summary
bank_summary = df.groupby("bank")["sentiment_score"].mean()

print("\nAverage Sentiment Score Per Bank:")
print(bank_summary)

# Distribution
print("\nSentiment Distribution:")
print(df.groupby("bank")["sentiment_label"].value_counts())

# Theme frequency
print("\nTheme Frequency:")
print(df["identified_theme"].value_counts())

# Save final dataset
df.to_csv("data/processed/reviews_final_analysis.csv", index=False)

print("\nDONE: Sentiment and Theme Analysis Completed")