# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    # 초기화 (생성자 메서드)
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    # 인스턴스의 문자열을 출력
    def __str__(self):
        return "{0}, {1}, {2}".format(self.id, 
        self.name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)
#print(account1.__balance)
#백도어(테스트용도)
print(account1._BankAccount__balance)




