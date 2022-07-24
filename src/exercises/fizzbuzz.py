#!/usr/bin/python3

import argparse

from utils.parse_args import parse_vars


def get_fizzbuzz(num, mod_list):
    print_string = ""

    for mod in mod_list:
        if num % mod == 0:
            print_string += mod_list[mod]

    if print_string == "":
        return num
    return print_string


def fizzbuzz(length, mod_list):

    for i in range(1, int(length)+1):
        print(get_fizzbuzz(i, mod_list))


def main():
    mod_list = {3: "Three", 5: 'Five'}
    length = 100
    parser = argparse.ArgumentParser(description="...")

    parser.add_argument('-l', "--length", type=int)
    parser.add_argument('-m', "--mod",
                        metavar="KEY=VALUE",
                        nargs='+')
    args = parser.parse_args()

    if args.mod is not None:
        mod_list = parse_vars(args.mod)
    if args.length is not None:
        length = args.length

    fizzbuzz(length, mod_list)


if __name__ == "__main__":
    main()
