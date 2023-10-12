n = int(input("Enter any number: "))
num1 = 0
num2 = 1
next_number = num2 
count = 1

while count <= n:
	print(next_number, end=" ")
	count += 1
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()