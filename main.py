import random
poem = 'poem.txt'


def get_file_lines(filename):
    """
    gets file and opens allowing to read.
    """

    filename = open(filename, 'r')
    read_file = filename.readlines()
    return read_file


# print(get_file_lines(poem))
# lines_printed_backwards(get_file_lines(poem))
# lines_printed_random(get_file_lines(poem))
lines_printed_random(get_file_lines(poem))
