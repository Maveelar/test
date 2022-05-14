# Упражнение 123. «Поросячья латынь» (продолжение)
# (51 строка)
# Расширьте свое решение упражнения 122, чтобы ваш анализатор корректно обрабатывал символы в верхнем регистре и знаки препинания, такие
# как запятая, точка, а также восклицательный и  вопросительный знаки.
# Если в оригинале слово начинается с заглавной буквы, то в переводе на
# «поросячью латынь» оно также должно начинаться с  заглавной буквы,
# тогда как буквы, перенесенные в конец слов, должны стать строчными.
# Например, слово Computer должно быть преобразовано в Omputercay. Если
# в конце слова стоит знак препинания, он там же и должен остаться после
# выполнения перевода. То есть слово в конце предложения Science! необходимо трансформировать в Iencescay!.
# Упражнение 124. Линия наилучшего соответ



vowels = 'aeuio'

word = input()

if word[0] in vowels:
    finalWord = word + 'way'

else:
    finalWord = ''
    index = -1
    for i in word:
        index += 1
        if not word[len(word) - 1].isalpha():
            newWord = word[0:len(word)-1]
            if i in vowels:
                finalWord += newWord[index:len(word)] + newWord[0:index] + 'ay' + word[len(word) - 1]
                break
        else:
            if i in vowels:
                finalWord += word[index:len(word)] + word[0:index] + 'ay'
                break


print(finalWord.title())

# Computer
# Omputercay

# Science!
# Iencescay!