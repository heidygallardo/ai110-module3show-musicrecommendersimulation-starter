"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    # Updated profile with full feature set

    profiles = [
       {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False
        },

        { # user_prefs_missing_genre
        "favorite_genre": "electronic",
        "favorite_mood":  "happy",
        "target_energy":  0.80,
        "likes_acoustic": False,
        },

        { # user_prefs_energy_mood_conflict (high energy, sad mood)
        "favorite_genre": "country",
        "favorite_mood":  "sad",
        "target_energy":  0.95,
        "likes_acoustic": False,
        }

    ]

    for i, profile in enumerate(profiles, 1):
        print(f"\n=== Profile {i} ===")
        print(profile)

        recommendations = recommend_songs(profile, songs, k=5)

        print("\nTop recommendations:\n")
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {', '.join(explanation)}")
            print()
    

    # recommendations = recommend_songs(user_prefs, songs, k=5)

    # print("\nTop recommendations:\n")
    # for rec in recommendations:
    #     # You decide the structure of each returned item.
    #     # A common pattern is: (song, score, explanation)
    #     song, score, explanation = rec
    #     print(f"{song['title']} - Score: {score:.2f}")
    #     print(f"Because: {explanation}")
    #     print()


if __name__ == "__main__":
    main()
