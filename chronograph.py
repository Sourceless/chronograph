class Chronograph(object):
    '''Wrapper object for time and date operations'''
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __cmp__(self, other):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __xor__(self, other):
        # for abs difference maybe?
        pass

    def __radd__(self, other):
        self.__add__(other)

    def __rsub__(self, other):
        self.__sub__(other)

    def __rmul__(self, other):
        self.__mul__(other)

    def __rmod__(self, other):
        self.__mod__(other)

    def __rxor__(self, other):
        self.__xor__(other)

    @property
    def microseconds(self):
        pass

    @property
    def seconds(self):
        pass

    @property
    def minutes(self):
        pass

    @property
    def hours(self):
        pass

    @property
    def days(self):
        pass

    @property
    def weeks(self):
        pass

    @property
    def months(self):
        pass

    @property
    def years(self):
        pass

    @classmethod
    def now(cls):
        pass
