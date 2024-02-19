#my_set = {1,2,3,4,5} #set syntax

my_list = [1,2,3,4,5,3,5,2,7]
my_set = set(my_list)

#add new value
my_set.add(6)
print(my_set)

#remove a value from set
my_set.remove(4)
print(my_set)

#discard
my_set.discard(7)
print(my_set)

print(len(my_set))

## set operations
set_1 = {1,2,3}
set_2 = {3,4,5}

#union
union_set = set_1.union(set_2)
print("Union: ", union_set)

#Intersection
intersetion_set = set_1.intersection(set_2)
print("Intersection: ", intersetion_set)

#difference
difference_set = set_1.difference(set_2)
print("Difference: ",difference_set)

#symentic differece
symentic_diff_set = set_1.symmetric_difference(set_2)
print("Symentic Difference: ", symentic_diff_set)

##frozenset
my_set_1 = frozenset({1,2,3,4,5})
my_set_2 = frozenset({3,4,5,6,7})

union_frozen_set = my_set_1.union(my_set_2)
intersection_frozen_set = my_set_1.intersection(my_set_2)
print("Union on FrozenSet: ", union_frozen_set)
print("Intersection on FrozenSet: ", intersection_frozen_set)
