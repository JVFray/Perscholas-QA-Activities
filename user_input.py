print("Let me tell you about your numbers!")
print("Give me 4 random numbers")

a = int(input("Add your first number "))
b = int(input("Add your second number "))
c = int(input("Add your third number "))
d = int(input("Add your fourth number "))

list = []
list.append(a)
list.append(b)
list.append(c)
list.append(d)

list.sort()
print (list)
print("Your smallest number is", list[0] )
print("Your largest number is", list[3])