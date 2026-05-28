import pandas as pd

# Load dataset
netflix_df = pd.read_csv("netflix_data.csv")

# Filter only movies
movies = netflix_df[netflix_df["type"] == "Movie"]

# Filter movies released in the 1990s
movies_1990s = movies[
    (movies["release_year"] >= 1990) &
    (movies["release_year"] < 2000)
]

# Find most frequent duration
duration = int(movies_1990s["duration"].mode()[0])

# Count short action movies
short_movie_count = movies_1990s[
    (movies_1990s["genre"] == "Action") &
    (movies_1990s["duration"] < 90)
].shape[0]

print("Most frequent duration:", duration)
print("Short action movie count:", short_movie_count)
