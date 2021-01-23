friend1 = "Rolf"
friend2 = "Bob"
friend3 = "Anne"

friends = ["Rolf", "Bob", "Anne"]
friends_another = list(["cisco", "juniper", "ubiq"])

print(friends[0])  # This is called a subscript
print(friends[1])

# You can put anything you like inside a list, but it's almost always a good idea to keep it homogeneous.

friends = ["Rolf", 2, "Anne", True]  # Generally a bad idea

# -- Length of a list --

friends = ["Rolf", "Anne"]
print(len(friends))  # 2

# -- Lists inside lists --
# As mentioned earlier, you can put anything inside a list—and that includes other lists.
arp_table_in_list_format = [
    ["1.1.1.1", "MAC_ADDR_A"],
    ["1.1.1.2", "MAC_ADDR_b"],
    ["1.1.1.3", "MAC_ADDR_c"],
    ["1.1.1.4", "MAC_ADDR_d"],
    ["1.1.1.5", "MAC_ADDR_e"]
    ]
arp_table_in_list_format[0] = ["8.8.8.8", "MAC_ADDR_A"]

for ip,mac in arp_table_in_list_format:
    print(f"{ip}-{mac}")

friends = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]
print(friends[0][1])  # 24
print(friends[1][0])  # Bob

# -- Long lists --

friends = [
    ["Rolf", 24],
    ["Bob", 30],
    ["Anne", 27],
    ["Charlie", 37],
    ["Jen", 25],
    ["Adam", 29],
]

# -- Adding to a list --

friends = ["Rolf", "Bob", "Anne"]
friends.append("Jen")

print(friends)  # ["Rolf", "Bob", "Anne", "Jen"]

# -- Removing from a list --

friends.remove("Bob")

print(friends)  # ["Rolf", "Anne", "Jen"]

# Remember if you have a list of lists, for example, you still need the entire thing you want to remove:

friends = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]

friends.remove(["Bob", 30])

arp_table_in_list_format_len = len(friends)

arp_table_in_list_format_just_the_first_3 = arp_table_in_list_format[:3] # it will include Item number 0,1,2
my_vendor = "Cisco"

print(arp_table_in_list_format_len)
print(arp_table_in_list_format_just_the_first_3)
print(my_vendor)