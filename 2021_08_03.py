# 2021_08_03.py

phone = { "kim" : "1111", "lee" : "2222", "park" : "3333"}
phone.keys()
phone.values()
print("park" in phone)
print("moon" in phone)
p = phone
print(p)

# 강제복사

a = [1,2,3]
b = a[:]
print(id(a), id(b))
a[0] = 38
print(a)
print(b)
print(id(a),id(b))

# if 문

# money = True
# if money:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")    

# score = int(input("Input Score: "))
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"        

# print("Grade is : " + grade)

# FOR문

print("---Break구문---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---Continue구문---")
for i in lst:
    if i %2 == 0:
        continue
    print("Item:{0}".format(i))

print("---Continue구문---")
for i in lst:
    if i %2 == 1:
        continue
    print("Item:{0}".format(i))


# 수열 함수

print(range(10))
print(list(range(10)))
print(set(range(10)))
print(tuple(range(10)))
print(list(range(2000,2022)))
print(list(range(10,0,-1)))

# 수동으로 루프를 돌리는 경우

for i in range(5):
    print(i)

