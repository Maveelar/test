# Упражнение 120. Форматирование списка
# (Решено. 41 строка)
# Обычно при написании перечислений и  списков мы разделяем их элементы запятыми, а перед последним ставим союз «и», как показано ниже:
# 102  Упражнения
# яблоки
# яблоки и апельсины
# яблоки, апельсины и бананы
# яблоки, апельсины, бананы и лимоны
# Напишите функцию, которая будет принимать на вход список из строк
# и возвращать собранную строку из его элементов в описанной выше манере. Хотя в представленном примере количество элементов списка ограничивается четырьмя, ваша функция должна уметь обрабатывать списки
# любой длины. В основной программе запросите у пользователя несколько
# элементов списка, отформатируйте их должным образом при помощи
# функции и выведите на экран.



words = []
finalString = ''
while True:
    i = input()
    if i == '':
        break
    words.append(i)

if len(words) > 2:
    finalString += ', '.join(words[:len(words) - 2]) + ', '
    finalString += (' и '.join(words[(len(words) - 2):(len(words))]))
else:
    finalString += ' и '.join(words)
print(finalString)

# Яблоки
# лимоны
#
# Яблоки и лимоны


# Пироги
# вишня
# хлеб
# морковь
# сок
# чеснок
#
# Пироги, вишня, хлеб, морковь, сок и чеснок


# Яблоки
#
# Яблоки