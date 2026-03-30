# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

During my experiments I discovered that the system is heavily biased toward genre due to its high weight and binary scoring. Since genre contributes a large portion of the total score, it often dominates the ranking before other features like energy or acousticness, are meaningfully considered. During testing, this caused songs with a genre match but weaker overall alignment to rank above songs that were better matches across multiple continuous features. In conclusion, the recommender can overlook more nuanced matches and produce less balanced recommendations.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested three difeferent user profiles to see how the recommender behaves. 

The first profile was a "Happy Pop" listener, the second used "electronic" as genre which did not exist in the dataset, and the third had conflicting preferences since it wanted both very high energy and a sad mood. 

One suprising result was that songs like "Gym Hero" kept appearing even for users who just wanted "Happy Pop". This happened because the system gives a lot of weight to genre and energy, so a high-energy pop song can rank highly even if the mood does not match. In the profile that had the missing genre, the system ignored the genre entirely and relied on other features. Overall making the recommendations less accurate. 

These user profiles showed that the system can be overly influenced by certain features and does not always handle unusual or conflicting preferences as well.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
