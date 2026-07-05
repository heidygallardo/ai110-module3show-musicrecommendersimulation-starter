import csv
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
    """Load songs from a CSV file into a list of dicts."""
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a single song against user preferences, returning the score and reasons."""
    score = 0.0
    reasons: List[str] = []

    # Genre: strongest taste signal (+3)
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 3
        reasons.append(f"genre match ({song['genre']})")

    # Mood: refines ties within a genre (+2)
    if song["mood"] == user_prefs["favorite_mood"]:
        score += 2
        reasons.append(f"mood match ({song['mood']})")

    # Energy: distance-based so near matches still score well (+2 x (1 - |diff|))
    diff = abs(song["energy"] - user_prefs["target_energy"])
    energy_points = 2 * (1 - diff)
    if energy_points > 0:
        score += energy_points
        reasons.append(f"energy close to target ({song['energy']:.2f} vs {user_prefs['target_energy']:.2f})")

    # Acoustic: bonus when the user likes acoustic and the song is clearly acoustic (+1)
    if user_prefs["likes_acoustic"] and song["acousticness"] > 0.6:
        score += 1
        reasons.append(f"acoustic ({song['acousticness']:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs scored and ranked against user preferences."""
    scored = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    scored.sort(key=lambda item: item[1], reverse=True)
    return [
        (song, score, ", ".join(reasons) if reasons else "no strong matches")
        for song, score, reasons in scored[:k]
    ]
