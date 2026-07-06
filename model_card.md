# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**MusicGenie 1.0**  

---

## 2. Intended Use  

MusicGenie 1.0 is a simple content-based recommender that suggests songs from a small catalog by matching each track's genre, mood, energy, and acousticness against a user's stated preferences and returning a ranked top-k list. It assumes the user can describe their taste as a favorite genre, favorite mood, a target energy level, and whether they like acoustic music, and that those stated preferences fully represent what they want. It is built for classroom exploration of how recommender systems work — not for real users or production use.

---

## 3. How the Model Works  

The model gives every song a score and then picks the highest ones. It looks at four things about each song: its genre, its mood, its energy level, and how acoustic it is.

It compares those to what the user wants: a favorite genre, a favorite mood, a target energy level, and whether they like acoustic music.

Each match adds points. A matching genre adds the most points, because genre is the strongest hint of taste. A matching mood adds a few points. Energy is scored by how close the song is to the user's target — closer means more points. Liking acoustic music adds a small bonus for songs that are clearly acoustic.

The points are added up into one score. The songs with the highest scores are recommended, and the model lists the reasons each song was chosen.

The starter code just returned the first few songs without really thinking. The main change was building this points-based scoring so the results actually reflect the user's preferences.

---

## 4. Data  

The catalog has 18 songs. Each song has a genre, a mood, an energy level, a tempo, and a few other traits.

Many genres are represented, like pop, lofi, rock, jazz, hip-hop, classical, edm, and folk. The moods are varied too, such as happy, chill, intense, relaxed, and energetic.

A lot of musical taste is missing. Most genres have only one song, so choices run out fast. There is no data on popularity, release year, language, or artist history. This makes the catalog too small to represent real-world music taste.

---

## 5. Strengths  

The system works best for users with clear, consistent taste. When someone wants a calm, acoustic, low-energy vibe, the top songs match that mood well.

It captures the energy signal nicely. Songs close to the user's target energy rise to the top, so a high-energy request returns high-energy songs.

The results also match intuition when preferences agree with each other. The lofi/chill profile returned calm lofi and acoustic songs, which is exactly what you would expect.

Genre matching is another strength. If a genre is well represented in the catalog, the system reliably surfaces songs from it.

---

## 6. Limitations and Bias 

The system over-prioritizes genre relative to the other attributes when scoring. As a result, same-genre songs outrank better-fitting cross-genre songs, even when a user's energy, mood, or acoustic preferences point elsewhere.


---

## 7. Evaluation  

**User profiles tested.** The recommender was run against three contrasting profiles defined in `src/main.py`:

1. **Aligned profile (lofi / chill).** Favorite genre `lofi`, favorite mood `chill`, target energy `0.35`, likes acoustic. Every preference points the same direction — calm, low-energy, acoustic — so this is the "easy" case where all four signals reinforce one another.
2. **Opposite profile (edm / energetic).** Favorite genre `edm`, favorite mood `energetic`, target energy `0.95`, does not like acoustic. A high-energy electronic mirror image of the first profile, used to confirm the ranking flips as expected.
3. **Contradictory profile (edm but calm + acoustic).** Favorite genre `edm`, favorite mood `energetic`, but target energy `0.10` and likes acoustic. The preferences conflict internally: the only EDM song in the catalog is high-energy and non-acoustic, so the genre/mood weights (+3/+2) swamp the energy and acoustic signals the user also asked for. This profile stress-tests the over-prioritization of genre noted in Section 6.

**Comparing the outputs.** The differences between profiles behaved as expected. Genre was the primary divider: the EDM/energetic profile pulled electronic tracks to the top while the acoustic/chill profile surfaced lofi and folk songs, so the two rankings barely overlapped. Within that genre split the secondary signals lined up too — the EDM profile favored higher-energy, danceable tracks, while the acoustic profile shifted toward low-energy, acoustic-guitar songs. Placing the two rankings side by side made both the genre separation and the energy/acousticness contrast obvious, confirming that genre sets the overall grouping and the other signals then move results in opposite directions within it.


---

## 8. Future Work  

The biggest change would be to stop letting genre dominate. Right now a genre match adds so many points that it outweighs everything else. I would lower the genre weight so energy, mood, and acousticness matter more, which would also add more variety to the top results.

I would also handle case sensitivity better. A genre like "EDM" should still match "edm", so the model should compare preferences in a consistent way instead of needing an exact match.

Finally, I would add more data. A bigger catalog with more songs per genre would give users real choices instead of running out after one match.

---

## 9. Personal Reflection  

From building this system, I learned how platforms like Spotify use collaborative and content-based filtering to recommend songs to their users. 

While building the content-based recommendation system, something interesting was how the recommendation depends on the algorithm built as well as the attributes taken into account. Overall, changing the way I view recommendation systems. Rather than thinking about them as magic, I now see the intuition behind these systems.


