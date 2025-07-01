# Sets(sets do not allow duplicates but can remove and add)
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Add value on my set
my_set.add(6)
print(my_set)

# Remove value on my set
my_set.remove(3)
print(my_set)

# operations with sets(allow you manipulate and compare collections of elements)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
#union
union_set = set1.union(set2)
print(union_set)

# Intersection menthod(find the comon element)
inter_set = set1.intersection(set2)
print(inter_set)

# Difference(find the element the is present to one but not to other)
diff_set = set1.difference(set2)
print(diff_set)
