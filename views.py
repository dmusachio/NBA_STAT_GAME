from flask import Blueprint, render_template, request, jsonify
from game_logic import get_numbers, csv_data, get_stat, get_player1, get_player2, a_or_not_func, more_or_better_func

global former_player_1
global former_player_2
global former_stat

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/play_game")
def play_game():
    return render_template("play_game.html")

@views.route('/play', methods=['POST'])
def play():
    global LOSE, wins, former_stat, former_player_1, former_player_2, a_or_not
    LOSE = False
    wins = 0
    get_numbers()
    stat = get_stat()
    former_stat = stat
    player1 = get_player1()
    former_player_1 = player1
    player2 = get_player2()
    former_player_2 = player2
    a_or_not = a_or_not_func()
    more_or_better = more_or_better_func()

    # Construct the initial game info
    initial_game_info = f"Who has {more_or_better}{a_or_not}{csv_data[0][stat]}? " \
                        f"Player 1: {csv_data[player1][0]} or Player 2: {csv_data[player2][0]}"
    return jsonify({'next_question': initial_game_info})

@views.route('/make_guess', methods=['POST'])
def make_guess():
    global LOSE
    global wins
    global former_stat
    global former_player_1
    global former_player_2
    global a_or_not
    global more_or_better


    LOSE = False




    #get_numbers()
    #stat = get_stat()
    #player1 = get_player1()
    #player2 = get_player2()
    #a_or_not = a_or_not_func()

    #print(stat)

    player_choice = int(request.form['choice'])

    if player_choice not in [1, 2]:
        return "Invalid choice. Please choose 1 or 2."



    result = ""
    if player_choice == 1:
        if float(csv_data[former_player_1][former_stat]) > float(csv_data[former_player_2][former_stat]):
            result = "Correct!"
            wins += 1
        else:
            result = "Wrong!"
            LOSE = True

    if player_choice == 2:
        if float(csv_data[former_player_2][former_stat]) > float(csv_data[former_player_1][former_stat]):
            result = "Correct!"
            wins += 1
        else:
            result = "Wrong!"
            LOSE = True


    if LOSE == True:
        return jsonify({'result': result, 'game_info': 'Game Over', 'next_question': 'Game Over', 'wins': wins})


    game_info = f"{csv_data[former_player_1][0]} had {a_or_not}{csv_data[former_player_1][former_stat]} " \
                f"{csv_data[0][former_stat]} and {csv_data[former_player_2][0]} had {a_or_not}{csv_data[former_player_2][former_stat]} {csv_data[0][former_stat]}."

    get_numbers()
    former_stat = get_stat()
    former_player_1 = get_player1()
    former_player_2 = get_player2()
    a_or_not = a_or_not_func()
    more_or_better = more_or_better_func()

    next_question = f"Who has {more_or_better}{a_or_not}{csv_data[0][former_stat]}? " \
                    f"Player 1: {csv_data[former_player_1][0]} or Player 2: {csv_data[former_player_2][0]}"

    return jsonify({'result': result, 'game_info': game_info, 'next_question': next_question, 'wins': wins})