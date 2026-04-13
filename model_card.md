# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

BetterMusic

## 2. Intended Use  

BetterMusic suggests songs from a small catalog based on a user's declared genre, mood, energy, and audio preferences. It is a classroom simulation and is not intended for real users or production use.

---


## 3. How the Model Works  

Every song gets a score from 0 to 1 based on how closely its genre, mood, energy, acousticness, valence, and tempo match the user's preferences, genre matters most and tempo matters least. One key change from the starter is that genre is not a strict yes/no match: related genres like r&b and hip-hop receive partial credit instead of scoring zero.

---

## 4. Data  

The catalog contains 19 songs across 16 genres and 15 moods, expanded from the original 10-song starter by adding hip-hop, r&b, country, classical, metal, blues, edm, folk, and dream pop. Genres like reggae, soul, and Latin are missing entirely, and most genres have only one song, which limits how well the system can rank within a genre.

---

## 5. Strengths  

The system works best for listeners with clear, common preferences — a chill lofi user or a high-energy pop user gets accurate, intuitive results because those genres have multiple catalog entries and distinctive numeric profiles. The genre similarity table also means a related-genre song can still surface rather than scoring zero, which produces more useful fallback recommendations than a strict binary match would.

---

## 6. Limitations and Bias 

The most significant weakness discovered during testing is that genre and mood together account for 50% of the maximum possible score (5.0 out of 10.0), which causes the system to lock users into a narrow taste bubble. A "Contradictory" profile was tested where the genre and mood were set to "lofi/chill" but the numeric preferences — energy 0.92, acousticness 0.10, and tempo 145 BPM — described a loud, fast, electronic sound; the system still returned quiet acoustic lofi tracks in the top results because the categorical match alone outweighed all four numeric mismatches. This means a user whose actual listening behavior has shifted (for example, a former lofi fan who now wants high-energy music) would continue receiving stale recommendations as long as their declared genre preference stays the same. The system also cannot surface cross-genre discoveries: a hip-hop listener with high valence and danceability preferences would likely enjoy certain pop or r&b tracks, but songs in those genres are structurally penalized unless they appear in the similarity table. In real recommendation systems this kind of genre lock-in is known as a filter bubble — the system keeps confirming what it already knows about you rather than helping you find something new.

---

## 7. Evaluation  

Six user profiles were tested: High-Energy Pop, Chill Lofi, Deep Intense Rock, Contradictory, No Genre Match, and All Middle. The first three were designed to reflect realistic listener types and produced results that matched intuition — the right songs showed up at the top with high scores and clear explanations. The three adversarial profiles were designed to stress-test the logic, and two of them produced genuinely surprising results. The Contradictory profile (lofi/chill genre and mood, but high energy and fast tempo) still returned quiet lofi tracks at the top — the system confidently recommended the opposite of what the numeric preferences described, because genre and mood alone were enough to dominate the score. The No Genre Match profile (genre set to "reggae," which does not exist in the catalog) showed the system losing most of its discriminating power: the top result won on a single mood match, and spots two through five were nearly tied because numeric proximity alone cannot separate songs meaningfully. The most unexpected finding was how rarely valence affected the rankings — in most profiles it contributed less than 0.1 points of separation between songs, making it the weakest feature in practice despite being included in the scoring rule.

---

## 8. Future Work  

The most impactful improvement would be replacing the declared taste profile with implicit signals, tracking what a user actually plays, skips, and replays so the system learns their preferences instead of asking them to state it upfront. Adding collaborative filtering so the system can compare a user's taste to other users would also help surface cross-genre discoveries that content-based scoring alone cannot find.

---

## 9. Personal Reflection  

First, building this made it clear that a recommender is only as good as the signals it has access to. Secondly, declaring a genre preference is a very blunt way to describe taste. Lastly, the system's biggest failures all came from that label overriding more nuanced numeric information. It also changed how I think about apps like Spotify, with massive amounts of complexity being abstracted away from something as simple as a recommendation system. One time I had to double check AI was when it suggested creating a dictionary with tuples that mapped to a correlation (for genres) and passed in a sorted list, but the keys weren't all sorted.
