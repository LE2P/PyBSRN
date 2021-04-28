from .lr0100 import LR0100


class BSRN:

    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
        self.lr0100 = LR0100(year, month)

