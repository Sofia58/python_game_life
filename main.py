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

    def __init__(self, width=10, height=10, fill_percent=10, randomize=False, cells=None):
        self.width = width
        self.height = height
        self.fill_percent = fill_percent
        self.cells = []

        if randomize:
            self.cells = self.prefill_field(self.random_aliveness())
        elif cells:
            self.cells = self.prefill_field(cells)
        else:
            self.cells = self.prefill_field([False for _ in range(self.width * self.height)])

    def previous_step(self, j):
        res = []
        for n in pow(2, self.width * self.height):
            fld = self.prefill_field(self._add_zeros(bin_2(j)))
            self.field_update(fld)
            if fld == self.cells:
                res.append(n)
        return res

    def _add_zeros(self, lst):
        zeros = []
        for i in range(self.height * self.width - len(lst)):
            zeros.append(False)
        zeros.extend(lst)
        return zeros

    def prefill_field(self, aliveness):
        fld = []
        for i in range(self.height):
            fld.append([])
            for j in range(self.width):
                fld[i].append(Cell(j, i, aliveness[i * self.width + j]))
        return fld

    def random_aliveness(self):
        aliveness = []
        for i in range(self.height * self.width):
            if random.randrange(0, 100) < self.fill_percent:
                aliveness.append(True)
            else:
                aliveness.append(False)
        return aliveness

    def make_step(self):
        for i in range(self.height):
            for j in range(self.width):
                pass
                # .next_step()

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
       step = field.previous_step(8)
       pp(step)
       exit(0)
       #field.field_update(step)
       #time.sleep(1)