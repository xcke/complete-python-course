# -- Defining tuples --

short_tuple = "Rolf", "Bob"
tuple_from_list = tuple([1,2,3,4,5])
print(tuple_from_list)
a_bit_clearer = ("Rolf", "Bob")
not_a_tuple = "Rolf"

# -- Adding to a tuple --

friends = ("Rolf", "Bob", "Anne")
friends.append("Jen")  # ERROR!

print(friends)  # ["Rolf", "Bob", "Anne", "Jen"]

# -- Removing from a tuple --

friends.remove("Bob")  # ERROR!

print(friends)  # ["Rolf", "Anne", "Jen"]

# Tuples are useful for when you want to keep it unchanged forever.
# Most of the time I'd recommend using tuples over lists, and only use lists when you specifically want to allow changes.
