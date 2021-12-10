"""
References:
    https://adventofcode.com/2015/day/10#part2
"""
from itertools import groupby


def main():
    start: str = "3113322113"
    for _ in range(50):
        start = "".join(str(len([*group])) + key for key, group in groupby(start))

    print(len(start))


if __name__ == "__main__":
    main()