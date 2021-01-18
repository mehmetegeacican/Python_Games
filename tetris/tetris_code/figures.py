import random

class Figure:
    colors = [
        (0, 0, 0),
        (120, 37, 179),
        (100, 179, 179),
        (80, 34, 22),
        (80, 134, 22),
        (180, 34, 22),
        (180, 34, 122),
    ]
    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],#I
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],#L
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],#L 
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],#T
        [[1, 2, 5, 6]],#RECT
        [[1, 2, 6, 7],[2, 6, 5, 9], [4, 5, 1, 2],[0, 4, 5, 9]], #Z
        [[5, 6, 2 ,3],[9, 5, 6, 2],[ 6, 5, 1, 0],[1,5,6,10]]
    ]
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(self.colors) - 1)
        self.rotation = 0
        
    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])