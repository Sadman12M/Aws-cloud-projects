print("hello from Mirza's Docker Container")
print("--------------Simple Calculator work--------------")
 
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

print("Choose operation you want to do:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice=input("Choose 1/2/3/4 :")

if choice=="1":
	print("Result:",num1+num2)
elif choice=="2":
	print("Result:",num1-num2)
elif choice=="3":
	print("Result:",num1*num2)
elif choice=="4:":
	if num2==0:
		print("cannot divide by zero")

	else:
		print("Result:",num1/num2)
else:
	print("Invalid choice")
	