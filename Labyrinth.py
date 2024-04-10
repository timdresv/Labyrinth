import pygame


class Labyrinth(pygame.sprite.Sprite):
    def __init__(self, generator):
        pygame.sprite.Sprite.__init__(self)
        self.generator = generator

    def draw_labyrinth(self, screen, scale, offset_x, offset_y):
        walls_width = 2  # width of walls
        pygame.draw.line(screen, (0, 0, 0), (offset_x, offset_y),
                         (offset_x + self.generator.width * scale, offset_y), width=walls_width)
        pygame.draw.line(screen, (0, 0, 0), (offset_x, offset_y + self.generator.height * scale),
                         (offset_x + self.generator.width * scale, offset_y + self.generator.height * scale),
                         width=walls_width)
        pygame.draw.line(screen, (0, 0, 0), (offset_x, offset_y),
                         (offset_x, offset_y + self.generator.begin_y * scale), width=walls_width)
        pygame.draw.line(screen, (0, 0, 0), (offset_x, offset_y + (self.generator.begin_y + 1) * scale),
                         (offset_x, offset_y + self.generator.height * scale), width=walls_width)
        pygame.draw.line(screen, (0, 0, 0), (offset_x + self.generator.width * scale, offset_y),
                         (offset_x + self.generator.width * scale, offset_y + self.generator.end_y * scale),
                         width=walls_width)
        pygame.draw.line(screen, (0, 0, 0),
                         (offset_x + self.generator.width * scale, offset_y + (self.generator.end_y + 1) * scale),
                         (offset_x + self.generator.width * scale, offset_y + self.generator.height * scale),
                         width=walls_width)
        for x in range(len(self.generator.matrix)):
            for y in range(len(self.generator.matrix[x])):
                if self.generator.matrix[x][y][0]:
                    pygame.draw.line(screen, (0, 0, 0), (offset_x + x * scale, offset_y + y * scale),
                                     (offset_x + (x + 1) * scale, offset_y + y * scale), width=walls_width)
                if self.generator.matrix[x][y][1]:
                    pygame.draw.line(screen, (0, 0, 0), (offset_x + (x + 1) * scale, offset_y + y * scale),
                                     (offset_x + (x + 1) * scale, offset_y + (y + 1) * scale), width=walls_width)
                if self.generator.matrix[x][y][2]:
                    pygame.draw.line(screen, (0, 0, 0), (offset_x + x * scale, offset_y + y * scale),
                                     (offset_x + x * scale, offset_y + (y + 1) * scale), width=walls_width)
                if self.generator.matrix[x][y][3]:
                    pygame.draw.line(screen, (0, 0, 0), (offset_x + x * scale, offset_y + (y + 1) * scale),
                                     (offset_x + (x + 1) * scale, offset_y + (y + 1) * scale), width=walls_width)

    def draw_track(self, screen, scale, offset_x, offset_y):
        for (num, (x, y)) in enumerate(self.generator.track):
            pygame.draw.rect(screen, (255, 255 * num / len(self.generator.track), 0),
                             (offset_x + x * scale, offset_y + y * scale, scale + 1, scale + 1))

    def draw(self, screen, scale, offset_x, offset_y):
        screen.fill((255, 255, 255))

        if self.generator.track:
            self.draw_track(screen, scale, offset_x, offset_y)

        self.draw_labyrinth(screen, scale, offset_x, offset_y)
