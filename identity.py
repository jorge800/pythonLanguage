# Python Identity Operator.

x = ["Apple","Banana"]
y = ["Dates", "Almonds"]
z = x
print(z is z)
z = y
print(z is y)
print(x is not y)
print (z is not z)
print(x == y)
print(z == y)
print(x == z)
print(y == z)
exit()
