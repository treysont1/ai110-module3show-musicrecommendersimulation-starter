# Reflection: Comparing User Profile Outputs

---

## High-Energy Pop vs Chill Lofi

These two profiles sit at opposite ends of almost every numeric feature. The High-Energy Pop profile wants loud, fast, electronic songs — energy near 0.85, low acousticness, tempo around 125 BPM. The Chill Lofi profile wants the opposite — quiet, slow, acoustic songs with energy around 0.38 and acousticness near 0.75. As expected, their top results share no songs at all. What is interesting is how steep the score drop-off is in each list. Both profiles return a #1 result above 0.98, but by position #4 the scores have already fallen to the 0.58–0.79 range. This shows the catalog has strong coverage for both listener types at the top but runs out of good matches quickly after the first two or three songs.

---

## Deep Intense Rock vs Contradictory

This is the most revealing comparison. Both profiles ask for very similar numeric values — high energy (0.90 and 0.92), low acousticness (0.10), and fast tempo (148 and 145 BPM). The only difference is that Deep Intense Rock declares genre "rock" and mood "intense," while Contradictory declares genre "lofi" and mood "chill." Their top results are completely different. Deep Intense Rock gets Storm Runner at 0.99 — the right song, for the right reasons. Contradictory gets Midnight Coding at 0.78 — a quiet, slow lofi track that is the sonic opposite of what the numeric preferences describe. The lesson: two profiles that want the same sound can get entirely different recommendations just because of how their genre and mood labels are set. The system listens to the label more than it listens to the numbers.

---

## No Genre Match vs All Middle

Both of these profiles produce weaker, less confident results compared to the standard profiles — but for different reasons. No Genre Match fails because "reggae" is not in the catalog, so the genre feature contributes zero points for every song. The system is essentially running on five features instead of six, and the results feel scattered — songs from jazz, r&b, dream pop, and lofi all cluster near the same score because nothing separates them strongly. All Middle fails because every numeric preference is set to 0.50, which is close enough to the middle of every song's range that nothing scores much better than anything else on numeric grounds. In both cases, the top result wins almost entirely on a genre or mood match, and the rest of the list is basically arbitrary. This shows that the system needs strong signals in both the categorical and numeric features to produce a ranking that feels meaningful.

---

## Why Does Gym Hero Keep Appearing for Happy Pop Listeners?

Gym Hero is a pop song, which means it immediately earns genre match points for any pop profile — that alone is worth 3.0 out of 10.0 possible points. Its energy (0.93) is also close to the High-Energy Pop target (0.85), which adds another strong score. The system does notice that Gym Hero's mood is "intense" rather than "happy" and subtracts those 2.0 mood points — but by then, the genre and energy scores have already pushed it high enough to rank in the top five.

The problem is that "intense" and "happy" feel very different to a real listener, but the system treats a mood miss as just a missing 2.0 points rather than as a meaningful incompatibility. A person who wants upbeat, feel-good pop songs would probably skip Gym Hero after ten seconds. The system has no way to know that — it only sees numbers, and the numbers say "pop, high energy, low acoustic," which looks close enough.

This is a good example of the difference between a mathematically reasonable recommendation and a musically honest one.
