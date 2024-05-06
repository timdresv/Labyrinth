import pygame


class Player(pygame.sprite.Sprite):
    # Класс реализует перемещение игрока по лабиринту

    def __init__(self, screen, scale, offset_x, offset_y, begin_x, begin_y):
        pygame.sprite.Sprite.__init__(self)

        self.x = begin_x
        self.y = begin_y

        self.screen = screen

        self.scale = scale
        self.offset_x, self.offset_y = offset_x, offset_y

        self.player_radius = self.scale / 4
        self.player_offset = self.scale / 2

        self.update()

    def update(self):
        pygame.draw.circle(self.screen, (0, 0, 0), (self.offset_x + self.x * self.scale + self.player_offset,
                                                    self.offset_y + self.y * self.scale + self.player_offset),
                           self.player_radius)

    def up(self):
        self.y = self.y - 1

    def down(self):
        self.y = self.y + 1

    def left(self):
        self.x = self.x - 1

    def right(self):
        self.x = self.x + 1
