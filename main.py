import pygame
from pygame.locals import *

import pygame_menu

from GeneratorDFS import GeneratorDFS
from GeneratorMST import GeneratorMST
from Labyrinth import Labyrinth
from Player import Player


def main():
    generators = [("DFS", GeneratorDFS(50, 30)), ("MST", GeneratorMST(50, 30))]

    pygame.init()
    width, height = 900, 700
    screen = pygame.display.set_mode((width, height))
    surface = pygame.Surface((width, height))

    menu = pygame_menu.Menu(title="Labyrinth", width=width, height=height)
    menu.add.dropselect(title="Algorithm", items=generators,
                        dropselect_id="algorithm", default=0).set_background_color((100, 100, 100))
    menu.add.button(title="Play", action=lambda: menu.disable(),
                    font_color=(255, 255, 255), background_color=(100, 100, 100))
    menu.mainloop(screen)

    generator = menu.get_input_data().get("algorithm")[0][1]
    generator.generate()

    padding = 50
    scale = min((height - padding * 2) / generator.height, (width - padding * 2) / generator.width)
    offset_x, offset_y = ((width - generator.width * scale) / 2, (height - generator.height * scale) / 2)

    labyrinth = Labyrinth(generator)
    labyrinth.draw(surface, scale, offset_x, offset_y)

    player = Player(screen, scale, offset_x, offset_y, generator.begin_x, generator.begin_y)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN and event.key == K_SPACE:
                generator.find_track()
                labyrinth.draw(surface, scale, offset_x, offset_y)
            elif event.type == KEYDOWN and event.key == K_UP and generator.matrix[player.x][player.y][0] == 0:
                player.up()
            elif event.type == KEYDOWN and event.key == K_RIGHT and generator.matrix[player.x][player.y][1] == 0:
                player.right()
            elif event.type == KEYDOWN and event.key == K_LEFT and generator.matrix[player.x][player.y][2] == 0:
                player.left()
            elif event.type == KEYDOWN and event.key == K_DOWN and generator.matrix[player.x][player.y][3] == 0:
                player.down()
        screen.blit(surface, (0, 0))
        player.update()
        pygame.display.update()

        clock.tick(60)


if __name__ == '__main__':
    main()
