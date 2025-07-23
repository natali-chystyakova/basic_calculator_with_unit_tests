## 🧮 basic_calculator_with_unit_tests
Цей застосунок демонструє роботу модульного тестування для простого калькулятора.


📌 Призначення

* за допомогою doctest — для перевірки прикладів у рядках документації;

* за допомогою unittest — для створення окремих тестових класів і методів.



## 🔍 Тестування на основі функцій (doctest)

### ✅ Якщо тести та програма в одному файлі:

if __name__ == '__main__':
    import doctest
    doctest.testmod()


▶️ Запуск doctest через термінал:
python -m doctest -v basic_calculator.py

### ✅ Якщо тести в окремому файлі (doctests.txt):


if __name__ == '__main__':
    import doctest
    doctest.testfile("doctests.txt")
    
▶️ Запуск doctest через термінал:
python -m doctest -v doctests.txt

### 🧪 Тестування об'єкта на основі класу (doctest)

✅ Якщо тести та програма в одному файлі:

if __name__ == '__main__':
    import doctest
    doctest.testmod()

✅ Якщо тести в окремому файлі (class_calculator_doctests.txt):
if __name__ == '__main__':
    import doctest
    doctest.testfile("class_calculator_doctests.txt")

▶️ Запуск doctest через термінал:
python -m doctest -v class_calculator_doctests.txt


## 🧷 Юніт-тести (unittest)

✅ Запуск усіх тестів у файлі test_calculator.py:

if __name__ == '__main__':
    import unittest
    unittest.main()
    
### ▶️ Запуск через термінал:
python -m unittest -v test_calculator

### ▶️ Запуск тестів окремого класу:
python -m unittest -v test_calculator.TestCalculator

### ▶️ Запуск одного конкретного тесту:
python -m unittest -v test_calculator.TestCalculator.test_addition





