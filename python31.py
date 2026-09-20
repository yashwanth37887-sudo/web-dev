a=float(input("enter first number"))
b=float(input("enter second number"))
c=float(input("enter third number"))
if a>=b:
    if a>=c:
        print(f"{a} is largest")
    else:
        print(f"{c} is largest")
elif b>=a:
    if b>=c:
        print(f"{b} is the largest")
    else:
        print(f"{c} is the largest")
else:
    pass
