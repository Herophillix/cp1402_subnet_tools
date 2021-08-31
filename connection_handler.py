"""

"""
from connection import Connection


class ConnectionHandler:
    """ """

    def __init__(self, lines: [str]):
        """Constructor"""
        self.connections = []

        for line in lines:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                name = ""
                host_count = 0
                for i, part in enumerate(parts):
                    if i == len(parts) - 1:
                        host_count = int(part) if part.isdigit() else 0
                    else:
                        name = name + part + (',' if i != len(parts) - 2 else "")
                if host_count != 0:
                    self.connections.append(Connection(name, host_count))

        self.connections = sorted(self.connections, key=lambda connection: connection.host_count, reverse=True)

    def __str__(self):
        """Description of the class"""
        to_return = ""
        for connection in self.connections:
            to_return = to_return + str(connection) + "\n"
        return to_return

    def host_total(self):
        return sum(connection.host_count for connection in self.connections)
