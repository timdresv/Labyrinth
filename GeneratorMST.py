import random
import sys

from Generator import Generator

sys.setrecursionlimit(20000)


class GeneratorMST(Generator):
    # Класс генерации лабиринта с помощью алгоритма MST

    def update(self):
        Generator.update(self)

        self.colors = [[0 for y in range(self.height)] for x in range(self.width)]
        # 0 - WHITE color
        # 1 - GRAY color
        # 2 - BLACK color
        self.parent = [[(-1, -1) for y in range(self.height)] for x in range(self.width)]
        # previous cell

    def __init__(self, width: int, height: int):
        Generator.__init__(self, width, height)

    def generate(self):
        self.update()
        self.begin_x, self.begin_y = 0, random.randint(0, self.height - 1)
        self.end_x, self.end_y = self.width - 1, random.randint(0, self.height - 1)

        self.matrix[self.begin_x][self.begin_y][2] = 0
        self.matrix[self.end_x][self.end_y][1] = 0

        self.MST(self.begin_x, self.begin_y)

    def MST(self, bx: int, by: int):
        self.colors[bx][by] = 1
        self.grey_cells = [(bx, by)]

        while self.grey_cells:
            x, y = random.choice(self.grey_cells)
            self.grey_cells.remove((x, y))

            target_cells = list(enumerate([(x, y - 1), (x + 1, y), (x - 1, y), (x, y + 1)]))

            for (wall, (to_x, to_y)) in target_cells:
                if 0 <= to_x < self.width and 0 <= to_y < self.height:
                    if self.colors[to_x][to_y] == 0:
                        self.grey_cells.append((to_x, to_y))
                        self.colors[to_x][to_y] = 1
                        self.parent[to_x][to_y] = (x, y)
                    elif self.parent[x][y] == (to_x, to_y):
                        self.matrix[x][y][wall] = 0
                        self.matrix[to_x][to_y][3 - wall] = 0

    def find_track(self):
        x, y = (self.end_x, self.end_y)

        self.track = [(x, y)]
        while self.parent[x][y] != (-1, -1):
            x, y = self.parent[x][y]
            self.track.append((x, y))
