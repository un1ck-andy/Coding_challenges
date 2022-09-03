"""
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

"""


def comp(array1, array2):
    try:
        return sorted([x * x for x in array1]) == sorted(array2)
    except:
        return False
