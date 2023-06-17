class MyException1(Exception): 
    def init(self, message):
        self.message = message
        
class MyException2(Exception):
    def init(self, message):
        self.message = message
        
class MyException3(Exception):
    def init(self, message):
        self.message = message
        
def test_function(num): 
    if num < 0:
        raise MyException1('Число должно быть положительным')
    elif num > 100:
        raise MyException2('Число должно быть меньше или равно 100')
    else:
        raise MyException3('Произошла неизвестная ошибка')
try:
    test_function(150) 
except MyException1 as e:
    print(e.message)
except MyException2 as e: 
    print(e.message)
except MyException3 as e: 
    print(e.message)
