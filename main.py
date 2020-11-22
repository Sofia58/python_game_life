import random
import time
from pprint import pprint as pp
import pygame


class Cell:
    next_alive = None

    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive

    def __repr__(self):
        if self.alive:
            return "*"
        else:
            return " "

    def calculate_state(self, neighbours):
        alive_neighbours = 0
        for n in neighbours:
            if n.alive:
                alive_neighbours += 1
        if self.alive:
            if alive_neighbours in (2, 3):
                self.next_alive = True
            else:
                self.next_alive = False
        else:
            if alive_neighbours == 3:
                self.next_alive = True
            else:
                self.next_alive = False

    def next_step(self):
        self.alive = self.next_alive


class Field:

    def __init__(self, width=10, height=10, fill_percent=10, randomize=False):
        self.width = width
        self.height = height
        self.fill_percent = fill_percent
        self.cells = []

        if randomize:
            self.randomize_field()

    def previous_step(self, j):
        res = []
        zero =[]
        for j in range(self.width):
            bin_2(j)
        return j
        #while True:
            #zero.append(0)
            #if len(res) < 5:
             #   zero.extend(res)
        #return j

    def randomize_field(self):
        for i in range(self.height):
            self.cells.append([])
            for j in range(self.width):
                alive = False
                if random.randrange(0, 100) < self.fill_percent:
                    alive = True
                self.cells[i].append(Cell(j, i, alive))


    def field_update(self, field):
        for i in range(self.height):
            for j in range(self.width):
                neighbours = [field[(i - 1) % self.height][(j) % self.width],
                              field[(i + 1) % self.height][(j) % self.width],
                              field[(i) % self.height][(j - 1) % self.width],
                              field[(i) % self.height][(j + 1) % self.width],
                              field[(i - 1) % self.height][(j - 1) % self.width],
                              field[(i + 1) % self.height][(j + 1) % self.width],
                              field[(i - 1) % self.height][(j + 1) % self.width],
                              field[(i + 1) % self.height][(j - 1) % self.width]]
                field[i][j].calculate_state(neighbours)
        for i in range(self.height):
            for j in range(self.width):
                field[i][j].next_step()

    def next(self):
        return self.field_update(self.cells)


def bin_2(n):
    res = []
    while n > 0:
        o = n % 2
        res.append(o == 1)
        n = n // 2
    return res


if __name__ == '__main__':
    field = Field(5, 5, randomize=True)
    while True:
       step = field.previous_step(6)
       pp(step)
       #field.field_update(step)
    #     time.sleep(1)
