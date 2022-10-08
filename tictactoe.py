import numpy as np
n=3
arr=[]
for i in range(n):
    r=[]
    for j in range(n):
        r.append('0')
    arr.append(r)
board=np.array(arr)
print((board))

def isnfill(board):
    flag=True
    for i in range(n):
        for j in range(n):
            if board[i][j]=='0':
                flag=False
                break
    if flag:
        return(0)
    else:
        return(1)
def show(board):
    for i in range(n):
        for j in range(n):
            if j==2:
                print(board[i][j])
            else:
                print(board[i][j], end=' ')
def winner(board, last):
    flag=False
    for i in range(n):
        if board[i][0]==board[i][1]==board[i][2]==last:
            flag=True
            break
    for j in range(n):
        if board[0][j]==board[1][j]==board[2][j]==last:
            flag=True
            break
    if board[0][0]==board[1][1]==board[2][2]==last:
        flag=True
    if board[0][2]==board[1][1]==board[2][0]==last:
        flag=True
    return(flag)
def start():
    p1=int(input("Enter your symbol\n 1:x \n 2:o\n "))
    if p1==1:
        s1='x'
        s2='o'
    else:
        s1='o'
        s2='x'

    last=s2
    print("Player 1 is ",s1)
    print("Player 2 is ",s2)
    while(isnfill(board)):

        if last==s2:
            print("Player 1's turn")
            row=int(input("Enter row:"))-1
            col=int(input("Enter column:"))-1
            if row in range(0,3) and col in range(0,3):
              if board[row][col]=='0':
                  board[row][col]=s1
                  last= s1
                  show(board)
                  if winner(board, last):
                      print("Player 1 wins")
                      break
              elif board[row][col]!='0':
                  print("Cannot make this move")
                  continue
            else:
              print("Invalid input. Please enter row and column numbers 1,2 or 3")
              continue
        if last==s1:
              print("Player 2's turn")
              row=int(input("Enter row:"))-1
              col=int(input("Enter column:"))-1
              if row in range(0,3) and col in range(0,3):
                if board[row][col]=='0':
                    board[row][col]=s2
                    last= s2
                    show(board)
                    if winner(board, last):
                        print("Player 2 wins")
                        break
                elif board[row][col]!='0':
                    print("Cannot make this move")
                    continue

              else:
                print("Invalid input. Please enter row and column numbers 1,2 or 3")
                continue
    if not isnfill(board):
      print("It's a tie")
start()