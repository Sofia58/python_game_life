import main
import pygame


class GUI():
    def __init__(self, field: main.Field, wait_ms=1000, screen_width=500, screen_height=500) -> None:
        self.field = field
        self.cell_size_x = screen_width / field.width
        self.cell_size_y = screen_height / field.height
        self.size = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.wait_ms = wait_ms

    def paint_cell(self, cell: main.Cell):
        x = cell.x * self.cell_size_x
        y = cell.y * self.cell_size_y
        rect = (x, y, self.cell_size_x - 1, self.cell_size_y - 1)
        pygame.draw.rect(self.screen, pygame.Color('green' if cell.alive else 'black'), rect)

    def draw(self):
        for row in self.field.cells:
            for c in row:
                self.paint_cell(c)
            pygame.display.flip()

    def wait(self):
        self.clock.tick(int(1000 / self.wait_ms))


if __name__ == '__main__':
    gui = GUI(main.Field(width=100, height=100, fill_percent=15, randomize=True), wait_ms=200, screen_width=500,
              screen_height=500)

    while True:
        gui.field.next()
        gui.draw()
        gui.wait()
