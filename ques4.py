# Python Program to find the GCD of two numbers using recursion

def gcd(a,b):
	if(b==0):
		return a
	else:
		return gcd(b,a%b)


# taking first number from the user
a=int(input("Enter first number:"))

# taking second number from the user
b=int(input("Enter second number:"))

GCD=gcd(a,b)

print("GCD is: ")
print(GCD)

# end of program
