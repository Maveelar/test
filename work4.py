# Упражнение 122. «Поросячья латынь»
# (32 строки)
# «Поросячьей латынью» называют молодежный жаргонный язык, производный от английского. И  хотя корни этого новообразованного языка
# неизвестны, упоминание о  нем есть как минимум в  двух документах,
# датированных XIX веком, а  это значит, что ему уже больше сотни лет.
# Для перевода слова с английского на «поросячью латынь» нужно сделать
# следующее:
#  если слово начинается с согласной буквы (включая y), то все буквы
# с начала слова и до первой гласной (за исключением y) переносятся
# в конец слова и дополняются сочетанием букв ay. Например, слово
# computer будет преобразовано в omputercay, а слово think – в inkthay;
#  если слово начинается с гласной буквы (не включая y), к концу слова просто добавляется way. К примеру, слово algorithm превратится
# в algorithmway, а office – в officeway.
# Напишите программу, которая будет запрашивать у пользователя строку. После этого она должна переводить введенный текст на «поросячью
# латынь» и выводить его на экран. Вы можете сделать допуск о том, что
# все слова пользователь будет вводить в нижнем регистре и разделять их
# пробелами.



vowels = 'aeuio'

word = input()

if word[0] in vowels:
    finalWord = word + 'way'

else:
    finalWord = ''
    index = -1
    for i in word:
        index += 1
        if i in vowels:
            finalWord += word[index:len(word)] + word[0:index] + 'ay'
            break
print(finalWord)


# algorithm
# algorithmway

# run
# unray

# computer
# omputercay
