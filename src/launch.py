import pygame
from pygame.locals import *

import pygame_menu

from src.labyrinth import Labyrinth
from src.player import Player
from src.generator_DFS import GeneratorDFS
from src.generator_MST import GeneratorMST


def menu_generator(screen):
    # меню выбора настроек генератора лабиринта

    generators_menu = [("DFS", 0), ("MST", 1)]

    menu = pygame_menu.Menu(title="Labyrinth", width=screen.get_width(), height=screen.get_height(),
                            theme=pygame_menu.themes.THEME_DARK)
    menu.add.dropselect(title="Algorithm", items=generators_menu,
                        dropselect_id="algorithm", default=0)
    menu.add.text_input(title="Height: ", default="30", textinput_id="height")
    menu.add.text_input(title="Width: ", default="50", textinput_id="width")
    menu.add.button(title="Play", action=lambda: menu.disable(),
                    font_color=(255, 255, 255), background_color=(100, 100, 100))
    menu.mainloop(screen)

    generator_width = int(menu.get_input_data().get("width"))
    generator_height = int(menu.get_input_data().get("height"))

    if menu.get_input_data().get("algorithm")[0][1] == 0:
        generator = GeneratorDFS(generator_width, generator_height)
    else:
        generator = GeneratorMST(generator_width, generator_height)

    return generator


def launch():
    pygame.init()
    width, height = 900, 700
    screen = pygame.display.set_mode((width, height))
    surface = pygame.Surface((width, height))

    generator = menu_generator(screen)
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
            elif event.type == KEYDOWN and event.key == K_SPACE:  # при нажатии SPACE отображается путь
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
