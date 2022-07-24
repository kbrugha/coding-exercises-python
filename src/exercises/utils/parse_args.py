#!/usr/bin/python3
"""Argument parser"""


def parse_var(string):
    items = string.split('=')
    key = items[0].strip()
    if len(items) > 1:
        value = '='.join(items[1:])
    return (int(key), value)


def parse_vars(items):
    parsed_items = {}

    if items:
        for item in items:
            key, value = parse_var(item)
            parsed_items[key] = value
    return parsed_items
