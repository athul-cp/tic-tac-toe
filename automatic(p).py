import numpy as np
import random
from time import sleep

#creating a 2d array
def create():
    return(np.array([[0,0,0],
                     [0,0,0],
                     [0,0,0]]))

#checking empty position 
def possible(board):
    a=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                a.append((i,j))
    return(a)

#selecting places
def random_pos(board,player):
    select=possible(board)
    current_pos=random.choice(select)
    board[current_pos]=player
    return(board)

def row(board,player):
    for x in range(len(board)):
        win=True
        for y in range(len(board)):
            if board[x,y]!=player:
                win=False
                continue
        if win==True:
            return(win)
    return(win)

def col(board,player):
    for x in range(len(board)):
        win=True
        for y in range(len(board)):
            if board[y][x]!=player:
                win=False
                continue
        if win==True:
            return(win)
    return(win)

def diagonal(board,player):
    win = True
    y = 0
    for x in range(len(board)): 
        if board[x, x] != player: 
            win = False
    if win: 
        return win 
    win = True
    if win: 
        for x in range(len(board)): 
            y = len(board) - 1 - x 
            if board[x, y] != player: 
                win = False
    return win 
def check(board):
    winner = 0
      
    for player in [1, 2]: 
        if (row(board, player) or
            col(board,player) or 
            diagonal(board,player)): 
                 
            winner = player 
              
    if np.all(board != 0) and winner == 0: 
        winner=0
    return winner 
    
    

#main()
def start():
    board,winner,no=create(),0,1
    print(board)
    sleep(2)
    while winner==0:
        for player in[1,2]:
            board=random_pos(board,player)
            print("After the move" +str(no))
            print(board)
            sleep(2)
            no=no+1
            winner=check(board)
            if winner!=0:
                break
    return(winner)


print("The Winner is:"+str(start()))



