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

One significant limitation of the current system is its vulnerability to an "exact-match string trap," which inherently creates a rigid filter bubble. Because the algorithm relies on strict text matching for categorical tags, it completely ignores highly related styles, such as awarding zero genre points to an "indie pop" track when a user explicitly requests "pop." Furthermore, because the scoring logic evaluates each song in a vacuum without enforcing playlist variety, the system easily overfits and creates an artist echo chamber if one musician's catalog perfectly aligns with the target audio traits. Ultimately, this strict, uncontextualized scoring unintentionally favors users with mainstream, easily categorized tastes while heavily penalizing listeners who prefer nuanced subgenres.

---

## 7. Evaluation  

* **Profiles Tested:** We evaluated the engine using a custom CLI test runner (`src/main.py`) against "Golden Path" profiles (e.g., *The Gym Banger*) to verify standard behavior, and "Adversarial" edge cases (e.g., *The Happy Goth*, *Speedcore Lofi*) to stress-test the limits of the scoring logic.
* **Testing Focus:** The primary goal was to observe how the algorithm resolved conflicts between categorical text tags (Genre/Mood) and continuous mathematical audio features (Energy, Valence, Tempo) when generating the top 5 recommendations.
* **Surprising Findings:** The adversarial tests revealed a severe "Tag Tyranny" vulnerability. For instance, in *The Happy Goth* test, the system initially recommended an aggressive metal track with entirely mismatched audio features over a pop track with mathematically perfect audio traits. The flat +3.0 point bonus for matching text tags was acting as an insurmountable wall against the actual sonic math. 
* **Resolution:** This discovery forced a structural update to the scoring recipe, requiring us to nerf the categorical bonuses (+1.5 for Genre) and buff the emotional multipliers (Valence x1.5) to ensure a perfectly matched audio profile could outcompete rigid text labels.

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
