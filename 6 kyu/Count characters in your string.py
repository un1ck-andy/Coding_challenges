'''
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

'''


def count(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


def count2(string):
    return {i: string.count(i) for i in string}
