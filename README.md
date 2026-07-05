# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world recommendation systems such as Spotify use both collaborative and content-based filtering. Collaborative filtering recommends based on patterns across users, while content-based filtering recommends based on the attributes of the items themselves. In this system, content-based filtering is prioritized. 

Features used:

- `Song`: genre, mood, energy, acousticness
- `UserProfile`: favorite_genre, favorite_mood, target_energy, likes_acoustic

### Algorithm Recipe (scoring)

Each song earns points against the user profile, then songs are ranked by total.

| Signal | Match rule | Points |
|---|---|---|
| Genre | `song.genre == favorite_genre` | **+3** |
| Mood | `song.mood == favorite_mood` | **+2** |
| Energy | closeness to `target_energy` | **+2 × (1 − \|diff\|)** |
| Acoustic | `likes_acoustic and acousticness > 0.6` | **+1** |

Genre outweighs mood (3 vs 2) because genre is the stronger taste signal; mood
just refines ties within a genre. Energy is distance-based so near matches score
well instead of needing an exact float match.

```
user_prefs + songs ─► score_song (per song) ─► sort desc ─► top k
```

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
User profile: 
- "favorite_genre": "lofi",
- "favorite_mood": "chill", 
- "target_energy": 0.35,
- "likes_acoustic": True
================================================
  TOP RECOMMENDATIONS
================================================

1. Library Rain  —  Paper Lanterns
   Score: 8.00
   Reasons:
     • genre match (lofi)
     • mood match (chill)
     • energy close to target (0.35 vs 0.35)
     • acoustic (0.86)

2. Midnight Coding  —  LoRoom
   Score: 7.86
   Reasons:
     • genre match (lofi)
     • mood match (chill)
     • energy close to target (0.42 vs 0.35)
     • acoustic (0.71)

3. Focus Flow  —  LoRoom
   Score: 5.90
   Reasons:
     • genre match (lofi)
     • energy close to target (0.40 vs 0.35)
     • acoustic (0.78)

4. Spacewalk Thoughts  —  Orbit Bloom
   Score: 4.86
   Reasons:
     • mood match (chill)
     • energy close to target (0.28 vs 0.35)
     • acoustic (0.92)

5. Coffee Shop Stories  —  Slow Stereo
   Score: 2.96
   Reasons:
     • energy close to target (0.37 vs 0.35)
     • acoustic (0.89)

================================================

```

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



