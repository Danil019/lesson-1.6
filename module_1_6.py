# Словарик
my_dict = {
    "Danil": 2002,
    "Denis": 2001,
    "Kirill": 2006,
    "Tomas": 2004
}
print('Имя и год рождения\n', my_dict)
value = my_dict.get('Danil')
value_none = my_dict.get('Anton', 'Нет такого человека')
print('Вывод одного значения, по его ключу\n',value)
print('Вывод по отсутствующему\n', value_none)
my_dict["Diana"] = 1995
my_dict["Fiona"] = 1998
removed_value = my_dict.pop("Kirill")
print("Удаленный год рождения субъекта Kirill\n", removed_value)
print("Обновленный словарь\n",  my_dict)

# Множество
my_set = {'Danil', 'Danil', 'Danil', 1, 1, 1, 2, 3, 4, 4}
print("\nУникальные значения\n", my_set)
my_set.add(6)
my_set.add("None")
print("Обновленные множества\n",my_set)
my_set.remove(3)
print("Обновленные множества\n",my_set)