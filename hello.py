#List numbers
# nums = [1,4,6,8,2,9,3,5]
#print("nums: ", nums)
#print("nums[2:]: ", nums[2:])

#List strings
heros = ["Iron Man", "He Man", "Spider Man", "Hanu Man"]
#print("Befor DC:", heros)
heros_dc = ["Super Man", "Bat Man"]
heros.extend(heros_dc)
#print("After DC: ", heros)
heros.insert(5, 'Wonder Women')
#print("After WW: ", heros)

#delete a value from a list
heros.pop(1) #del heros[1]
#print("After del: ", heros)

#sort methods
#heros.sort() #orignal list
sorted_list = sorted(heros) #new sorted list
print('Sorted List: ', sorted_list)
print('Sort List', heros)


# Remove item from List
marvel = ["Iron Man", "He Man", "Spider Man", "Hanu Man"]
print("Total No Of Heros in Marvel: ", len(marvel))
marvel.clear()
print("Marvel Comic: ", marvel)
print("Total No Of Heros in Marvel: ", len(marvel))

#Sort a Numbers list
nums = [5,9,8,4,2,1,3,7,6,2]
new_numbs = sorted(nums)
print("Numbers Sort: ", nums.sort(reverse=True))

#Tuple
#mutable and Immutable
users = ('Sai', 'John', 'Prabhas')
heros[0] = "Ant Man"
newusers = list(users)
newusers[0] = "Will Smith"
users = tuple(newusers)

print("Users: ", users)
print(type(users))
print("Updated Tuple to List: ", newusers)
print(type(newusers))
print(max(nums))
print(min(nums))

# print(users.index('Sai'))
# names[0] = "Will Smith"
# print("First Value from Tuple: ", names[0], heros[0])

#Dictionary
