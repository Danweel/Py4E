hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Hours:")
r = float(rte)

ot = ((h-40)*(r*1.5))
wd = 40*r

def computepay(h,r):

    if h > 40:
        return ot + wd
    else:
        return h * r

p = computepay(h,r)
print("Pay",p)
