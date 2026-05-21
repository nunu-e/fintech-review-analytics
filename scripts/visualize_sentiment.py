import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load analyzed dataset
df = pd.read_csv("data/processed/reviews_final_analysis.csv")

# create figure
plt.figure(figsize=(10,6))

# sentiment distribution
sns.countplot(
    data=df,
    x="bank",
    hue="sentiment_label"
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.tight_layout()

# save chart
plt.savefig("sentiment_distribution.png")

plt.show()