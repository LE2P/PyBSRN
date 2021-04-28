class ValidatorLR0001:

    value = None

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if value is not None:
            if not isinstance(value, LR0001):
                raise TypeError(f'Expected {value!r} to be LR0100 object')
        self.value = value


class LR0001:

    def __init__(self, year: int, month: int):
        self._year = year
        self._month = month

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

