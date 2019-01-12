class BoolWrapper:
    """
    Wraps bool object into mutable, non-singleton class.
    """
    def __init__(self, value):
        """
        Initializes object with given bool value.
        :param value: bool value (or value which could be converted to bool) used for initialization
        :type value: bool
        """
        self._value = bool(value)

    def set(self, value):
        self._value = bool(value)

    # def get(self):
        # TODO: implement this if someone would like to operate on real bool object

    def __repr__(self):
        return repr(self._value)

    def __bool__(self):
        return self._value

    def __eq__(self, other):
        return self._value == other

    def __ne__(self, other):
        return self._value != other
