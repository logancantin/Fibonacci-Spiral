# Reading from stdin and assigning it to array data
from sys import stdin
data = stdin.read().split("\n")

# Rectangle class
class Rect(object):

    # Initiating the rectangle with first parameters
    def __init__(self):
        self.top = 0  
        self.bottom = -1
        self.left = 0
        self.right = 1
    
    # Side length generator
    def sideLen(self, side):
        if side == 1:
            return abs(self.top - self.bottom)
        elif side == 2:
            return abs(self.left - self.right)
        elif side == 3:
            return abs(self.top - self.bottom)
        elif side == 0:
            return abs(self.left - self.right)
        else:
            raise Exception("side id out of range: " + str(side))
    
    # Checking if point is inside the rectangle
    def pointCheck(self, x, y):
        if (self.left <= x <= self.right) and (self.bottom <= y <= self.top):
            return True
        else:
            return False

# Main loop
while True:
    try:
        # Cycling through the lines
        for line in data:

            # Setting TargetX and TargetY
            targetX, targetY = [int(x) for x in line.strip("\r").split(" ")]
            
            # Current Fibonacci number
            fib = 1

            # Initiating the rectangle as r
            r = Rect()

            # Looping until answer is found
            while True:
                # If point is inside the rectangle, print fib number and then exit the loop
                if r.pointCheck(targetX, targetY) == True:
                    print(fib)
                    break
                else:
                    # l is set to the side length of the side clockwise of the last one
                    l = r.sideLen(fib % 4)

                    # Increasing the rectangle size
                    if fib % 4 == 1:
                        r.left -= l
                    elif fib % 4 == 2:
                        r.top += l
                    elif fib % 4 == 3:
                        r.right += l
                    elif fib % 4 == 0:
                        r.bottom -= l

                    # Incrementing fib
                    fib += 1
    
    # If at the end of the input, exit
    except:
        exit()