class MyException1(Exception): # Определяем три класса исключений: MyException1, MyException2 и MyException3. 
    def init(self, message): # Каждый класс наследуется от базового класса Exception, и определяет метод init для задания сообщения об ошибке. 
        self.message = message
        
class MyException2(Exception):
    def init(self, message):
        self.message = message
        
class MyException3(Exception):
    def init(self, message):
        self.message = message
        
def test_function(num): #Определяем функцию test_function с одним аргументом num, которая проверяет значение num
    if num < 0:
        raise MyException1('Число должно быть положительным')
    elif num > 100:
        raise MyException2('Число должно быть меньше или равно 100')
    else:
        raise MyException3('Произошла неизвестная ошибка')
    # Если num меньше нуля, то возбуждается исключение MyException1 с сообщением "Число должно быть положительным".
    # Если num больше 100, то возбуждается исключение MyException2 с сообщением "Число должно быть меньше или равно 100".
    # В остальных случаях возбуждается исключение MyException3 с сообщением "Произошла неизвестная ошибка".
try:
    test_function(150) # В блоке try-except вызываем функцию test_function с аргументом 150. 
except MyException1 as e: #Если в функции возникает исключение MyException1, то перехватываем его и выводим сообщение об ошибке.
    print(e.message)
except MyException2 as e: #Если возникает исключение MyException2, то выводим сообщение об ошибке этого типа исключения
    print(e.message)
except MyException3 as e: #Если возникает исключение MyException3, то также выводим сообщение об ошибке этого типа исключения.
    print(e.message)