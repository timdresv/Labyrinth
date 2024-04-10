class Generator:
    def update(self):
        self.matrix = [[[1] * 4 for y in range(self.height)] for x in range(self.width)]
        # first value - is there a wall on the top
        # second value - is there a wall on the right
        # third value - is there a wall on the left
        # fourth value - is there a wall on the bottom

        self.track = []

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.update()
