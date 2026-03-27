# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**SonicVibe Recommender 1.0**  

---

## 2. Intended Use  

The SonicVibe Recommender generates custom song playlists based on a user's current mood and exact audio preferences. It assumes the user knows the specific vibe they want to hear, down to the energy and tempo. This model is built for classroom exploration and testing to understand recommendation algorithms. It is not designed for live production use or to replace commercial streaming apps. Instead, it acts as a safe sandbox for developers to observe how small math changes impact listener experiences.

---

## 3. How the Model Works  

The model looks at text tags like genre and mood, alongside musical numbers like energy, tempo, and acousticness. It compares these song features to a user's ideal target numbers. The system calculates the mathematical gap between what the user wants and what the song actually sounds like. Smaller gaps earn higher percentage match scores. During testing, we changed the starter logic to give more weight to the actual musical traits. This ensures a song with the perfect sonic math can beat a song that simply matches the genre text. Specifically, it uses an additive point system to total these matches up. Finally, it sorts the catalog from highest to lowest score to present the user with their Top 5 playlist.

---

## 4. Data  

The dataset is a custom catalog containing 17 songs. It covers a wide range of genres, including pop, lofi, rock, metal, classical, and hip-hop. We added 7 new songs to the original starter file to test extreme moods like "aggressive," "epic," and "carefree." Because it is a miniature dataset, it completely misses major aspects of real-world musical taste, such as release year, vocal style, popularity, and lyrical themes.

---

## 5. Strengths  

The system works incredibly well for users with focused, highly aligned requests, such as finding a high-energy pop track for the gym. It accurately captures the physical feel of a song by heavily weighting traits like energy and valence. The recommendations match human intuition best when the user's requested genre naturally matches their requested audio numbers. Another major strength is its complete transparency. Because the algorithm outputs a specific list of "reasons" for every score, users always understand exactly why a track was recommended to them.

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

To improve the model, the first step is adding an Artist Diversity Filter to prevent the system from recommending five songs by the same person in a row. I also want to fix the rigid text-matching so a request for "pop" can still recognize and reward an "indie pop" track. Finally, future versions should include a slight randomness factor to slowly introduce new, out-of-bounds genres to the user to encourage musical discovery.

---

## 9. Personal Reflection  

I learned that text labels like genre can easily overpower actual audio data if the math is not balanced carefully. It was surprising to see how an algorithm can do exactly what it is programmed to do, yet still deliver a bad user experience. For example, our early model recommended an aggressive metal track to a user wanting happy music simply because the genre tag matched. This project completely changed the way I think about big music streaming apps. It made me realize how much hidden logic they must use to break listeners out of filter bubbles and echo chambers.
