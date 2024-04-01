# Task 1: Your Mood Today

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]

for day in range(7):
    if day == 0:
        print(f"Sunday: {random.choice(moods)}")
    elif day == 1:
        print(f"Monday: {random.choice(moods)}")
    elif day == 2:
        print(f"Tuesday: {random.choice(moods)}")
    elif day == 3:
        print(f"Wednesday: {random.choice(moods)}")
    elif day == 4:
        print(f"Thursday: {random.choice(moods)}")
    elif day == 5:
        print(f"Friday: {random.choice(moods)}")
    else:
        print(f"Saturday: {random.choice(moods)}")