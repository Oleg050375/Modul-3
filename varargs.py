def singl_root_words(root_word, *other_word):  # определение функции
    same_word = []  # создание исходного пустого списка результата
    for w in other_word:  # цикл перебора заданного списка
      if w.lower() in root_word.lower():  # проверка на входимость с выравниванием регистра
            same_word.append(w)
      elif root_word.lower() in w.lower():  # проверка на обратную входимость с выравниванием регистра
            same_word.append(w)
    return same_word

result_1 = singl_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result_2 = singl_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result_1)
print(result_2)
