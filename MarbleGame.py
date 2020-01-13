print("---------------------------------------------------------------------------")
print("---------0's are marbles,1's are free space and 8's are forbiden-----------")
print("--to play you have to spacify row and col of marble you want to play with--")
print("----then choose the move form list of available moves by typing its no.----")
print("---------------------------------------------------------------------------")

m=0
e=1
f=8

Gbrd = [[f,f,m,m,m,f,f],
        [f,f,m,m,m,f,f],
        [m,m,m,m,m,m,m],
        [m,m,m,e,m,m,m],
        [m,m,m,m,m,m,m],
        [f,f,m,m,m,f,f],
        [f,f,m,m,m,f,f]]
movelst=[]
poslst=[]

def Gbrdnow():
    for row in Gbrd:
        print(row)

def user():
    i=int(input('row:-'))-1
    j=int(input('col:-'))-1
    return (i,j)

def canMove(i,j):

    if Gbrd[i][j]==m:
        if (i==0 or i==1):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                return True
            elif  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                return True
            elif  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                return True
            else:
                return False

        elif (j==0 or j==1):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                return True
            elif Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                return True
            elif  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                return True
            else:
                return False

        elif (i==5 or i==6):
            if Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                return True
            elif  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                return True
            elif  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                return True
            else:
                return False

        elif (j==5 or j==6):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                return True
            elif Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                return True
            elif  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                return True
            else:
                return False
        else:
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                return True
            elif  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                return True
            elif Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                return True
            elif  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                return True
            else:
                return False
    else:
        return False

def addmoves(i,j):
    global movelst,poslst
    if canMove(i,j):
        if (i==0 or i==1):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                movelst.append((i+2,j))
                poslst.append((i+3,j+1))
            if  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                movelst.append((i,j+2))
                poslst.append((i+1,j+3))
            if  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                movelst.append((i,j-2))
                poslst.append((i+1,j-1))

        elif (j==0 or j==1):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                movelst.append((i+2,j))
                poslst.append((i+3,j+1))
            if  Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                movelst.append((i-2,j))
                poslst.append((i-1,j+1))
            if  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                movelst.append((i,j+2))
                poslst.append((i+1,j+3))

        elif (i==5 or i==6):
            if Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                movelst.append((i-2,j))
                poslst.append((i-1,j+1))
            if  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                movelst.append((i,j+2))
                poslst.append((i+1,j+3))
            if  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                movelst.append((i,j-2))
                poslst.append((i+1,j-1))

        elif (j==5 or j==6):
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                movelst.append((i+2,j))
                poslst.append((i+3,j+1))
            if  Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                movelst.append((i-2,j))
                poslst.append((i-1,j+1))
            if  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                movelst.append((i,j-2))
                poslst.append((i+1,j-1))


        else:
            if Gbrd[i+2][j]==e and Gbrd[i+1][j]==m:
                movelst.append((i+2,j))
                poslst.append((i+3,j+1))
            if  Gbrd[i][j+2]==e and Gbrd[i][j+1]==m:
                movelst.append((i,j+2))
                poslst.append((i+1,j+3))
            if Gbrd[i-2][j]==e and Gbrd[i-1][j]==m:
                movelst.append((i-2,j))
                poslst.append((i-1,j+1))
            if  Gbrd[i][j-2]==e and Gbrd[i][j-1]==m:
                movelst.append((i,j-2))
                poslst.append((i+1,j-1))

def move(mrbx,mrby):
    global movelst,poslst
    if len(poslst)==1:
        (mvx,mvy)=movelst[0]
    else:
        print(poslst)
        moveidx=int(input('choose your move no.:-'))-1
        (mvx,mvy)=movelst[moveidx]
    Gbrd[mrbx][mrby]=e
    Gbrd[mvx][mvy]=m
    if mrbx==mvx:
        if mvy > mrby:
            Gbrd[mrbx][mrby+1]=e
        else:
            Gbrd[mrbx][mrby-1]=e
    elif mrby==mvy:
        if mvx > mrbx:
            Gbrd[mrbx+1][mrby]=e
        else:
            Gbrd[mrbx-1][mrby]=e
    print("----------------------------")

def count():
    count=0
    for row in Gbrd:
        for place in row:
            if place == m:
                count+=1
    return count

def status():

    stat="end"
    for i in range(0,7):
        for j in range(0,7):
            if canMove(i,j):
                stat="run"
    if stat=="run":
        return True
    else:
        return False

while status():

    movelst=[]
    poslst=[]

    Gbrdnow()
    (mrbx,mrby)=user()
    if canMove(mrbx,mrby):
        addmoves(mrbx,mrby)
        move(mrbx,mrby)

    else:
        print("---CAN NOT MOVE THAT---")

Gbrdnow()
print("----------------------------")
print("---No more moves possible---")
print("Number of marbles left:-",count())
