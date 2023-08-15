from random import randrange

class Input:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class BoardsError(Exception):
    pass


class BoardOutAre(BoardsError):
    def __str__(self):
        return "Dont shut at the out of board"

class BoardAgainShhot(BoardsError):
    def __str__(self):
        return "Try again, don't repeat"

class Ship:
    def __init__(self, ):
