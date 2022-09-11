def encode(s: str):
    prev_char: str = ''
    counter: int = 1
    result: str = ''
    for char in s:
        if char == prev_char:
            counter += 1
        else:
            if prev_char != '':
                result += str(counter) + prev_char
            counter = 1
            prev_char = char
    result += str(counter) + prev_char
    return result


s = 'aaaaaaaaaaaaabbscccccccd'
print(encode(s))
