import csv
import sys

with open(sys.argv[1]) as csvfile:

    header_line = csvfile.readline()

    split_header = header_line.split(',')
    print(len(split_header))

    first_line = csvfile.readline()

    split_first_line = first_line.split(',')
    print(len(split_first_line))
