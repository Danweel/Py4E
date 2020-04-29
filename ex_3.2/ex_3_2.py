hrs = input("Enter Hours:")
h = float(hrs)

r = 10.50
ot = r*1.5

#error handling:
try:
    h = float(h)
except:
    print("You need to enter only the # of hours accrued. Use only whole or decimal numbers.")
    continue

try:
    h > 0
except:
    print("Number of hours must be greater than zero.")
    continue

#to calculate pay:
if h > 40:
  p = float(40*r + (h-40) * ot)
  print(p)

else:
  p = float(h*r)
  print(p)
