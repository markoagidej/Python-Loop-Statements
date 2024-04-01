# Task 1: Your Mood Tracker

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
times = ["morning", "afternoon", "evening"]

for day in days:
    for time in times:
        print(f"On {day} {time} you felt {random.choice(moods)}")