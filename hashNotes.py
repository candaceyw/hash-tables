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

def my_hash(s):
    # take every character in the string, and convert character to number
    # Convert each character into UTF-8 numbers
    string_utf = s.encode()

    total = 0

    for char in string_utf:
        total += char
    return total

print(my_hash('Hello'))
print(my_hash('Hello'))
print(my_hash('World'))