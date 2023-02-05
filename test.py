import math


class Board :
    q = None
    count = 0
    def __init__(self) :
        self.q = [0] * (8)
    def findSolutions(self, n) :
        if (n == 8) :
            self.printSolutions()
            self.count += 1
            print(self.count)
            print()
            print()
        else :
            self.q[n] = 0
            while (self.q[n] < 8) :
                if (self.isSafe(n)) :
                    self.findSolutions(n + 1)
            self.q[n] += 1
    def  isSafe(self, n) :
        i = 0
    while (i < n) :
        if (self.q[i] == self.q[n]) :
            return False
        if (n - i == abs(self.q[n] - self.q[i])) :
            return False
        i += 1
    return True
    def printSolutions(self) :
        row = 0
    while (row < 8) :
        col = 0
        while (col < 8) :
            if (self.q[row] == col) :
                print("Q", end ="")
            else :
                print("-", end ="")
        col += 1
        print()
        row += 1
    @staticmethod
    def main( arg) :
        b = Board()
    b.findSolutions(0)


if __name__=="__main__":
    Board.main([])
