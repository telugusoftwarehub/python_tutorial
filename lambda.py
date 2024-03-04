#lambda or anonymous function
#Syntax: lambda argumnets: expression

# def square(x):
#     result = (x**2)
#     print("Result: ",result)

# square(5)

# square = lambda x: x**2
# square_1 = square(5)
# square_2 = square(2)

# print("square_1: ",square_1)
# print("square_2: ",square_2)

#-------- End ---------


#----- Start ---------
# map(), filter() and sorted()


#map() example
# cube = lambda x: x**2
# numbers = [1,2,3,4,5]

# cubed_numbers = list(map(cube, numbers))
# cubed_numbers = list(map(lambda x: x**2, [1,2,3,4,5,6,7,8])) # apply each value

# print("cubed_numbers: ", cubed_numbers)
#---------- End ------------


#--------#filter() example Start ---------
# numbers = [1,2,3,4,5,6,7,8,9]
# is_even = lambda x: x%2 == 0

# even_numbers = list(filter(is_even, numbers)) # True, False

# print("even_numbers: ", even_numbers)

#---------- End ---------------

#------------ Sorted -------------
# super_heros = [("Iron Man", 45), ("Thor", 36), ("Spider Man", 30)]
# sorted_heros = sorted(super_heros, key=lambda hero: hero[1])

# print("sorted_heros: ", sorted_heros)





