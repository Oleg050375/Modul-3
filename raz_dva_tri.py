data_struct = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
def css(*args):  # определение функции
    a = 0  # задание начального значения
    for i in args:
        if isinstance(i, int) or isinstance(i, float):  # проверка на число
            a = a + i
        elif isinstance(i, str):  # проверка на строку
            a = a + len(i)
        elif isinstance(i, list):  # проверка на список
            for k in i:
                a = a + css(k)
        elif isinstance(i, dict):  # проверка на словарь
            sum_k = 0
            sum_v = 0
            for sv in list(i.values()):  # цикл подсчёта значений
                sum_v = sum_v + css(sv)
            for sk in list(i.keys()):  # цикл подсчёта длин ключей
                sum_k = sum_k + len(sk)
            a = sum_v + sum_k
        elif isinstance(i, set):  # проверка на множество
            for s in list(i):
                a = a + css(s)
        elif isinstance(i, tuple):  # проверка на кортеж
            for l in list(i):
                a = a + css(l)
    return a

print(css(data_struct))
