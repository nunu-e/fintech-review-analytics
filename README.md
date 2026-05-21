# 🏦 Fintech Review Analytics

## 📌 Project Overview

This project analyzes Google Play Store reviews of Ethiopian banking mobile applications to extract actionable insights for improving customer experience.

The goal is to transform raw user feedback into:

- Sentiment insights
- Key complaint themes
- Business recommendations
- Data-driven product improvements

Banks analyzed:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

# 🧠 Problem Statement

Mobile banking users frequently express their experiences through app store reviews. However, this feedback is unstructured and difficult to interpret manually.

This project builds a full analytics pipeline to:

- Collect reviews
- Clean and process data
- Perform sentiment analysis
- Extract recurring themes
- Store structured data in PostgreSQL
- Generate business recommendations

---

# 📊 Dataset Description

- Source: Google Play Store
- Tool: `google-play-scraper`
- Total Reviews: 1200+ (400+ per bank)
- Fields collected:
  - Review text
  - Rating (1–5)
  - Review date
  - Bank name
  - Source

---

# 🧹 Data Preprocessing

Steps performed:

- Removed duplicate reviews
- Dropped missing values
- Standardized date format (YYYY-MM-DD)
- Selected required columns:
  - review
  - rating
  - date
  - bank
  - source

---

# 🧠 Sentiment Analysis

Sentiment classification was performed using:

- Model: DistilBERT
- Model Name: `distilbert-base-uncased-finetuned-sst-2-english`

Each review was labeled as:

- Positive
- Negative

A confidence score was also generated for each prediction.

---

# 🔍 Thematic Analysis

Themes were extracted using keyword-based grouping.

Identified themes:

- Account Access Issues (login, OTP, password)
- Transaction Performance (slow transfers, delays)
- App Stability (crashes, freezes, errors)
- UI & Design (interface feedback)
- Feature Requests (missing functionality)

---

# 🗄️ PostgreSQL Database Design

## Tables:

### banks

- bank_id (PK)
- bank_name
- app_name

### reviews

- review_id (PK)
- bank_id (FK)
- review_text
- rating
- review_date
- sentiment_label
- sentiment_score
- identified_theme
- source

---

# 📈 Visualizations

The following analyses were performed:

- Sentiment distribution by bank
- Rating distribution per bank
- Theme frequency per bank
- Sentiment trend over time

These visualizations help compare customer experience across banks.

---

# 📊 Key Insights

## CBE

- Strong overall sentiment
- Major complaints: OTP delays and slow transactions
- Users generally satisfied with usability

## BOA

- Lowest sentiment score among the three
- High frequency of crashes and login failures
- Needs stability improvements

## Dashen Bank

- Balanced sentiment
- Users request more features (fingerprint login, analytics tools)
- Occasional post-update bugs

---

# 🧠 Bank-Specific Product Recommendations

## 🟢 Commercial Bank of Ethiopia (CBE)

### Key Issues

- OTP/login failures
- slow transactions during peak hours

### Recommendations

- Improve OTP delivery reliability with fallback SMS systems
- Introduce trusted-device login sessions
- Optimize backend transaction processing for peak loads
- Scale infrastructure during high-traffic periods

---

## 🟠 Bank of Abyssinia (BOA)

### Key Issues

- app crashes and instability
- authentication issues

### Recommendations

- Prioritize bug fixing over feature development
- Implement crash monitoring tools (e.g., Firebase Crashlytics)
- Simplify login process and reduce OTP dependency
- Improve onboarding experience for new users

---

## 🔵 Dashen Bank

### Key Issues

- bugs after app updates
- missing user-requested features

### Recommendations

- Introduce staged rollout (beta testing → partial release → full release)
- Add fingerprint authentication login
- Implement budgeting and spending analytics tools
- Improve transaction notification system

---

# ⚙️ Technologies Used

- Python
- Google Play Scraper
- Pandas, NumPy
- Transformers (HuggingFace)
- Scikit-learn
- PostgreSQL
- SQLAlchemy
- Matplotlib / Seaborn
- Git & GitHub Actions

---

# 🧪 CI/CD Pipeline

A GitHub Actions workflow was implemented to:

- Install dependencies
- Run automated tests on every push to main branch

---

# ⚠️ Limitations

- Some banks had limited review availability
- Reviews are mostly in English (language bias)
- Sentiment model may misclassify sarcasm or context-heavy reviews
- Scraping rate limits affected full dataset extraction

---

# 🚀 Future Improvements

- Use deep topic modeling (LDA or BERTopic)
- Add multilingual sentiment analysis
- Deploy dashboard (Streamlit or Power BI)
- Integrate real-time review monitoring system

---

# 📌 Conclusion

This project demonstrates how unstructured user feedback can be transformed into actionable business intelligence using data engineering and NLP techniques.

It provides banks with:

- Clear understanding of customer pain points
- Product improvement priorities
- Data-driven decision-making support

---

# 👨‍💻 Author

Data Analytics Project — 10 Academy AI Mastery Program
