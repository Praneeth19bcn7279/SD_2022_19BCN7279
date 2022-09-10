def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j],end="\t")
        print()
def addPlayerCharacters(pos,grid,player):
    for i in range(5):
        if pos==0:
            grid[pos][i]=str('A-')+player[i]
        else:
            grid[pos][i]=str('B-')+player[i]
    printGrid(grid)
def checkEndGame(grid):
    a=0
    b=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j][0]=='A':
                a+=1
            if grid[i][j][0]=='B':
                b+=1
    if a==0 or b==0:
        return False
    return True
def getChar(grid,ch,pl):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if len(grid[i][j])==4 and grid[i][j][0]==pl:
                if grid[i][j][2:4]==ch:
                    return i,j
    
grid=[["." for x in range(5)] for x in range(5)]
moves=['F','B','R','L']
print("Enter all characters in a single line with space")
player1=input("Player 1 Input :").split()
addPlayerCharacters(0,grid,player1)
player2=input("Player 2 Input :").split()
addPlayerCharacters(4,grid,player2)
def checkmove(pl,grid,move,ch,pos_i,pos_j):
    temp=grid[pos_i][pos_j]
    grid[pos_i][pos_j]='.'
    if pl=='A':
        if move=="L":
            grid[pos_i][pos_j+1]=temp
        elif move=="R":
            grid[pos_i][pos_j-1]=temp
        elif move=="F":
            print(pos_i,pos_j)
            grid[pos_i+1][pos_j]=temp
            print(pos_i,pos_j)
        else:
            grid[pos_i-1][pos_j]=temp
    else:
        if move=="L":
            grid[pos_i][pos_j-1]=temp
        elif move=="R":
            grid[pos_i][pos_j+1]=temp
        elif move=="F":
            grid[pos_i-1][pos_j]=temp
        else:
            grid[pos_i+1][pos_j]=temp
    printGrid(grid)
def makemove(pl,grid,move,ch,pos_i,pos_j):
    checkmove(pl,grid,move,ch,pos_i,pos_j)
while checkEndGame(grid):
    def checkp1():
        ch,move=input("Player 1 move :").split(":")
        k=0
        if ch not in player1:
            print("Character does not exist. Try again!!")
            k+=1
            check(p1)
        if move not in moves:
            print("Invalid move. Try Again!!")
            k+=1
            checkp1()
        i,j=getChar(grid,ch,'A')
        if True:
            if move=="L":
                if j+1>4:
                    print("No left moves for the character. Try Again!!")
                    k+=1
                    checkp1()
                if grid[i][j+1][0]=='A':
                    print("Invalid move!!! Can't kill friend")
                    checkp1()
            elif move=="R":
                if j-1<0:
                    print("No right moves for the character. Try Again!!")
                    k+=1
                    checkp1()
                if grid[i][j-1][0]=='A':
                    print("Invalid move!!! Can't kill friend")
                    checkp1()
            elif move=="F":
                if i+1>4:
                    print("No forward moves for the character. Try Again!!")
                    k+=1
                    checkp1()
                if grid[i+1][j][0]=='A':
                    print(i,j)
                    print("Invalid move!!! Can't kill friend")
                    k+=1
                    checkp1()
            else:
                if i-1<0:
                    print("No backward moves for the character. Try Again!!")
                    k+=1
                    checkp1()
                if grid[i-1][j][0]=='A':
                    print("Invalid move!!! Can't kill friend")
                    k+=1
                    checkp1()
        if k==0:
            return ch,move,i,j
            
                    
    ch1,move1,i,j=checkp1()
    makemove('A',grid,move1,ch1,i,j)
    def checkp2():
        ch,move=input("Player 2 move :").split(":")
        k=0
        if ch not in player1:
            print("Character does not exist. Try again!!")
            checkp2()
        if move not in moves:
            print("Invalid move. Try Again!!")
            checkp2()
        i,j=getChar(grid,ch,'B')
        if True:
            if move=="L":
                if j-1<0:
                  print("No left moves for the character. Try Again!!")
                  checkp2()
                if grid[i][j-1][0]=='B':
                  print("Invalid move!!! Can't kill friend")
                  checkp2()
            elif move=="R":
                if j+1>4:
                    print("No right moves for the character. Try Again!!")
                    checkp2()
                if grid[i][j+1][0]=='B':
                    print("Invalid move!!! Can't kill friend")
                    checkp2()
            elif move=="F":
                if i-1<0:
                    print("No forward moves for the character. Try Again!!")
                    checkp2()
                if grid[i-1][j][0]=='B':
                    print("Invalid move!!! Can't kill friend")
                    checkp2()
            else:
                if i+1>4:
                    print("No backward moves for the character. Try Again!!")
                    checkp1()
                if grid[i+1][j][0]=='B':
                    print("Invalid move!!! Can't kill friend")
                    checkp2()
        return ch,move,i,j
    ch2,move2,i,j=checkp2()
    makemove('B',grid,move2,ch2,i,j)