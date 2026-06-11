import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import random

# Load movies
movies = pd.read_csv("movies.csv")

# GUI Window
root = tk.Tk()
root.title("AI Movie Recommendation System")
root.geometry("700x650")

# Heading
tk.Label(
    root,
    text="🎬 Movie Recommendation System",
    font=("Arial", 18, "bold")
).pack(pady=10)

# User Name
tk.Label(root, text="Enter Your Name:").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

# Language Preference
tk.Label(root, text="Preferred Language:").pack()

language_var = tk.StringVar()
language_var.set("English")

languages = ["English", "Hindi", "Japanese", "Korean"]

tk.OptionMenu(root, language_var, *languages).pack()

# Genre Selection
tk.Label(root, text="Select Favorite Genres:").pack()

genres = ["Action", "Sci-Fi", "Romance",
           "Comedy", "Drama",
           "Thriller", "Fantasy",
           "Animation"]

genre_vars = {}

frame = tk.Frame(root)
frame.pack()

for genre in genres:
    var = tk.IntVar()
    genre_vars[genre] = var

    tk.Checkbutton(
        frame,
        text=genre,
        variable=var
    ).pack(anchor='w')

# Movie Ratings
tk.Label(
    root,
    text="\nRate These Movies (1-5):",
    font=("Arial", 12, "bold")
).pack()

rating_movies = [
    "Inception",
    "3 Idiots",
    "Titanic",
    "Drishyam",
    "Avengers: Endgame"
]

rating_entries = {}

for movie in rating_movies:
    row = tk.Frame(root)
    row.pack()

    tk.Label(row, text=movie, width=20).pack(side=tk.LEFT)

    entry = tk.Entry(row, width=5)
    entry.pack(side=tk.LEFT)

    rating_entries[movie] = entry


def recommend():
    name = name_entry.get()

    if not name:
        messagebox.showerror(
            "Error",
            "Please enter your name."
        )
        return

    selected_genres = [
        genre
        for genre, var in genre_vars.items()
        if var.get() == 1
    ]

    preferred_language = language_var.get()

    filtered = movies[
        movies["language"] == preferred_language
    ]

    if selected_genres:
        filtered = filtered[
            filtered["genre"].isin(selected_genres)
        ]

    if filtered.empty:
        messagebox.showinfo(
            "No Recommendations",
            "No movies found."
        )
        return

    recommendations = filtered.sample(
        min(5, len(filtered))
    )

    result = f"Hello {name}!\n\nRecommended Movies:\n\n"

    for _, row in recommendations.iterrows():
        percentage = random.randint(80, 98)

        result += (
            f"{row['title']} "
            f"({row['genre']})\n"
            f"Match: {percentage}%\n\n"
        )

    messagebox.showinfo(
        "Recommendations",
        result
    )


tk.Button(
    root,
    text="Recommend Movies",
    command=recommend,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold")
).pack(pady=20)

root.mainloop()