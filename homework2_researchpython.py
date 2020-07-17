# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:00:25 2020

@author: dorcos
"""


import math
import random

import matplotlib.pyplot as plt
import time

# =============================================================================
# exercise 1
# =============================================================================
#For our tic-tac-toe board, we will use a numpy array with dimension 3 by 3.
#Write a function create_board() that creates such a board with the value of 
#each cell set to the integer 0.
#Call create_board() and store it.
#What is the correct numpy function to initialize our tic-tac-toe board?
import numpy as np
def create_board():
    b = np.zeros((3,3), dtype = int)
    return b
# =============================================================================
# exercise 2
# =============================================================================
#Players 1 and 2 will take turns changing values of this array from a 0 to a 1 or 2, 
#indicating the number of the player who places a marker there.
#Create a function place(board, player, position), where:
#- player is the current player (an integer 1 or 2).
#- position is a tuple of length 2 specifying a desired location to place their marker.
#Your function should only allow the current player to place a marker on the board 
#(change the board position to their number) if that position is empty (zero).
#Use create_board() to store a board as board, and use place to have Player 1 place 
# marker on location (0, 0).
#What is the correct way to use the place function to have Player 1 place a marker 
#on location (0,0)?
def rand():
    return random.choice([0,1,2,3])
def loc():
    return (rand(),rand())

def place(board, player, position):
    board = create_board()
    if player == 1:
        if board == 0:
            board[a,b] = 1
    elif player == 2:
        if position == empty:
            board[a,b] = 2
    else:
        print('not good input argument\n')

    return (board,player,position)
# =============================================================================
# board version of edx
# =============================================================================
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board
    
board = create_board()

##Create a function possibilities(board) that returns a list of all positions (tuples) 
#on the board that are not occupied (0). (Hint: numpy.where is a handy function that returns
# a list of indices that meet a condition.)
#numpy.where

def possibilities(board):
    return list(zip(*np.where(board == 0)))

# =============================================================================
# ex4
# =============================================================================
#Write a function random_place(board, player) that places a marker for the current player 
#at random among all the available positions (those currently set to 
import random
random.seed(1)
def possibilities(board):
    return list(zip(*np.where(board == 0)))

def random_place(board, player):
    selection  = possibilities(board)
    placement = random.choice(selection)
    board[placement] = player
    return board
    
# =============================================================================
# ex5
# =============================================================================
#Call random_place(board, player) to place three pieces each on board for players 1 and 2.
random.seed(1)
board = create_board()
random_place(board,1)
random_place(board,2)
random_place(board,1)
random_place(board,2)
random_place(board,1)
random_place(board,2)

for i in range(3):
    for player in [1, 2]:
        random_place(board, player)

# =============================================================================
# ex6
# =============================================================================
#ake a function row_win(board, player) that takes the player (integer) and determines 
#if any row consists of only their marker.
#Have it return True if this condition is met and False otherwise.
#Note that board is already defined as in Exercise 5. Call row_win to check if Player 1 
#has a complete row.
#Does Player 1 have a complete row?
        
def row_win(board, player):
    if np.any(np.all(board==player, axis=1)): 
        # this checks if any row contains all positions equal to player.
        return True
    else:
        return False

# =============================================================================
# ex7
# =============================================================================
#Make a function col_win(board, player) that takes the player (integer) and determines 
#if any column consists of only their marker.
#Have it return True if this condition is met and False otherwise.
#Note that board is already defined as in Exercise 5. Call col_win to check if 
#Player 1 has a complete column.
#Does Player 1 have a complete column?

def col_win(board,player):
    if np.any(np.all(board==player, axis=0)):
        return True
    else:
        return False
    
# =============================================================================
# ex8
# =============================================================================
#create a function diag_win(board, player) that takes the player (integer) and 
#determines if any diagonal consists of only their marker.
#Have it return True if this condition is met and False otherwise.
#Note that board is modified from Exercise 5. Call diag_win to check if Player 2 
#has a complete diagonal.
#Use this sample code to get started:

board[1,1] = 2
def diag_win(board,player):
    if board[0,0] & board[1,1] & board[2,2] == player:
        return True
    elif board[0,2] & board[1,1] & board[2,0] == player:
        return True
    else:
        return False
#version
def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        # np.diag returns the diagonal of the array
        # np.fliplr rearranges columns in reverse order
        return True
    else:
        return False
    
# =============================================================================
# ex9
# =============================================================================
#Create a function evaluate(board) that uses row_win, col_win, and diag_win functions 
#for both players. If one of them has won, return that player's number. 
#If the board is full but no one has won, return -1. Otherwise, return 0.
#Note that board is defined as in Exercise 8. 
#Call evaluate to see if either player has won the game yet.
        
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board,player) is True:
            return player
        elif col_win(board,player) is True:
            return player
        elif diag_win(board,player) is True:
            return player
        pass
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

##version
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
# =============================================================================
# ex 10
# =============================================================================
#Create a function play_game() that:

#- Creates a board.

#- Alternates taking turns between two players (beginning with Player 1), placing 
#a marker during each turn.

#- Evaluates the board for a winner after each placement.

#- Continues the game until one player wins (returning 1 or 2 to reflect the winning player),
# or the game is a draw (returning -1).

#Call play_game 1000 times, and store the results of the game in a list called results. 
#Use random.seed(1) so we can check your answer!

#How many times does Player 1 win out of 1000 games?
random.seed(1)
board = create_board()
for i in range(10):
    play_game()
    
def play_game():
    for i in range(4):
        for player in [1,2]:
            results = list(play_set())
    return results
        
    def play_set():
        possibilities(board)
        random_place(board, player)
        winner = evaluate(board)
        return board, winner
        
random.seed(1)
board = create_board()
while board == 1: 
    for player in [1,2]:
        play_game()
        
        
random.seed(1)
def play_game():
    board = create_board()
    while True:
       for player in [1, 2]:
           #possibilities(board)
           random_place(board, player)
           result = evaluate(board)
           if result != 0:
               return result
random.seed(1)
wins = []
lose = []
totals = 500
for i in range(totals):
   if play_game1() == 1 or 2:
       wins.append(play_game1())
print('total:', len(wins))
print('player 1:', wins.count(1))
print('player 2:', wins.count(2))
print(lose)


def play_game1():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner
# =============================================================================
# ex11
# =============================================================================
#Create a function play_strategic_game(), where Player 1 always starts with the middle square, 
#and otherwise both players place their markers randomly.

#Call play_strategic_game 1000 times.

#Set the seed to 1 using random.seed(1) again.

#How many times does Player 1 win out of 1000 games with this new strategy?

random.seed(1)
def play_strategic_game():
    board = create_board()
    for player in [1]:
        board[1,1] = 1
    for player in [1,2]:
        play_game1()
    return play_game1()

        
random.seed(1)
wins= []
lose = []
totals = 1000
for i in range(totals):
   if play_strategic_game() == 1 or 2:
       wins.append(play_strategic_game())
   
print('total:', len(wins))
print('player 1:', wins.count(1))
print('player 2:', wins.count(2))