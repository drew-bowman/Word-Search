#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 21:38:08 2018

@author: Drew
"""
import random
import string

def make_blank_board(rows, cols):
    board = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append('*')
        board.append(row)

    return board

def print_board(board, words):
    header = "–––"
    for x in range(cols):
        header += "––"
    print(header)
    
    for row in board:
        text = '| '
        for col in row:
            text += col + ' '
        print(text + "|")
    
    print(header)
    print("Hidden Words:")
    for word in words:
        print(word)
        
def fill_blanks(board):
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == '*':
                board[r][c] = random.choice(string.ascii_uppercase)

def place_word(board, word):
    orientation = round(random.random())
    if orientation == 0:
        flipped = ''
        for letter in word:
            flipped = letter + flipped
        word = flipped
    
    placement_type = random.randint(0,3)
    if placement_type == 0:
        place_horiz(board, word)
    elif placement_type == 1:
        place_vert(board, word)
    elif placement_type == 2:
        place_diag_backw(board, word)
    else:
        place_diag_forw(board, word)
    
def place_horiz(board, word):
    row = int(random.random() * rows)
    col = int(random.random() * (cols - len(word) + 1))
    
    failed = False
    for letter in word:
        if board[row][col] == '*' or board[row][col] == letter:
            col += 1
        else:
            failed = True
            
    if failed == False:
        col -= len(word)
        for letter in word:
            board[row][col] = letter
            col += 1
    else:
        place_word(board, word)
        
def place_vert(board, word):
    row = int(random.random() * (rows - len(word) + 1))
    col = int(random.random() * (cols))
    
    failed = False
    for letter in word:
        if board[row][col] == '*' or board[row][col] == letter:
            row += 1
        else:
            failed = True
            
    if failed == False:
        row -= len(word)
        for letter in word:
            board[row][col] = letter
            row += 1
    else:
        place_word(board, word)    
            

            
def place_diag_forw(board, word):
    row = int((random.random() * (rows - len(word) + 1)) + len(word) -1)
    col = int(random.random() * (cols - len(word) + 1))
    
    failed = False
    for letter in word:
        if board[row][col] == '*' or board[row][col] == letter:
            col += 1
            row -= 1
        else:
            failed = True
            
    if failed == False:
        col -= len(word)
        row += len(word)
        for letter in word:
            board[row][col] = letter
            col += 1
            row -= 1
    else:
        place_word(board, word)
    
def place_diag_backw(board, word):
    row = int(random.random() * (rows - len(word) + 1))
    col = int(random.random() * (cols - len(word) + 1))
    
    failed = False
    for letter in word:
        if board[row][col] == '*' or board[row][col] == letter:
            col += 1
            row += 1
        else:
            failed = True
            
    if failed == False:
        col -= len(word)
        row -= len(word)
        for letter in word:
            board[row][col] = letter
            col += 1
            row += 1
    else:
        place_word(board, word)
            
#=========================================================================
# Start of Program

# Get words
words = []
print("Enter words to include in word search (enter blank line when finished): ")
should_continue = True
while should_continue:
    word = input("")
    if word == "":
        should_continue = False
    else:
        words.append(word)

# Sort by length, since we'll want to place the large words first
len_sorted_words = sorted(words, key=len, reverse=True)
max_word = len(len_sorted_words[0])

# Get size of board, make sure it's possible
print("Recommended size:", max_word, "X", max_word)

acceptable_size = False
while acceptable_size == False:
    print("Enter dimensions:")
    rows = int(input("Rows = "))
    cols = int(input("Columns = "))
    if rows < max_word and cols < max_word:
        print("At least one dimension must be greater than or equal to " + str(max_word))
    else:
        acceptable_size = True
    print()

# Make the board
board = make_blank_board(rows, cols)

# Place every word
for word in len_sorted_words:
    place_word(board, word.upper())

# Fill in the blanks in the board with random letters
fill_blanks(board)

# Display the board
print_board(board, words)
    


        