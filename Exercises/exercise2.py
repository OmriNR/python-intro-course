#Indexing string
s = "Hello World!"
print(s[0]) #H
print(s[6]) #W
print(s[11]) #!

print(s[-1]) #!
print(s[-6]) #W
print(s[-12]) #H

#Slicing strings
print(s[0:5])
print(s[6:11])

print(s[:5])
print(s[6:])
print(s[-6:-1])

#Conditions
grade = 85

if grade >= 60:
    print("Passing")

if grade >= 90:
    print("Excellent!")

grade = 75

if grade >= 90:
    print("Excellent")
elif grade >= 80:
    print("Very Good")
elif grade >= 60:
    print("Passing")
else:
    print("Failing")

color = "red"
if color == "red" or color == "blue":
    print("Primary color")

x = 5
if x > 0 and x < 10:
    print("x is between 0 and 10")

logged_in = False
if not logged_in:
    print("Please log in")
    
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
elif age >= 18 and not has_id:
    print("Show your ID")
else:
    print("Entry denied")