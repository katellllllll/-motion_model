import numpy as np
from os import system

class Field:
    def __init__(self, x, y):
        self.arr = np.zeros((10, 15))
        self.arr[x, y] = 1

    def Update(self):
        for i in range(self.arr.shape[0]):
            for j in range(self.arr.shape[1]):
                print(round(self.arr[i, j], None), end = '')
            print('')

    def Move(self, curX, curY, direction):
        if direction == 'w':
            self.arr[curY, curX] = 0
            self.arr[curY - 1, curX] = 1
        if direction == 's':
            self.arr[curY, curX] = 0
            self.arr[curY + 1, curX] = 1
        if direction == 'a':
            self.arr[curY, curX] = 0
            self.arr[curY, curX - 1] = 1
        if direction == 'd':
            self.arr[curY, curX] = 0
            self.arr[curY, curX + 1] = 1

class Character:
    def __init__(self, y_arr, x_arr):
        self.x = x_arr
        self.y = y_arr
        self.field = Field(self.y, self.x)

    def Move(self, dc):
        if (self.y == 0 and dc == 'w') or (self.x == 0 and dc == 'a'):
            return
        if (self.y == self.field.arr.shape[0] - 1 and dc == 's') or (self.x == self.field.arr.shape[1] - 1 and dc == 'd'):
            return
        self.field.Move(self.x, self.y, dc)
        if dc == 'w':
            self.y -= 1
        if dc == 's':
            self.y += 1
        if dc == 'a':
            self.x -= 1
        if dc == 'd':
            self.x += 1

    def ShowField(self):
        self.field.Update()

person = Character(0, 0)

while (True):
    person.ShowField()
    print("Direction (WASD): ", end='')
    direction = input()
    person.Move(direction)
    system('cls')