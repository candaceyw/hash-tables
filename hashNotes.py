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
class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


hash_table = [None] * 8


def my_hash(s):
    # take every character in the string, and convert character to number
    # Convert each character into UTF-8 numbers
    string_utf = s.encode()
    total = 0

    for char in string_utf:
        total += char
        total &= 0xffffffff  # limit total to 32 bits
    return total


def hash_index(key):
    hash_num = my_hash(key)
    return hash_num % len(hash_table)


def put(key, val):
    # has the key and get an index
    i = hash_index(key)
    # find the start of the linked list using the index
    # search through linked list
    # If the key already exists in teh linked list
    # replace the value
    # else
    # add new HashTable entry to the haed of linked list

    # this can be deleted
    # CHECK IF SOMETHING ALREADY EXISTS AT THAT INDEX
    # if hash_table[i] != None:
    #     print(f"Collision! Overwriting {repr(hash_table[i])}!")
    # hash_table[i] = val


def get(key):
    # has the key and get an index
    i = hash_index(key)
    # Get the linked list AT the computed index
    # Search through the linked list for the key
    #   Compare keys until you find the right one
    # if it exists, return the value
    # else, return None

    # return the value from the array at the index
    # return hash_table[i]


def delete(key):
    # has the key and get an index
    i = hash_index(key)
    # Search through the linked list for the matching key
    # delete that node
    # return value of deleted node (or None)


def resize():
    # Make a new array that's DOUBLE the current size
    # Go through each linked list in the array
    # Go through each item and re-has it
    # insert the items into their new location
    pass


def shrink():
    # same as resize, but reduce array by HALF
    pass


put("Hello", "Hello Value")
put("world", "world value")

print(hash_table)
# print(my_hash('Hello'))
# print(my_hash('Hello'))
# print(my_hash('World'))
