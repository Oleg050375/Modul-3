def get_multiplied_digits(number):  # создание рекурсивной функции
    str_number = str(number)  # трансформация числа в строку
    first = int(str_number[0])  # выделение первой литеры числа с трансформацией обратно в число
    if len(str_number) == 1:  # проверка на разрядность
        return first
    return first * get_multiplied_digits(int(str_number[1:]))  # возврат произведения литеры на следующую

print(get_multiplied_digits(40203))