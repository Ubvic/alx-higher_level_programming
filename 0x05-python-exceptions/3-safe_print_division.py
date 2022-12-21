#!/usr/bin/python3

def safe_print_division(a, b):
    """Function returns the division of a by b"""
    try:
        divide = a / b
    except (TypeError, ZeroDivisionError):
        divide = None
    finally:
        print("Inside result: {}".format(divide))
    return (divide)
