import random
import time
from pprint import pprint as pp
import numpy as np
import os

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

    def __eq__(self, other):
        return isinstance(other, Cell) and self.alive == other.alive

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

    def decode(self, n):
        return self._add_zeros(bin_2(n))

    def previous_step(self):
        res = []
        for n in range(pow(2, self.width * self.height)):
            if n % 10000 == 0:
                print(n)
            decoded = self.decode(n)
            #if decoded[9:12] == [True, True, True] and decoded[:8] == [False] * 8:
                #pp(decoded)
            fld = self.prefill_field(decoded)
            self.field_update(fld)
            if fld == self.cells:
                res.append(n)
                # if len(res) == 2:
                #     return res
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
    return list(reversed(res))


if __name__ == '__main__':
    # cells = [False, False, False, False, False,
    #          False, False, True,  False, False,
    #          False, True,  True,  True, False,
    #          False, False, True,  False, False,
    #          False, False, False, False, False]
    cells = [
        False, False, False, False,
        False, False, True, False,
        False, False, True, False,
        False, False, True, False,
    ]

    # cells = [
    #   True,  True,  True, False,
    #   True,  True,  True, False,
    #   True, False, False, False,
    #   True, False, False,  True,
    # ]

    field = Field(4, 4, cells=cells)
    for lst in field.cells:
        pp(lst)
    while True:
        command = input('n or p')
        print(command)
        if command == 'p':
            steps = field.previous_step()
            print(steps)
            #pp(steps)
            for n in steps:
                res = np.array(field.decode(n))
                res = res.reshape(4, 4)
                print(res)
                print(os.linesep)
                print('-------------------------------------')
            exit(0)
        elif command == 'n':
            field.next()
            for lst in field.cells:
                pp(lst)
        # field.field_update(step)
        # time.sleep(1)
