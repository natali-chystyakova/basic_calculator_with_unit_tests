# basic_calculator_with_unit_testss
This application describes the work of unit tests of a simple calculator
 * если тесты и программа в одном файле:
 if __name__=='__main__':
    import doctest
    doctest.testmod()

 * запуск doctest через коммандную строку:
 python -m doctest -v basic_calculator.py


 * если тесты в отдельном файле:
 if __name__=='__main__':
     import doctest
     doctest.testfile("doctests.txt")

 * запуск doctest через коммандную строку:
 python -m doctest -v doctests.txt
