import random
poem = 'poem.txt'


def get_file_lines(filename):
    """
    gets file and opens allowing to read.
    """

    filename = open(filename, 'r')
    read_file = filename.readlines()
    return read_file


def lines_printed_backwards(lines_list):
    """
    prints lines backwards with their associated line number
    """

    line_counter = len(lines_list) + 1
    for line in reversed(lines_list):
        line_counter -= 1
        print(f'{line_counter} {line}')
    return line


def lines_printed_random(lines_list):
    """
    prints lines randomly 
    """

    random.shuffle(lines_list)
    for line in lines_list:
        print(line)


def lines_printed_custom(lines_list):
    """
    prints 3 random lines creating a short poem like a haiku
    """
    haiku = random.sample(lines_list, 3)
    for line in haiku:
        print(line)


# print(get_file_lines(poem))
# lines_printed_backwards(get_file_lines(poem))
# lines_printed_random(get_file_lines(poem))
lines_printed_custom(get_file_lines(poem))
