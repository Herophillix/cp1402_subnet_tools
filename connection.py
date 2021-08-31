"""

"""


class Connection:
    """ """

    def __init__(self, name: str, host_count: int):
        """Constructor"""
        self.name = name
        self.host_count = host_count if host_count > 0 else 0
        self.closest_bit_power = 1 if host_count == 0 else 1 << (host_count-1).bit_length()

    def __str__(self):
        """Description of the class"""
        return "{0} - {1} hosts".format(self.name, self.host_count)
