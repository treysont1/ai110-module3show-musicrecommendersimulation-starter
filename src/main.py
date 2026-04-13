"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from tabulate import tabulate
from recommender import load_songs, recommend_songs


# ---------------------------------------------------------------------------
# User profiles
# ---------------------------------------------------------------------------

# Standard profiles
HIGH_ENERGY_POP = {
    "genre":        "pop",
    "mood":         "happy",
    "energy":       0.85,
    "valence":      0.80,
    "acousticness": 0.15,
    "tempo_bpm":    125,
    "likes_acoustic": False,
}

CHILL_LOFI = {
    "genre":        "lofi",
    "mood":         "chill",
    "energy":       0.38,
    "valence":      0.60,
    "acousticness": 0.75,
    "tempo_bpm":    78,
    "likes_acoustic": True,
}

DEEP_INTENSE_ROCK = {
    "genre":        "rock",
    "mood":         "intense",
    "energy":       0.90,
    "valence":      0.45,
    "acousticness": 0.10,
    "tempo_bpm":    148,
    "likes_acoustic": False,
}

# Adversarial / edge case profiles
CONTRADICTORY = {
    # Genre and mood say quiet/relaxed, but energy and tempo say loud and fast.
    # Tests whether numeric features can override categorical ones.
    "genre":        "lofi",
    "mood":         "chill",
    "energy":       0.92,
    "valence":      0.50,
    "acousticness": 0.10,
    "tempo_bpm":    145,
    "likes_acoustic": False,
}

NO_GENRE_MATCH = {
    # "reggae" is not in the catalog — forces the system to rank entirely
    # on numeric proximity with no genre contribution.
    "genre":        "reggae",
    "mood":         "relaxed",
    "energy":       0.55,
    "valence":      0.70,
    "acousticness": 0.50,
    "tempo_bpm":    95,
    "likes_acoustic": False,
}

ALL_MIDDLE = {
    # Every numeric value set to 0.5 — tests whether the system produces
    # a meaningful ranking or collapses into near-identical scores.
    "genre":        "ambient",
    "mood":         "chill",
    "energy":       0.50,
    "valence":      0.50,
    "acousticness": 0.50,
    "tempo_bpm":    119,
    "likes_acoustic": False,
}

PROFILES = {
    "High-Energy Pop":   HIGH_ENERGY_POP,
    "Chill Lofi":        CHILL_LOFI,
    "Deep Intense Rock": DEEP_INTENSE_ROCK,
    "Contradictory":     CONTRADICTORY,
    "No Genre Match":    NO_GENRE_MATCH,
    "All Middle":        ALL_MIDDLE,
}


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in PROFILES.items():
        print(f"\n{'='*72}")
        print(f"  Profile: {profile_name}")
        print(f"  Preferences: genre={user_prefs['genre']}, mood={user_prefs['mood']}, "
              f"energy={user_prefs['energy']}, tempo={user_prefs['tempo_bpm']} BPM")
        print(f"{'='*72}")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        rows = []
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            rows.append([
                rank,
                song["title"],
                f"{song['genre']} / {song['mood']}",
                f"{score:.2f}",
                explanation,
            ])

        print(tabulate(
            rows,
            headers=["#", "Title", "Genre / Mood", "Score", "Why"],
            tablefmt="rounded_outline",
            maxcolwidths=[None, 22, 18, None, 38],
        ))
        print()


if __name__ == "__main__":
    main()
