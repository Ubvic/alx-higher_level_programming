#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    something = list(my_list)
    if idx < 0 or idx >= len(my_list):
        return something
    else:
        something[idx] = element
    return something
