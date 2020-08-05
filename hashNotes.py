words = ["apple", "book", "cat", "dog", "egypt", "france"]


# to access egypt, runtime is O(n)

## What if we had a magic function
# Takes a word ----> returns the index for wehre that word is located in some array
# book -> 1
# egypt -> 4
# fake_word -> None
# this function is O(1)
#
# HASH FUNCTIONS
# Any string input ---> A Specific number (within some range)
# MOST IMPORTANT:
# This function must be deterministic

def my_hash(s, limit):
    # take every character in the string, and convert character to number
    # Convert each character into UTF-8 numbers
    string_utf = s.encode()

    total = 0

    for char in string_utf:
        total += char
        total &= 0xffffffff  # limit total to 32 bits
    return total % limit

# print(my_hash('Hello'))
# print(my_hash('Hello'))
# print(my_hash('World'))

hash_table = [None] * 8

hash_table_python = dict() # same as going {} for a hash table.

# Add items to has_table using the my_hash function
index = my_hash('card', len(hash_table))
hash_table[index] = "Value for card"

index = my_hash('apple', len(hash_table))
hash_table[index] = "Value for apple"

# Retrieve some items from has_table
# Lets retrieve the value for "hello"
index = my_hash("card", len(hash_table))
print(hash_table[index])
print(hash_table)