#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    length = len(argv)
    for i in range(1, length):
        sum = sum + int(argv[i])
    print("{:d}".format(sum))
