# Python Class 08_04_Class.py

# 클래스를 정의

class Person:
    def __init__(self):
        self.name = "default name" # 초기화
    def print(self):
        print("My name is {0}".format(self.name))

# 인스턴스생성
p1 = Person()
p2 = Person()
p1.name = "전우치"

p1.print()
p2.print()