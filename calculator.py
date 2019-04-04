from module import *

print(" Menu")
print("--------")

Menu = int(input("""
1: add

2: sub

3: mul

4: div

5: stop

:"""))

num1 = int(input("num1: "))
num2 = int(input("num2: "))

a = FourCal(num1,num2)
if Menu == 1:

    print(a.add())

elif Menu == 2:

    print(a.sub())

elif Menu == 3:

    print(a.mul())
elif Menu == 4:

    print(a.div())

elif Menu == 5:
    print("계산을 멈춥니다.")

