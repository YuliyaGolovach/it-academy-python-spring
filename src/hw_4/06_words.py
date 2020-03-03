""" Слова

Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим числом
пробелов или символами конца строки. Определите, сколько различных слов
содержится в этом тексте
Пробельные символы: [ \f\n\r\t\v].
Непробельные символы: Все, кроме пробельных.
"""

print('Input line numbers:')
n = int(input())
print('Input {} line of text:'.format(n))
text = ''
for _ in range(n):
    text += input() + '\n'

print('There are {} different words.'.format(len(set(text.split()))))
