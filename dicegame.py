# Title: Dice Roll Game - Who Wins More?

# Can you create a Python program that simulates a dice roll game between two players? 
# The game should run for a specified number of rounds, with each player rolling two dice 
# in each round. Based on the total score of the dice rolls, the program should determine the winner
# of each round. Additionally, the program should keep track of the number of rounds won by 
# each player and display the overall winner at the end. As a bonus, can you store the results 
# of each round in an SQLite database for future reference?

import random
import sqlite3

# Establishing the SQLite connection and creating a table
connection = sqlite3.connect("python_project2/dice_game_results.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS dice_game_results
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   player1_score INTEGER,
                   player2_score INTEGER);''')
connection.commit()

player1score = 0
player2score = 0

name = input("Enter your name: ")
print(f"Hi {name}, Welcome to the Dice Game :)")

print(f"{name} has 2 dice")
print("Player2 has 2 dice")

n = int(input("Please enter the number of rounds you want to play in the dice roll game: "))
for i in range(n): # n - number of rounds
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(dice1)
    print(dice2)
    player1 = dice1 + dice2
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    print(dice3)
    print(dice4)
    player2 = dice3 + dice4
    print(f"{name} rolled: ", player1)
    print("player2 rolled: ", player2)
    if player1 > player2:
        player1score = player1score + 1
        print(f"{name} wins")
    elif player2 > player1:
        player2score = player2score + 1
        print("player2 wins")
    else:
        print("draw")

    # Inserting data into the SQLite table after each game
    cursor.execute("INSERT INTO dice_game_results (player1_score, player2_score) VALUES (?, ?);", (player1, player2))
    connection.commit()

print(f"Total {name} score:", player1score)
print("Total Player2 score:", player2score)

if player1score > player2score:
    print(f"{name} is the Winner!!!!!")
elif player2score > player1score:
    print("Player2 is the Winner!!!!!")
else:
    print("Draw!!!!!")

# Closing the database connection
connection.close()
