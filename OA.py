# Assignment 2 written by - Praneeth Rayasam  # UCID- phr2

def find_solutions(Q):
    global board_count
    if len(Q) == 8:
        print_board(Q)
        board_count += 1
        return

    for i in range(0,8):
        if safe(Q,i):
            # If the column in safe to palce the queen, append it to the list  Q
            Q.append(i)

            #Recursive call to check other rows
            find_solutions(Q)

            # Removing the last queen off the list
            Q.pop()


def print_board(Q):
    #Creates a 8*8 Chess Board which prints Q at the safe position and a '-' when it's not
    for i in range(0,8):
        for j in range(0,8):
            if Q[i] == j:
                print(' Q ', end = ' ')
            else:
                print(' - ', end = ' ')
        print("\n")
    print('Chessboard version : ' + str(board_count))
    print("\n")


def safe(Q,c):
    Q_length = len(Q)
    for i in range(Q_length):
        #Check the column
        if Q[i] == c:
            return False
        #Check the row
        if Q[i] - i == c - Q_length:
            return False
        #Check the diagonal
        if Q[i] + i == c + Q_length:
            return False
    return True

#The below function call prints all the solutions of the 8 queens problem
board_count = 1
Q = []
find_solutions(Q)
# We find out that there are 92 chessboards with this type

#Using print_board function
QueenPositions = [7,3,0,2,5,1,6,4]
print_board(QueenPositions)

#Using safe function to tell if the column is safe to place a queen
QueenIsSafe = [7, 3, 0]
print(safe(QueenIsSafe, 2))
print(safe(QueenIsSafe, 6))