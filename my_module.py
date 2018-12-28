# this module shall be imported to the test-module.py

print("imported my_module")

test = 'Test String'


def find_index(to_search, target):
    """ find index of a value in a sequence """
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
