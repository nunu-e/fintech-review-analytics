from google_play_scraper import reviews, Sort
import pandas as pd

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in apps.items():

    result, _ = reviews(
        app_id,
        lang="en",
        country="us",
        sort=Sort.NEWEST,
        count=1000
    )

    print(bank, "->", len(result))

    for r in result:
        all_reviews.append({
            "review": r["content"],
            "rating": r["score"],
            "date": r["at"],
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)

df.to_csv("data/raw/reviews_raw.csv", index=False)

print("TOTAL REVIEWS:", len(df))