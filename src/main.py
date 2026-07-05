"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def print_recommendations(title: str, recommendations) -> None:
    print("\n" + "=" * 48)
    print(f"  {title}")
    print("=" * 48)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']}  —  {song['artist']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.split(", "):
            print(f"     • {reason}")

    print("\n" + "=" * 48)


def main() -> None:
    songs = load_songs("data/songs.csv") 

    print("Loaded songs:", len(songs))

    # Starter example profile
    #user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    user_prefs = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
        "likes_acoustic": True
    }

    # Opposite profile: high-energy electronic instead of low-energy acoustic
    opposite_prefs = {
        "favorite_genre": "edm",
        "favorite_mood": "energetic",
        "target_energy": 0.95,
        "likes_acoustic": False
    }

    # Contradictory profile: wants EDM but also wants it calm and acoustic.
    # The only edm song is high-energy and non-acoustic, so the genre/mood
    # weights (+3/+2) swamp the energy/acoustic signals the user also asked for.
    contradictory_prefs = {
        "favorite_genre": "edm",
        "favorite_mood": "energetic",
        "target_energy": 0.10,
        "likes_acoustic": True
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)
    print_recommendations("TOP RECOMMENDATIONS (lofi / chill)", recommendations)

    opposite_recommendations = recommend_songs(opposite_prefs, songs, k=5)
    print_recommendations("TOP RECOMMENDATIONS (edm / energetic)", opposite_recommendations)

    contradictory_recommendations = recommend_songs(contradictory_prefs, songs, k=5)
    print_recommendations("TOP RECOMMENDATIONS (edm but calm + acoustic)", contradictory_recommendations)


if __name__ == "__main__":
    main()
