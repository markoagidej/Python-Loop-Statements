# Task 1: The Selective DJ

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
genres_sublist = genres[1:]


# Task 2: The One-Liner Band with List Comprehensions

music_list = [str(genre) + " Music" for genre in genres]
print(music_list)


# Task 3: Numerical Beats with range

for countdown in range(10, 0, -1):
    print(countdown)

print("The beat drops now!")