class Calculator:
    __result = 0
    
    def __init__(self):
        pass

    def add(self, a):
        self.__result += a

    def subtract(self, a):
        self.__result -= a

    def multiply(self, a):
        self.__result *= a

    def divide(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result /= a

    def modulo(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result %= a

    def power(self, a):
        base = 1
        print(self.__result)
        for i in range(1, a + 1):
            base *= self.__result 
        self.__result = base

    def square_root(self):
        calculated_result = 1
        i = 1
        while calculated_result <= self.__result:
            i += 1
            calculated_result = i * i
        i -= 1
        self.__result = i

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result