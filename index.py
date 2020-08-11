records = [
    {"Alice", "Engineering"},
    {"Bob", "Sales"},
    {"Carol", "Sales"},
    {"Sarah", "Sales"},
    {"Pranjal", "Sales"},
    {"Dave", "Engineering"},
    {"Erin", "Engineering"},
    {"Frank", "Engineering"},
    {"Grace", "Marketing"},
    {"Charles", "Marketing"},
    {"Jordan", "Marketing"},
]


# proposed dictionary
# keys will ber departments
# values array of names, or list of names
def build_index(recs):
    index = {}

    for record in recs:
        name, dept = record

        # check if department is already in index
        if dept in index:
            # if it is, add name to the list
            index[dept].append(name)
        else:
            # else create new key with list with name in it. Index = key
            index[dept] = [name]

    return index

department_index = build_index(records)
# Print all the departments
print(department_index.keys())
# print everyone in Engineering:
print(department_index['Engineering'])
# Print everyone in Sales:
print(department_index['Sales'])

# print everyone in marketing:
print(department_index['Marketing'])
