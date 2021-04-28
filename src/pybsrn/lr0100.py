from .validators import LR0100Vector
from calendar import monthrange


class LR0100:

    global2_avg = LR0100Vector()
    global2_std = LR0100Vector()
    global2_min = LR0100Vector()
    global2_max = LR0100Vector()
    direct_avg = LR0100Vector()
    direct_std = LR0100Vector()
    direct_min = LR0100Vector()
    direct_max = LR0100Vector()
    diffuse_avg = LR0100Vector()
    diffuse_std = LR0100Vector()
    diffuse_min = LR0100Vector()
    diffuse_max = LR0100Vector()
    downward_avg = LR0100Vector()
    downward_std = LR0100Vector()
    downward_min = LR0100Vector()
    downward_max = LR0100Vector()
    temperature = LR0100Vector()
    humidity = LR0100Vector()
    pressure = LR0100Vector()

    def __init__(self, year: int, month: int):
        self._year = year
        self._month = month
        self._n = monthrange(year, month)[1] * 1440

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if value is not None:
            if not isinstance(value, LR0100):
                raise TypeError(f'Expected {value!r} to be a LR0100 object')
        self.value = value

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def n(self):
        return self._n

