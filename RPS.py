import os
import random

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux & Mac
    else:
        os.system('clear')

clear_terminal()

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    else:
        opponent_history.clear()

    # Use opponent history to predict next move
    if len(opponent_history) < 5:
        return 'R'

    pattern = "".join(opponent_history[-3:])
    predictions = {"R": 0, "P": 0, "S": 0}

    for i in range(len(opponent_history) - 3):
        seq = "".join(opponent_history[i:i+3])
        if seq == pattern:
            next_move = opponent_history[i+3]
            predictions[next_move] += 1

    if sum(predictions.values()) == 0:
        predicted = opponent_history[-1]
    else:
        predicted = max(predictions, key=predictions.get)

    counter = {"R": "P", "P": "S", "S": "R"}
    move = counter[predicted]

    # Add slight unpredictability: shift move every 15 rounds
    rounds = len(opponent_history)
    
    if rounds % 15 == 0:
        move = {"R": "S", "P": "R", "S": "P"}[move]

    return move