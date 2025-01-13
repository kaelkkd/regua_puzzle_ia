from random import shuffle

class Regua:
    def __init__(self, size: int):
        self.size = size
        self.ruler = self.initializeRuler(size)

    def initializeRuler(self, size: int) -> list:
        ruler = ["-"]
        for _ in range((size-1) // 2):
            ruler.append("A")
            ruler.append("B")
        shuffle(ruler)

        return ruler
