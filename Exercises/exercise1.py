#Print
print("Hello, World!")

print(3+5)

print("The result of 3 + 5 is:", 3 + 5)

x = 8
print("The value of x is:", x)

print("Is 2 less than 5?", 2 < 5)
print("Is 10 greater than 20?", 10 > 20)

#variables
x = 1
my_variable = 2
result_1 = 3
student_name = "Alice"
print(x, my_variable, result_1, student_name)

#invalid name - starts with digit
#1variable = 10  # This will cause a syntax error

#case sensitivity
Variable = 5
variable = 10
VARIABLE = 15
print(Variable, variable, VARIABLE)

#Data types
a = 10  # integer
print(type(a))

b = 3.14  # float
print(type(b))

c = "Hello"  # string
print(type(c))

d = True  # boolean
print(type(d))

print(type(3))
print(type(3.0))

print(type(2+5.0))


#casting
x = int(3.9)
print(x)
print(type(x))

y = float(5)
print(y)
print(type(y))

s = str(42)
print(s)
print(type(s))

n = int("123")
print(n)
print(type(n))

#operators
a = 16
b = 7

print("Addition", a+b)
print("Substraction:", a-b)
print("Multiplication:", a*b)
print("Division:",a/b)
print("Floor division:",a//b)
print("Modulo:",a%b)
print("Exponentiation:",a**b)

n = 14
print(n % 2 == 0)

n = 7
print(n%2 == 0)


#string operators
first = "Hello"
second = " World"
print(first + second)

print("ha" * 3)
print('-' * 20)

print("cat" in "concatenation");
print("xyz" in "hello")

age = 23
print("My age is: " + str(age))

#Logical operators
print(not False)
print(not True)

x = 5
print(not (x > 10))