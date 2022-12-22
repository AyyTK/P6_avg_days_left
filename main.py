# Create a program using maths and f-Strings that tells us how many
# days, weeks, months we have left if we live until 90 years old
# Output format: You have x days, y weeks, and z months left.

age = input("How many years old are you? ")
x = 90 - int(age)
d = x * 365
y = x * 52
z = x * 12
print(f"You have {d} days, {y} weeks, and {z} months left.")