a=float(input())
op=str(input())
b=float(input())
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="//":
    if b==0:
        print("ERROR((( MAYBE YOU SHOULD CHECK YOUR WORKK?")
    else:
        print(a//b)
elif op=="/":
    if b==0:
        print("ERROR((( MAYBE YOU SHOULD CHECK YOUR WORKK?")
    else:
        print(a/b)
else:
    print("WRONG OPERATION")