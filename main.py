import random
from pprint import pprint as pp


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

    def __init__(self, width=100, height=100, cell_size=5, speed=4, randomize=False):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width * height
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed
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
        pass
if __name__ == '__main__':
    pp(Field(10, 10, randomize=True).cells)
