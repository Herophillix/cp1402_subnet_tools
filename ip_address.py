"""

"""
BYTE_LENGTH = 8


class IPAddress:
    """ """

    def __init__(self, address: str):
        """Constructor"""
        self.ip_bytes = [0, 0, 0, 0]
        self.subnet_mask = 0

        parts = address.strip().replace('/', '.').split('.')
        if len(parts) != len(self.ip_bytes) + 1:
            return

        # Subnet Mask
        subnet_mask = parts.pop(-1)
        if subnet_mask.isdigit():
            subnet_mask = int(subnet_mask)
            if 0 <= subnet_mask <= len(self.ip_bytes) * BYTE_LENGTH:
                self.subnet_mask = subnet_mask

        # Bytes
        for i, part in enumerate(parts):
            if part.isdigit():
                part = int(part)
                if 0 <= part <= 2 ** BYTE_LENGTH - 1:
                    self.ip_bytes[i] = part

    def __str__(self):
        """Description of the class"""
        to_return = ""
        for i, ip_byte in enumerate(self.ip_bytes):
            to_return = to_return + str(ip_byte) + ('.' if i != len(self.ip_bytes) - 1 else '/')
        to_return = to_return + str(self.subnet_mask)
        return to_return

    def available_address(self):
        return 2 ** (len(self.ip_bytes) * BYTE_LENGTH - self.subnet_mask)
