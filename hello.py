#List numbers
nums = [1,4,6,8,2,9,3,5]
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
