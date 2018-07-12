# Python Simple Calculator
def add():
  print("Enter first number: ")
  num = float(input())
  print("Enter another number: ")
  var = float(input())
  sum = float((num + var))
  print("The sum is: "+str(sum)+".")
  print("Do you want to exit?")
  check = str(input())
  if check == "Y" or check == 'y':
    exit()
  else:
    add()

add()
