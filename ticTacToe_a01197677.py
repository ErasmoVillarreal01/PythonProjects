board = [["-","-","-",],["-","-","-",],["-","-","-",]]
player1=""
player2=""
count=0
winner=0

def inputPosic():    
    row = int(input("Enter Position 1 (between 1 and 3) "))
    col= int(input("Enter Position 2 (between 1 and 3)): "))

    while(True):
        if (row > 3 or row < 0) or (col > 3 or row < 0):
            row = int(input("Enter Again Position 1 (between 1 and 3) "))
            col= int(input("Enter Again Position 2 (between 1 and 3)): "))

        else:
            return(row,col)
            break
    
def printBoard():
    for i in range(0,3):
        for j in range(0,3):
            print(board[i][j], end="")
        print("")

def winnerIs(p1,p2):
    global winner

    if (board[0][0] == 'X'  and board[0][1]== 'X' and board[0][2] == 'X'):
        print("You are the Winner " + p1)
        winner=winner +1 

    if (board[1][0] == 'X'  and board[1][1]== 'X' and board[1][2] == 'X'):
        print("You are the Winner " + p1)
        winner=winner +1 
    
    if (board[2][0] == 'X'  and board[2][1]== 'X' and board[2][2] == 'X'):  #horizontalWin
        print("You are the Winner " + p1)
        winner=winner +1 

    if (board[0][0] == 'X'  and board[1][0]== 'X' and board[2][0] == 'X'): #VerticalWin
        print("You are the Winner " + p1)
        winner=winner +1 

    if (board[0][1] == 'X'  and board[1][1]== 'X' and board[2][1] == 'X'):
        print("You are the Winner " + p1)
        winner=winner +1 
    
    if (board[0][2] == 'X'  and board[1][2]== 'X' and board[2][2] == 'X'): 
        print("You are the Winner " + p1)
        winner=winner +1 
    
    if (board[0][2] == 'X'  and board[1][1]== 'X' and board[2][0] == 'X'): #Crossed
        print("You are the Winner " + p1)
        winner=winner +1 
    
    if (board[0][0] == 'X'  and board[1][1]== 'X' and board[2][2] == 'X'): 
        print("You are the Winner " + p1)
        winner=winner +1 

    #Player2
    if (board[0][0] == 'O'  and board[0][1]== 'O' and board[0][2] == 'O'):
        print("You are the Winner " + p2)
        winner=winner +1 

    if (board[1][0] == 'O'  and board[1][1]== 'O' and board[1][2] == 'O'):
        print("You are the Winner " + p2)
        winner=winner +1 
    
    if (board[2][0] == 'O'  and board[2][1]== 'O' and board[2][2] == 'O'):  #horizontalWin
        print("You are the Winner " + p2)
        winner=winner +1

    if (board[0][0] == 'O'  and board[1][0]== 'O' and board[2][0] == 'O'): #VerticalWin
        print("You are the Winner " + p2)
        winner=winner +1 

    if (board[0][1] == 'O'  and board[1][1]== 'O' and board[2][1] == 'O'):
        print("You are the Winner " + p2)
        winner=winner +1

    if (board[0][2] == 'O'  and board[1][2]== 'O' and board[2][2] == 'O'): 
        print("You are the Winner " + p2)
        winner=winner +1
    
    if (board[0][2] == 'O'  and board[1][1]== 'O' and board[2][0] == 'O'): #Crossed
        print("You are the Winner " + p2)
        winner=winner +1 
    
    if (board[0][0] == 'O'  and board[1][1]== 'O' and board[2][2] == 'O'): 
        print("You are the Winner " + p2)
        winner=winner +1 

def writeBoard(position, player):
    global count
    r= position[0] - 1
    c= position[1] - 1
    
    if(player == player1):
        if(board[r][c] =='-'):
            board[r][c] = str('X')
        else:
            print("Invalid Position, please enter another one")
            count= count - 1

    else:
        if(board[r][c] =='-'):
            board[r][c] = str('O')
        else:
            print("Invalid Position, please enter another one")
            count= count - 1



try:   
    while(count < 10):
        if (count == 0):
            player1=(str((input("Enter Player X name "))))
            player2= (str((input("Enter Player O name "))))
            count = count +1
        else:
            printBoard()
            
            if (winner == 0):

                if (count%2 == 0):
                    print("It's your turn, "+ player2 +"!")
                    posic = inputPosic()
                    writeBoard(posic,player2)
                    count= count + 1
                    
                else:
                    print("It's your turn, "+ player1 +"!")
                    posic = inputPosic()
                    writeBoard(posic,player1)
                    count= count + 1
                
                if(count > 1):
                    winnerIs(player1,player2)
            else:
                print("------ Game Over -------")
                count=11

except KeyboardInterrupt:
    pass