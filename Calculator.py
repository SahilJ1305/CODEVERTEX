a = float(input("Enter First Number:"))
b = float(input("Enter Second Number:"))
print("Please Select the option from 1 to 4")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
c = int(input('Enter the option:'))
if c == 1:
  print("Addition of",float(a) ,"and", float(b), "is:",float(a) + float(b))
elif c==2:
  print("Subtraction of",float(a), "and", float(b), "is:",float(a) - float(b))
elif c==3:
  print("Mutiplication of",float(a), "and", float(b), "is:",float(a) * float(b))
elif c==4:
  print("Division of",float(a) ,"and", float(b), "is:",float(a) / float(b))
else:
  print("Invalid Option !!")