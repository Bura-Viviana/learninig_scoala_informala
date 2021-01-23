age = input("tell me your age ")
age = int(age)
name = input("tell me your name ")
if age < 18:
    print(name + " is a minor person")
else:
    print(name + " is a major person")
