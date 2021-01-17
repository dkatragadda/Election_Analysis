'''
print("Hello world ")

# Creates a variable with a string Frankfurter
title = "Frankfurter"

# Creates a variable with an integer 80
years = 80

# Creates a variable with the boolean value of True
expert_status = True

print("Nick is a professional" + title)
print("Expert status: " + str(expert_status))

# An f-string accepts all data types without conversion
print(f"Expert Status: {expert_status}")

#an f-string for years
print(f"Nick has been coding for {years} years")
print("Nick has been coding for " + str(years) + " years")

counties=["Araphoe","Denver","Jefferson"]
if counties[2]=="Jefferson":
    print(counties[2])

print('this is outside the loop')
'''
temperature=int(input("What is the temperature today?"))

if temperature > 80:
    print('turn on the A/C')
else:
    print('open the windows')







