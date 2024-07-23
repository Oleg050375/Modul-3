colls = 0  # глобальная переменная счётчика вызовов функцийdef count_colls():
def count_colls(): # определение функции счётчика вызовов функций
    global colls  # переопределение глобальной переменной
    colls = colls + 1  # инкремент переменной счётчика вызовов
    #print(colls)
def string_info(string): # определение функции информации о строке
    count_colls() # вызов функции счётчика
    a = len(string) # опредение длины строки
    b = string.upper() # формирование строки в верхнем регистре
    c = string.lower() # формирование строки в нижнем регистре
    d = (a, b, c) # создание целевого кортежа
    print(d)
def is_contains(string, list_to_search): # определение функции детектирования вхождения
    count_colls()
    for i in range(len(list_to_search)): # механизм понижения регистра строки, входящей в список
        if isinstance(list_to_search[i], str):
            list_to_search[i] = list_to_search[i].lower()
    string = string.lower() # понижение регистра строки
    print(string in list_to_search) # печать результата проверки вхождения

string_info('нечто')
is_contains('Qwe', [1,'qWe',3])
string_info('тарабарщина')
print(colls)