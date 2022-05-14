# Упражнение 118. Словесные палиндромы
# (34 строки)
# В упражнениях 75 и 76 мы уже имели дело со словами, являющимися палиндромами. Тогда мы анализировали буквы в слове с начала и конца, игнорируя пробелы и  знаки препинания, чтобы понять, совпадает ли его
# написание в  прямом и  обратном направлениях. И  хотя палиндромами
# обычно называют слова, это понятие вполне можно расширить. Например,
# английская фраза «Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?» является словесным палиндромом,
# поскольку если читать ее по словам, игнорируя при этом знаки препинания
# и заглавные буквы, в обоих направлениях она будет звучать одинаково. Еще
# примеры английских словесных палиндромов: «Herb the sage eats sage, the
# herb» и «Information school graduate seeks graduate school information».
# Напишите программу, которая будет запрашивать строку у пользователя и оповещать его о том, является ли она словесным палиндромом. Не
# забывайте игнорировать знаки препинания при выявлении результата.

words = input().split()
reverseWords = words[::-1]
for index in range(len(words)):
    word1 = ''
    word2 = ''
    flag = True
    for i in words[index]:
        if i.isalpha():
            word1 += i
    for z in reverseWords[index]:
        if z.isalpha():
            word2 += z
    if word1.lower() != word2.lower():
        flag = False
        break
    word1 = ''
    word2 = ''
print(flag)

# Herb the sage eats sage, the herb
# True

# Herb the sage eats sageasdasd, the herb
# False


# Information school graduate seeks graduate school information
# True

# Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?
# True








