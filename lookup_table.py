import math

# Inverse square root is 1 / square root of number
#  realatively time consuming
def get_inverse_square(num):
    return 1 / math.sqrt(num)

# we need to constantly get the inverse squaqre rooots of numbers between 1 and 1000

# what should our lookup table look like?
#Keys will be numbers
def build_lookup_table():
    lookup_table = {}
    for i in range(1, 1000):
        lookup_table[i] = get_inverse_square(i)
    return lookup_table

sqrt_lookup_table = build_lookup_table()

print(sqrt_lookup_table[3])
print(sqrt_lookup_table[982])
print(sqrt_lookup_table[234])