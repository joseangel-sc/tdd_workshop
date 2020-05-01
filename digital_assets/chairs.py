class CantStandException(Exception):
    pass


class Chair:
    def __init__(self, material: str, legs: int, color: str) -> None:
        self.material = material
        if legs < 3:
            raise CantStandException("I can't stand if I don't have at least 3 legs!")
        self.legs = legs
        self.color = color
