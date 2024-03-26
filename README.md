1. The Range Riddle
Objective:
The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. You will correct a code snippet, simulate moods for different days, and create a countdown timer.

Task 1: Your Mood Today
Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.

Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."

2. Double Scoop with Nested Loops
Objective:
The aim of this assignment is to practice using nested loops in Python. You will correct a nested loop code snippet, simulate a mood tracker, and generate a multiplication table.

Task 1: Your Mood Tracker
Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it.

Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"

3. Loop Condition Logic
Objective:
The aim of this assignment is to explore the importance of the loop condition in while loops. You will create loops with different conditions to see how they influence the behavior of the loop.

Task 1: Loop Condition Exploration
Write a while loop with a condition that will never be true (an infinite loop). Inside the loop, print a statement. Then, use a break statement to exit the loop after 5 iterations.

Task 2: Conditional Exit
Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. The loop should terminate naturally once the condition is met.

4. Python's Random Game Night
Objective:
The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness into your programs.

Task 1: Random Choice Game
Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.

5. Looping Lists - The Rhythm of Repetition
Objective:
Dive into the heart of Python loops with a musical twist. Your task is to explore different ways of looping through lists, each with its unique style and purpose. By the end of this assignment, you will be able to control your loops like a DJ controls the tracks, ensuring each element gets its time to shine.

Task 1: The for Loop DJ Set
Using the provided genres list, write a for loop that prints out each genre with a custom message. Extend this task by adding a counter that displays the number of the track before the genre.

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
Task 2: The Remix Artist with while
Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but also includes a condition to stop the loop if a certain genre is played for instance Hip-hop.

Task 3: Light Show Technician Loop
Using the range() function, loop through the genres list by index. For each genre, print out the track number and a message that the light show is ready. Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.

6. Advanced Looping Techniques
Objective:
Advance your looping skills by exploring more complex list manipulations. You will learn to selectively loop through parts of a list, use list comprehensions for concise code, and generate numerical lists with Python's range function.

Task 1: The Selective DJ
Loop through a slice of the genres list from the previous question and print out the genres. Use slicing to create a sublist of genres from the second to the fourth track.

Task 2: The One-Liner Band with List Comprehensions
Use a list comprehension to create a new list that contains each genre with the word "Music" appended to it. Print this new list.

Task 3: Numerical Beats with range
Write a loop using range() to print out a countdown from 10 to 1, followed by the message "The beat drops now!".