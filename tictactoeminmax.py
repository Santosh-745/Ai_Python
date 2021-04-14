def checkWinner(mat, box):
    winner = None
    # print("Box "+str(box))
    # Vertical
    for i in range(0,3):
        if(mat[0][i] == mat[1][i] ==  mat[2][i] and (mat[0][i] == 'X' or mat[0][i] == 'O')):
            winner = mat[0][i]
    # Handizontal
    for i in range(0,3):
        if(mat[i][0] == mat[i][1] == mat[i][2]  and (mat[i][0] == 'X' or mat[i][0] == 'O')):
            winner = mat[i][0]
    # Diagonal
    if(mat[0][0] == mat[1][1] == mat[2][2]  and (mat[0][0] == 'X' or mat[0][0] == 'O')):
        winner = mat[0][0]
    # Diagonal
    elif(mat[2][0] == mat[1][1] == mat[0][2] and (mat[0][2] == 'X' or mat[0][2] == 'O')):
        winner = mat[0][2] 
    elif(box <= 0 and winner == None):
        winner = "Tie"
    return winner

def displayBoard(board):
    for i in range (0,3):
        for j in range (0,3):
            print(board[i][j],end=" ")
        print()
    
def move(board,player,no):
    x , y = map(int , input(" ==> Enter move for Player "+no+" ==> ").split())
    board[x-1][y-1] = player
    return board

def best_score(board,isMax,box):
    rank = {
        'X' : -1,
        'O': 1,
        'Tie' : 0 
    }
    # print(checkWinner(board,box))
    if(checkWinner(board,box) != None):
        # print("Winner Found")
        bestScore = rank[checkWinner(board,box)] 
        return bestScore

    elif(isMax):
        bestScore = -10
        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j] == "-"):
                    board[i][j] = "O"
                    box = box - 1
                    score = best_score(board,False,box) #False for isMax or not & Max is stand for humans 
                    displayBoard(board)
                    print("Score "+str(score))
                    print()
                    if(score >= bestScore):
                        bestScore = score
                    board[i][j] = "-"
                    box = box + 1
        return bestScore 

    elif(isMax == False):
        bestScore = 10
        # print("False")
        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j] == "-"):
                    board[i][j] = "X"
                    box = box - 1
                    score = best_score(board,True,box) #True for isMax or not & Max is stand for humans 
                    displayBoard(board)
                    print("Score "+str(score))
                    print()
                    if(score <= bestScore):
                        bestScore = score
                    board[i][j] = "-"
                    box = box + 1
        return bestScore

def best_move(board,box):
    bestScore = 10
    x , y = 0 , 0
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j] == "-"):
                board[i][j] = "X"
                box = box - 1
                score = best_score(board,True,box) #True for isMax or not & Max is stand for humans 
                displayBoard(board)
                print("Score "+str(score))
                if(score <= bestScore):
                    bestScore = score
                    print("Best Score "+str(bestScore))
                    x , y = i , j
                board[i][j] = "-"    
    board[x][y] = "X"
    return board     

def main():
    board = [['X','O','X'],['O','-','X'],['-','-','-']]
    # board = [['-','-','-'],['-','-','-'],['-','-','-']]
    displayBoard(board)

    box = 3
    # box = 9
    # Game Loop
    while True:
        # .......Human Turn......
        board = move(board,'O','1')
        displayBoard(board)
        box = box - 1
        winner = checkWinner(board,box)
        if(winner is not None and winner != "Tie"):
            print(" ==> Winner is Player 1 ==> " + str(winner))
            break
        elif(box == 0 and winner == "Tie"):
            print("Match Ends with Tie")
            break
        # .......Computer Turn.......
        board = best_move(board,box)
        print(" ==> Move of Player 2 ==> ")
        displayBoard(board)    
        box = box - 1
        winner = checkWinner(board,box)
        if(winner is not None):
            print(" ==> Winner is Player 2 ==> "+str(winner))
            break

if __name__ == "__main__":
    main()
