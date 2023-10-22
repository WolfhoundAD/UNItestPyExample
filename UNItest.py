#В этом примере мы импортируем модуль unittest, который предоставляет основные функциональности для написания тестов. 
#Затем мы создаем класс MyTestCase, который наследуется от unittest.TestCase. Внутри класса определен метод test_add_two_numbers, 
#который содержит тестовый случай.
#Мы вызываем функцию add_two_numbers с разными аргументами и сравниваем результат с ожидаемым значением, используя метод assertEqual. 
#Если проверка не проходит, то тест считается неуспешным.
#Наконец, мы используем unittest.main() для запуска всех тестов в данном модуле.
import unittest
def add_two_numbers(a, b):
    return a + b

class MyTestCase(unittest.TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(3, 5)
        self.assertEqual(result, 8)  # Проверяем, что результат равен ожидаемому значению

        result = add_two_numbers(-2, 2)
        self.assertEqual(result, 0)  # Проверяем еще один случай

if __name__ == '__main__':
    unittest.main()


#В этом примере мы также импортируем модуль unittest и создаем класс MyTestCase, который наследуется
#от unittest.TestCase. Внутри класса определен метод test_is_prime, который содержит тестовые случаи.
#Мы вызываем функцию is_prime с разными аргументами и сравниваем результат с ожидаемыми значениями, 
#используя методы assertTrue и assertFalse. Если проверка не проходит, то тест считается неуспешным.
#В этом примере мы тестируем функцию is_prime, которая проверяет, является ли число простым. 
#Мы проверяем, что число 7 является простым, число 10 не является простым, а число 1 не является простым.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

class MyTestCase(unittest.TestCase):
    def test_is_prime(self):
        result = is_prime(7)
        self.assertTrue(result)  # Проверяем, что число 7 является простым

        result = is_prime(10)
        self.assertFalse(result)  # Проверяем, что число 10 не является простым

        result = is_prime(1)
        self.assertFalse(result)  # Проверяем, что число 1 не является простым

if __name__ == '__main__':
    unittest.main()