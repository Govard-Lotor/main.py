import pygame
pygame.init()
fps = 60
FPS = 0
clock = pygame.time.Clock()

black = (0, 0, 0)
green = (53, 161, 31)


class Main_menu:
    def __int__(self):
        pass

    def on_menu(self, screen):
        self.width = screen.get_width()
        self.height = screen.get_height()

        self.field = pygame.Surface((self.width, self.height))
        self.field.fill(black)

        button_one = [self.width // 10, self.height // 10, ]


