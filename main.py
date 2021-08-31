"""

"""
from ip_address import IPAddress
from connection_handler import ConnectionHandler


FILE_DIRECTORY = "input/file.txt"


def main():
    """"""
    file = open(FILE_DIRECTORY, 'r')
    lines = file.readlines()
    file.close()

    if len(lines) < 2:
        print("Invalid file")
        return

    ip_address = IPAddress(lines.pop(0))

    connection_handler = ConnectionHandler(lines)

    host_total = connection_handler.host_total()
    available_address = ip_address.available_address()
    if host_total > available_address:
        print("Total number of hosts({0}) is greater than the available addresses({1})".format(host_total,
                                                                                               available_address))


if __name__ == "__main__":
    main()
