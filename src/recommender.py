from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv

    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")

    songs = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)  # reads header row automatically as keys

        for row in reader:
            # convert numeric fields from strings to correct types
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    float(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Computes a weighted score for how well a song matches a user's preferences.
    Returns the total score and a list of reasons explaining it.
    """
    total_score = 0.0
    reasons = []

    # --- Genre (weight: 0.40) ---
    genre_score = 1.0 if song["genre"] == user_prefs["favorite_genre"] else 0.0
    total_score += 0.40 * genre_score
    if genre_score:
        reasons.append("genre match (+0.40)")

    # --- Mood (weight: 0.25) ---
    mood_score = 1.0 if song["mood"] == user_prefs["favorite_mood"] else 0.0
    total_score += 0.25 * mood_score
    if mood_score:
        reasons.append("mood match (+0.25)")

    # --- Energy (weight: 0.25) ---
    # closeness: 1.0 = perfect match, 0.0 = furthest apart
    energy_score = max(0.0, 1.0 - abs(song["energy"] - user_prefs["target_energy"]))
    energy_contribution = round(0.25 * energy_score, 4)
    total_score += energy_contribution
    reasons.append(f"energy close to target (+{energy_contribution})")

    # --- Acousticness (weight: 0.10) ---
    if user_prefs["likes_acoustic"]:
        acoustic_score = 1.0 if song["acousticness"] > 0.5 else 0.0
    else:
        acoustic_score = 1.0 if song["acousticness"] <= 0.5 else 0.0
    total_score += 0.10 * acoustic_score
    if acoustic_score:
        reasons.append("matches acoustic preference (+0.10)")

    return total_score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)

    
    # Score every song by calling score_song on each one
    # Build a list of (song, score, reasons) tuples
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, reasons))

    # sorted() is used here instead of .sort() because:
    #   - sorted() returns a NEW list, leaving the original songs list unchanged
    #   - .sort() would mutate the original list in place, which is a side effect
    #     we want to avoid in a function that only reads data
    # reverse=True gives us descending order (highest score first)
    ranked = sorted(scored, key=lambda x: x[1], reverse=True)

    # Return only the top k results
    return ranked[:k]
