Hr = input("Enter Hours: ")
Rt = input("Enter Rate: ")

floatH = float(Hr)
floatR = float(Rt)

if floatR > 40 :
    reg = floatR * floatH
    ot = (floatH - 40.0) * floatR
    xtra = reg + ot
else:
    xp = floatH * floatR
print("Pay: ", xp)
