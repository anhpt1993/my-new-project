#-----PERSONAL INFORMATION-----

name = input("What's your name?: ")
age = None

while True:
    try:
        age = int(input("How old are you?: "))
        break
    except ValueError:
        print("-------------------------------")
        print("Aren't you from Earth?")
        print("Please enter a positive integer")
        print("-------------------------------")
        print()


address = input("What is your address?: ")
purpose = input("What is your purpose in coming to the Earth?: ")
print()

print("Hello there. The following is your personal information:" )
print()

print("Your name is ", name.upper())
print()

if age >= 0:
    print("Your age is ", str(age), " year(s) old")
else:
    print("Your age is ", str(age), " year(s) old")
    print("Shit! You haven't born yet!!!")
print()

print("You are now living in ", address)
print()

print("And, you come to the Earth to ", purpose)