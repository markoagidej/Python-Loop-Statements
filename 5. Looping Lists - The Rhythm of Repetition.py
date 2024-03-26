# Task 1: The for Loop DJ Set

import random

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in genres:
    if genre == "Jazz":
        print("Jazz - Smooooth")
    elif genre == "Rock":
        print("Rock - Get the blood pumping")
    elif genre == "Hip-hop":
        print("Hip-hop - Hype it up")
    elif genre == "Classical":
        print("Classical - Sophisticated")

print("End Task 1")


# Task 2: The Remix Artist with while
        
index = random.choice(range(4))

while index != 2:
    if index == 0:
        print("Jazz - Smooooth")
    elif index == 1:
        print("Rock - Get the blood pumping")
    elif index == 2:
        print("Hip-hop - Hype it up")
    elif index == 3:
        print("Classical - Sophisticated")
    
    index = random.choice(range(4))

print("End Task 2")

# Task 3: Light Show Technician Loop
## The writing in this task is terrible
    
for genre_index in range(4): #would be safer to use len(genres) - 1 
    if genre_index != 4:
        print(str(genre_index) + " Lightshow is ready!")
    else:
        continue
