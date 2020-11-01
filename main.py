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
    fill_percent = 25
    cells = []

    def __init__(self, width=10, height=10, randomize=False):
        self.width = width
        self.height = height

        if randomize:
            self.randomize_field()

    def randomize_field(self):
        for i in range(self.height):
            self.cells.append([])
            for j in range(self.width):
                alive = False
                if random.randrange(0, 100) < self.fill_percent:
                    alive = True
                self.cells[i].append(Cell(j, i, alive))

    def field_update(self):
        for i in range(self.height):
            for j in range(self.width):
                neighbours = [self.cells[(i - 1) % self.height][(j) % self.width],
                              self.cells[(i + 1) % self.height][(j) % self.width],
                              self.cells[(i) % self.height][(j - 1) % self.width],
                              self.cells[(i) % self.height][(j + 1) % self.width],
                              self.cells[(i - 1) % self.height][(j - 1) % self.width],
                              self.cells[(i + 1) % self.height][(j + 1) % self.width],
                              self.cells[(i - 1) % self.height][(j + 1) % self.width],
                              self.cells[(i + 1) % self.height][(j - 1) % self.width]]
                self.cells[i][j].calculate_state(neighbours)
        for i in range(self.height):
            for j in range(self.width):
                self.cells[i][j].next_step()


if __name__ == '__main__':
    field = Field(10, 10, randomize=True)
    while True:
        pp(field.cells)
        field.field_update()
        time.sleep(1)
