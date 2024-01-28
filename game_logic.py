from csv_reader import read_csv

import random

# Specify the path to your CSV file
csv_file_path = '2022-2023 NBA STATS - Sheet1.csv'
# Call the read_csv function from csv_reader module
csv_data = read_csv(csv_file_path)

DATA_CHOICES = 43
NUM_PLAYERS = 500

LOSE = False

more_or_better = ""
a_or_not = ""
stat = 0 #will take value between 1-43
player1 = 0 #will take value between 1-500
player2 = 0 #will take value between 1-500
wins = 0

def get_stat():
    global stat
    return stat

def get_player1():
    global player1
    return player1

def get_player2():
    global player2
    return player2

def a_or_not_func():
    global a_or_not
    return a_or_not

def more_or_better_func():
    global more_or_better
    return more_or_better

def get_numbers():
    global stat
    global player1
    global player2
    global wins
    global more_or_better
    global a_or_not


    stat = random.randint(1,DATA_CHOICES)
    if stat in (9, 14, 19, 20, 25):
        more_or_better = " a better "
        a_or_not = " a "
    else:
        more_or_better = " more "
        a_or_not = " "

    player1 = random.randint(1, NUM_PLAYERS)
    player2 = random.randint(1, NUM_PLAYERS)

    while csv_data[player1][stat] == csv_data[player2][stat]:
        player2 = random.randint(1, NUM_PLAYERS)



def game():
    global LOSE
    global stat
    global player1
    global player2
    global wins
    global more_or_better
    global a_or_not


    while LOSE == False:
        get_numbers()

        print("Who had" + more_or_better + csv_data[0][stat] + "? Enter 1 for " + csv_data[player1][0] +
        " or 2 for " + csv_data[player2][0])
        answer = (input("1 or 2? "))


        if answer == "1":

            if float(csv_data[player1][stat]) > float(csv_data[player2][stat]):
                print("Correct!")
                wins += 1
            else:
                print("Wrong!")
                LOSE = True

        elif answer == "2":

            if float(csv_data[player2][stat]) > float(csv_data[player1][stat]):
                print("Correct!")
                wins += 1
            else:
                print("Wrong!")
                LOSE = True
        else:
            print("You didn't Type 1 or 2. You lose!")
            LOSE = True
        print(csv_data[player1][0] + " had" + a_or_not + csv_data[player1][stat] + " " + csv_data[0][stat] +" and "
              + csv_data[player2][0] + " had" + a_or_not + csv_data[player2][stat] + " " + csv_data[0][stat]  + ".")

    print("Thank you for playing! Your score was " + str(wins))