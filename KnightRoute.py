def isValidIndex(newX, newY, x, y):
    if newX < 0 or newY < 0 or newX >= N or newY >= N or newX < x:
        return False

    return True


def printRoute(data):
    print("*"*5+"Route No. :"+str(route)+"*"*10)
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                print("("+ str(i) +"," +str(j)+")", end =" ")
    print('\n')


# A Recursive function is used to Find All the routes for the knight from source to destination index
def knightRoute(data, x, y):
# Making Current Index as Visited
    data[x][y] = 1

# if Chess Board at last index then print route of the knight
    if x == (N-1):
        global route
        route += 1
        printRoute(data)
        # Making current index to zero so that program can go to other index
        data[x][y] = 0
        return

        # If index id greater then size of chess board then we need to return
    if x > (N-1):
        return		

    # There are only 8 routes for the knight
    for k in range(8):

        # new position of knight on chessboard
        newX = x + row[k]
        newY = y + col[k]
        # print(newX, newY, x, y)
        # if new position is a valid and not visited yet
        if isValidIndex(newX, newY, x, y) and data[newX][newY] == 0:
            knightRoute(data, newX, newY)

    # if node is visited then we need to make current node unvisited
    data[x][y] = 0


import numpy as np

# chess board type
# Chess Board 8*8
N = 8
# start position of knight
x_index = 1
y_index = 3

##############################################################################
row = [2, 1, -1, -2, -2, -1,  1,  2 , 2]
col = [1, 2,  2,  1, -1, -2, -2, -1, 1]
route = 0

data = [[0 for i in range(N)] for _ in range(N)]


if x_index == N-1:
    print("Knight Already present in Destination Row")
elif x_index > N-1 or x_index < 0 or y_index > N-1 or y_index < 0:
    print("Please give right index for a knight it should be between 0 - 8") 
else:
    knightRoute(data, x_index, y_index)
    if route == 0:
        print("No path is possible")
    else:
        print("*"*50)
        print("There are "+str(route)+" from source to destination for a knight")
        print("*"*50)