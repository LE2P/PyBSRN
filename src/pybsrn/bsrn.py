from .lr0001 import ValidatorLR0001, LR0001
from .lr0100 import ValidatorLR0100, LR0100


class BSRN:

    lr0001 = ValidatorLR0001()
    lr0100 = ValidatorLR0100()

    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
        self.lr0001 = LR0001(year, month)
        self.lr0100 = LR0100(year, month)
