#Homework
#Asking for full name and should display first and last, and middle if applicable
print("Hi!")
fullName=input("Please enter your full name:")
space=fullName.find(" ")
firstName=fullName[0:space]
secondSpace=fullName.rfind(" ")
if space!=secondSpace:
    middleName=fullName[space+1:secondSpace]
    lastName=fullName[secondSpace+1:]
    print("Hi,"+firstName,middleName,lastName+"!")
else:
    lastName=fullName[space:]
    print("Hi,"+firstName+lastName+"!")