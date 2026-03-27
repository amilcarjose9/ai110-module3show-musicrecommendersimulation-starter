"""
Command line runner for the Music Recommender Simulation.

This file helps you test your recommender against multiple 
golden path and adversarial user profiles.
"""

from recommender import load_songs, recommend_songs

def main() -> None:
    # 1. Load the catalog
    songs = load_songs("data/songs.csv") 

    # 2. Define the test profiles
    test_profiles = {
        "The Gym Banger (Golden Path)": {
            "favorite_genre": "pop",
            "favorite_mood": "intense",
            "target_energy": 0.95,
            "target_valence": 0.75,
            "target_danceability": 0.90,
            "target_acousticness": 0.05,
            "target_tempo_bpm": 135
        },
        "The Acoustic Purist (Golden Path)": {
            "favorite_genre": "folk",
            "favorite_mood": "melancholy",
            "target_energy": 0.20,
            "target_valence": 0.15,
            "target_danceability": 0.30,
            "target_acousticness": 0.95,
            "target_tempo_bpm": 65
        },
        "Speedcore Lofi (Adversarial)": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.99,
            "target_valence": 0.10,
            "target_danceability": 0.20,
            "target_acousticness": 0.00,
            "target_tempo_bpm": 160
        },
        "The Happy Goth (Adversarial)": {
            "favorite_genre": "metal",
            "favorite_mood": "aggressive",
            "target_energy": 0.85,
            "target_valence": 0.95,
            "target_danceability": 0.88,
            "target_acousticness": 0.70,
            "target_tempo_bpm": 110
        }
    }

    # 3. Loop through and test each profile
    for profile_name, prefs in test_profiles.items():
        print("\n" + "=" * 60)
        print(f" 🎧 TESTING PROFILE: {profile_name.upper()} 🎧")
        print("=" * 60)

        recommendations = recommend_songs(prefs, songs, k=5)

        for rank, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            
            print(f"\n[{rank}] {song['title']} by {song['artist']}")
            print(f"    Match Score: {score:.2f} pts")
            print("    Why it matched:")
            
            if explanation == "No specific matches found.":
                print(f"      - {explanation}")
            else:
                reasons = explanation.split(", ")
                for reason in reasons:
                    print(f"      ✓ {reason}")

    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
