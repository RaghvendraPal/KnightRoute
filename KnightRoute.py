from StackLinkList import StackLinkList 
route = 0
stack = StackLinkList()

def isValidIndex(newX, newY, x, y):
    if newX < 0 or newY < 0 or newX >= N or newY >= N:
        return False

    return True

def printRoute():
    print("*"*5+"Route No. :"+str(route)+"*"*10)
    stack_local = StackLinkList()
    while not stack.isEmpty():
        stack_local.push(stack.pop())

    while not stack_local.isEmpty():
        value = stack_local.pop()
        print(value, end =" ")
        stack.push(value)
    print('\n')
    


# A Recursive function is used to Find All the routes for the knight from source to destination index
def knightRoute(data, x, y):
# Making Current Index as Visited
    data[x][y] = 1
    stack.push("("+str(x)+","+str(y)+")")
    
# if Chess Board at end index then print route of the knight
    global route
    if x == x_end and y == y_end and route < 10:
        route += 1
        printRoute()
        # Removing Current Node because we have reached destination
        stack.pop()
        # Making current index to zero so that program can go to other index
        data[x][y] = 0
        return
    
    elif route >= 10:
        return


    # There are only 8 routes for the knight
    for k in range(8):

        # new position of knight on chessboard
        newX = x + row[k]
        newY = y + col[k]
        # if new position is a valid and not visited yet
        if isValidIndex(newX, newY, x, y) and data[newX][newY] == 0 and route < 10:
            knightRoute(data, newX, newY)

    # if node is visited then we need to make current node unvisited
    data[x][y] = 0
    # Removing Current Node because we have reached destination
    stack.pop()


import numpy as np

# chess board type
# Chess Board 8*8
while True:
    N = input("Enter Chess Board Dimention example 2*2, 3*3 :    ").split("*")
    if N[0] != N[1]:
        print("Please Enter Right Dimention both X and Y index should be same")
    else:
        N = int(N[0])
        break
# start position of knight
start_index = input("Start Index example 0 0 :   ").split()
x_index, y_index = int(start_index[0]), int(start_index[1])


# end position of knight
end_index = input("End Index example 2 2 :   ").split()
x_end, y_end = int(end_index[0]), int(end_index[1])

##############################################################################
row = [2, 1, -1, -2, -2, -1,  1,  2]
col = [1, 2,  2,  1, -1, -2, -2, -1]

print("Start Position : ("+str(x_index)+","+str(y_index)+")")
print("End Position : ("+str(x_end)+","+str(y_end)+")")


data = [[0 for i in range(N)] for _ in range(N)]


if x_end > N-1 or x_end < 0 or y_end > N-1 or y_end < 0:
    print("Please give right end position index for a knight it should be between 0 - 8") 
if x_index > N-1 or x_index < 0 or y_index > N-1 or y_index < 0:
    print("Please give right start position index for a knight it should be between 0 - 8") 
else:
    knightRoute(data, x_index, y_index)
    if route == 0:
        print("No path is possible")