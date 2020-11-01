import main
import pygame


class GUI():
    def __init__(self, field: main.Field, cell_size=20) -> None:
        self.field = field
        self.cell_size = cell_size
        self.size = (field.width * cell_size, field.height * cell_size)
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

    def draw_line(self, screen, colour, point_1, point_2):
        colour = (0, 0, 0)
        point_1 = (1, 1)
        point_2 = (1, 10)
        while True:
            for n in range(self.screen, 50):
                    pygame.draw.line(screen, colour, point_1, point_2)

    def paint_cell(self, cell: main.Cell):
        x = cell.x * self.cell_size
        y = cell.y * self.cell_size
        rect = (x, y, self.cell_size - 1, self.cell_size - 1)
        print(rect)
        pygame.draw.rect(self.screen, pygame.Color('red'), rect)

    def draw(self):
        for row in self.field.cells:
            for c in row:
                self.paint_cell(c)
        pygame.display.flip()

    def wait(self):
        self.clock.tick(1)

    def screen_update(self):
        pass

    def speed(self):
        pass






if __name__ == '__main__':
    gui= GUI(main.Field(randomize=True))

    while True:
        gui.draw()
        gui.wait()