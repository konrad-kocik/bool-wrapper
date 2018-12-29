class BoolWrapper:
    """
    Wraps bool object into mutable, non-singleton class.
    """
    def __init__(self, bool_to_wrap):
        """
        Initializes object with given bool value.
        :param bool_to_wrap: bool value (or value which could be converted to bool) used for initialization
        :type bool_to_wrap: bool
        """
        self._wrapped_bool = bool(bool_to_wrap)

    def __repr__(self):
        return repr(self._wrapped_bool)

    def __bool__(self):
        return self._wrapped_bool

    def wrap(self, bool_to_wrap):
        self._wrapped_bool = bool(bool_to_wrap)
