print('Arthmetic Operators!')
a = 10
b = 4

print("Addition: ", a + b)
print("Substraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)


print("Floor Division: ", a // b)
print("Modulus: ", a % b)
print("Exponentiation: ", a ** b)


print('*************** Comparison Operators! ***************')

print('Equal to: ', a == b)
print('Not Equal to: ', a != b)
print('Greater than: ', a > b)
print('Less than: ', a < b)
print('Greater than & Equal to: ', a >= b)
print('Less than & Equal to: ', a <= b)

print('*************** Logical Operators! ***************')

x = True
y = False

print(x and y) # False &&
print(x or y) #
print(not x)


#print('(a + b) and (a - b): ', (a + b) == 14 or (a - b) > 6)  #Output: 

print('*************** Assignment Operators! ***************')

k = 5 ##Assignment
k += k
k += k

print('K Value: ', k)

print('*************** Bitwise Operators! ***************')

d = 5 # binary representation 101
e = 3 # 011 111 - 1

print(d | e) #101|011 ->  111


print('*************** Membership Operators! ***************')

my_list = [1,2,3,4,5]
print('3 is prensent in list: ', 3 in my_list)
print('8 is not prensent in list: ', 8 not in my_list)


print('*************** Identity Operators! ***************')
my_list_1 = [1,2,3,4,5]
my_list_2 = [1,2,3,4,5]

print('my_list_1 is my_list_2: ', my_list_1 is my_list_2)
print('my_list_1 is not my_list_2: ', my_list_1 is not my_list_2)
