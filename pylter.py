import sys
from pprint import pprint

def strip_list(elements):
    return map(str.strip, elements)

def make_unique(elements):
    return strip_list(set(elements))

def read_input():
    unique = make_unique(sys.stdin)
    sys.stdout.write(','.join(unique))

if __name__ == "__main__":
    read_input()
