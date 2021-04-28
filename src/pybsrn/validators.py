

class ValidatorVector:

    value = None

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError(f'Expected {value!r} to be an list')
            if obj.n is not None:
                if len(value) != obj.n:
                    raise TypeError("Vector should be of length " + str(obj.n))
        self.value = value
