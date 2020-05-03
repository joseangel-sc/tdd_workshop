class CantStandException(Exception):
    pass


class OnlyOnePersonException(Exception):
    pass


class Chair:
    def __init__(self, material: str, legs: int, color: str) -> None:
        self.material = material
        if legs < 3:
            raise CantStandException("I can't stand if I don't have at least 3 legs!")
        self.legs = legs
        self.color = color
        self.capacity = 1

    def set_capacity(self, capacity):
        if self.color == 'blue' and capacity > 1:
            raise OnlyOnePersonException
        self.capacity = capacity
        return True
