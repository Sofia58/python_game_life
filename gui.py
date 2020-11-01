import main
import pygame


class GUI():
    def __init__(self, field) -> None:
        self.field = field

    def field(self, i, j):
        field = pygame.display.set_mode((10, 10))

    def draw_line(self, screen, colour, point_1, point_2):
        colour = (0, 0, 0)
        point_1 = (1, 1)
        point_2 = (1, 10)
        pygame.draw.line(screen, colour, point_1, point_2)

    def paint_cell(self):
        pass
    def screen_update(self):
        pass





if __name__ == '__main__':
    gui= GUI(main.Field())

