my_input = 'aaaabaabcccddaaaaaa'


def code(input_str):
    if input_str == '':
        return 0
    counter: int = 0
    prev_char: str = '0'
    result: str = ''
    for letter in input_str:
        if letter == prev_char:
            counter += 1
        else:
            if prev_char != '0':
                result = result + str(counter) + prev_char
            prev_char = letter
            counter = 1
    result = result + str(counter) + letter
    return result


print(code(my_input))

