#연습문제1 
List = ["Life", "is", "too", "short"]
result = " ".join(List)
print(result)

# 연습문제 (if) 답 : shirt

star1 = ""
while star1 < "*****":
    star1 += "*"
    print(star1)
    if star1 == "****": 
        break   


str1 = "mutzangesazachurum"
a = "aeiou"
count = 0
for i in str1:
    if i in a: 
       count += 1

print(count) 


num1 = 0
sum1 = 0 
while num1 < 1000:
    num1 += 1
    if (num1 % 3) != 0:continue
    sum1 = sum1 + num1
print(sum1)

num = 10
while num >0:
    num -=1
    print("*"*num)


A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0

while A:
    num = A.pop()
    if num >= 50:
        sum += num

print(sum)

for n in range(1, 101):
    print(n)

B = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum2 = 0
for num2 in B:
    sum2 += num2
ave = sum2 / len(B)
print(ave)

num3 = [1, 2, 3, 4, 5]
result = [n3*2 for n3 in num3 if n3%2==1]
print(result)