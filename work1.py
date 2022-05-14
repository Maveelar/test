# Упражнение 117. Только слова
# (38 строк)
# В данном упражнении вы напишете программу, которая будет выделять
# слова из строки, введенной пользователем. Начните с создания функции,
# принимающей на вход единственный строковый параметр. В  качестве
# результата она должна возвращать список слов из строки с  удаленными знаками препинания, в  число которых должны входить точки, запятые, восклицательный и вопросительный знаки, дефисы, апострофы,
# двоеточия и точки с запятыми. При этом не нужно избавляться от знаков
# Списки  101
# препинания, стоящих внутри слова, таких как апостроф, служащий в английском языке для обозначения сокращений. Например, если на вход
# функции дать строку "Contractions include: don’t, isn’t, and wouldn’t.",
# функция должна вернуть следующий список: ["Contractions", "include",
# "don’t", "isn’t", "and", "wouldn’t"].
# В основной программе, как обычно, должна происходить демонстрация
# вашей функции. Запросите у  пользователя строку и  выведите на экран
# все составляющие ее слова с удаленными знаками препинания. Вам понадобятся написанные при решении заданий 118 и 167 функции, так что
# убедитесь, что основная программа выполняется только в  случае, если
# файл не импортирован в качестве модуля.

def selectWords(str):
    words = []
    word = ''
    index = 0
    for i in str:
        if not i.isalpha():
            if i == '’' and index < (len(str) - 1):
                if str[index+1].isalpha():
                    word += i
            else:
                words.append(word)
                word = ''
        else:
            word += i
            if index == (len(str) - 1):
                words.append(word)
        index += 1
    words = [i for i in words if i != '']
    print(words)

str = input()
selectWords(str)


# "Contractions include: don’t, isn’t, and wouldn’t."
# ['Contractions', 'include', 'don’t', 'isn’t', 'and', 'wouldn’t']


# Поправка







