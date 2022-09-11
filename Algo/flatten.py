def flatten(arr):
    res = []
    for i in range(len(arr)):
        if type(arr[i]) is list:
            flat = flatten(arr[i])
            for j in range(len(flat)):
                res.append(flat[j])
            flatten(arr[i])
        else:
            res.append(arr[i])
    return res

print(flatten([[1], [[2, 3]], [[[4]]]])) # -> [1, 2, 3, 4]


def removeDupes(str):
    return ''.join(set(str))


print(removeDupes('abcd')) # // -> 'abcd'
print(removeDupes('aabbccdd')) # // -> 'abcd'
print(removeDupes('abcddbca')) # // -> 'abcd'
print(removeDupes('abababcdcdcd')) # // -> 'abcd'