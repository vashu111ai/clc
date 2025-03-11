def add():
    a = int(input("first value."))
    b = int(input("second value.."))
    print("the add of", a ,"and", b ,"is" ,a+b)
def sub():
    a = int(input("first value."))
    b = int(input("second value.."))
    print("the sub of", a ,"and", b ,"is" ,a-b)

def mul():
    a = int(input("first value."))
    b = int(input("second value.."))
    print("the multiple of", a ,"and", b ,"is" ,a*b)
def div():
    a = int(input("first value."))
    b = int(input("second value.."))
    print("the divide of", a ,"and", b ,"is" ,a/b)
def power():
    a = int(input("Give a No for power of"))
    b = int(input("power value"))
    print(a**b)
print("this is vahsu calc in python")
c = input("what you want to do like + - * / po")
if c == "+":
    add()
elif c == "-":
    sub()
elif c == "*":
    mul()
elif c == "/":
    div()
elif c == "po":
    power()
else:
    print("wrong input please choose between + - * / only")
