from .validators import ValidatorVector
from calendar import monthrange


class ValidatorLR0100:

    value = None

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if value is not None:
            if not isinstance(value, LR0100):
                raise TypeError(f'Expected {value!r} to be LR0100 object')
        self.value = value


class LR0100:

    global2_avg = ValidatorVector()
    global2_std = ValidatorVector()
    global2_min = ValidatorVector()
    global2_max = ValidatorVector()
    direct_avg = ValidatorVector()
    direct_std = ValidatorVector()
    direct_min = ValidatorVector()
    direct_max = ValidatorVector()
    diffuse_avg = ValidatorVector()
    diffuse_std = ValidatorVector()
    diffuse_min = ValidatorVector()
    diffuse_max = ValidatorVector()
    downward_avg = ValidatorVector()
    downward_std = ValidatorVector()
    downward_min = ValidatorVector()
    downward_max = ValidatorVector()
    temperature = ValidatorVector()
    humidity = ValidatorVector()
    pressure = ValidatorVector()
    _n = None

    def __init__(self, year: int = None, month: int = None):
        self._year = year
        self._month = month
        self._n = monthrange(year, month)[1] * 1440

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def n(self):
        return self._n

