def print_args(a = 1, b = 'строка', c = True): # определение функции вывода аргументов
    print(a, b, c)

values_list = [False, 7, 'чебурашка'] # создание списка
values_list_2 = [True, 79] # создание сокращённого списка
values_dict = {'a': 'сокол', 'b': True, 'c': 9} # создание словаря

print_args(*values_list) # вывод полного списка с распаковкой
print_args('финик', *values_list_2) # вывод сокращённого списка с распковкой
print_args(**values_dict) # вывод занчений словаря