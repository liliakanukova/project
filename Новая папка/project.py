"""
    Функция шифрует слова методом Цезаря .Для этого мы перебирая буквы исходного слова находим их индексы в алфавите и присваиваем переменной place, затем создаём новый индекс для зашифрованного текста , который будет равен сумме индекса исходной буквы и значению ключа key.Соединив послеовательно получившиеся буквы, мы получаем зашифрованное слово.
    
    :param message: это слово ,которое необходимо зашифровать
    :type message: str
    :param key: это ключ шифрования
    :type key: int
    
    :return: зашифрованное слово
    :rtype: str
 
    """
alfavit = 'абвгдеёжзийклмнопрстуфхцчшщьыьэюяабвгдеёжзийклмнопрстуфхцчшщьыьэюя'
def encrypt_cezar(message,key):
       itog = ''
       for i in message:
              place = alfavit.find(i)   # Алгоритм для шифрования сообщения на русском 
              new_place = place + key
              if i in alfavit:
                     itog += alfavit[new_place]
              else:
                     itog += i
       return itog
"""
    Функция шифрует слова методом Цезаря .Для этого мы перебирая буквы зашифрованного слова находим их индексы в алфавите и присваиваем переменной place, затем создаём новый индекс для дешифрованного текста , который будет равен разности индекса зашифроованной буквы и значения ключа key.Соединив послеовательно получившиеся буквы, мы получаем расшифрованное слово.
    
    :param message: это слово ,которое необходимо расшифровать
    :type message: str
    :param key: это ключ шифрования
    :type key: int
    
    :return: расшифрованное слово
    :rtype: str
 
    """
def decrypt_cezar(message,key):
       itog = ''
       for i in message:
               place = alfavit.find(i)    
               prev_place = place - key    
               if i in alfavit:
                   itog += alfavit[prev_place]
               else:
                   itog += i 
       return itog
alpha = ["abcdefghijklnopqrstvwyz"]
def encode_atbash(plain_text):
       for i,y in enumerate(alpha):
              for u in y:
                     list_e = u
       list_d = sorted(list_e, reverse=True)
       for i in plain_text:
              for z,y in enumerate(list_e):
                     if i == y:
                            text = list_d[z]
       encoded_text = ""
       for i in text:
              encoded_text += i
       return encoded_text


def decode_atbash(ciphered_text):
    for i,y in enumerate(alpha):
              for u in y:
                     list_e = u
    list_d = sorted(list_e, reverse=True)
    for i in ciphered_text :
           for z,y in enumerate(list_e):
                  if i == y:
                         text = list_d[z]    

    decoded_text = ""
    for i in text:
           decoded_text += i
    return decoded_text
import random
def encrypt_perest(text, key):
    """
    Функция шифрует текстовое сообщение методом перестановок.Для этого она проверяет делится ли сообщение на ключ шифрования, и если нет, то добиваем рандомными буквами текст так чтобы длина текста делилась на длину ключа,а затем создаём новое зашифрованное сообщение ,которое формируется с помощью key
    
    :param text: это сообщение ,которое необходимо зашиaровать
    :type text: str
    :param key: это ключ шифрования
    :type key: list
    
    :return: зашифрованное сообщение
    :rtype: str
 
    """
    n = len(text)
    m = len(key)
    d = n % m 
    if d != 0:
        for i in range(m - d):
            text += chr(random.randrange(ord('а'), ord('я'), 1))
        n = len(text)
    p = ''
    q = 0
    while q < n:
        p += ''.join(text[q+x] for x in key)
        q += m
 
    return p


print(decode('вбкутаут', [3, 0, 2, 1])) 
#Функция дешифрования кода с помощью перестановки permutation
def decrypt_perest(text, key):
    blockSize = len(key)
    codeSize = len(text)
   #Дешифрование
    for i in range(0, codeSize, blockSize):
        string = [ text[i+j] for j in key]
        for j in range(blockSize):
            text[i + j] = string[j]
    return string
alphabeth= 'abcdefghijklmnopqrstuvwxyz'
def encrypt_gammir(text, gamma):
    textLen = len(text)
    gammaLen = len(gamma)

    #Формируем ключевое слово(растягиваем гамму на длину текста)
    keyText = []
    for i in range(textLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(textLen % gammaLen):
        keyText.append(gamma[i])

    #Шифрование
    code = []
    for i in range(textLen):
        code.append(alphabeth[(alphabeth.index(text[i]) + alphabeth.index(keyText[i])) % 26])

    return code
print(encrypt_gammir('hello','jk'))
alphabeth = "abcdefghijklmnopqrstuvwxyz"
def decrypt_gammir(code, gamma):
    codeLen = len(code)
    gammaLen = len(gamma)
    #Формируем ключевое слово(растягиваем гамму на длину текста)
    keyText = []
    for i in range(codeLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(codeLen % gammaLen):
        keyText.append(gamma[i])
    #Расшифровка
    text = []
    for i in range(codeLen):
        text.append(alphabeth[(alphabeth.index(code[i]) - alphabeth.index(keyText[i]) + 26) % 26]) 

    return text
"""
    Функция шифрует русские слова методом Вижнера.Для этого мы берём переменную и записываем туда индекс символа,затем находим индекс остатка от деления индекса буквы в слове на длину key и записывает в другую переменную,затем эти переменные складываются и остаток от деления суммы на длину алфавита присваивается индексу зашифрованной буквы.После последовательное выполнение аналогичных действий с оставшимися буквами исходного слова мы получаем зашифрованное значение.
    
    
    :param text: это слово ,которое необходимо зашифровать
    :type text: str
    :param key: это ключ шифрования
    :type key: str 
    
    :return: зашифрованное слово
    :rtype: str
 
    """
tabula_recta = 'абвгдеоеёжзийклмнопрстуфхцчшщийъыьэюя'
def encrypt_vygner(key, text):
    result = []
    space = 0
    for i, char in enumerate(text):
        if char != ' ':
            mj = tabula_recta.index(char)
            kj = tabula_recta.index(key[(i - space) % len(key)])
            cj = (mj + kj) % len(tabula_recta)
            result.append(tabula_recta[cj])
        else:
            space += 1
            result.append(' ')
    return ''.join(result)
"""
    Функция дешифрует русские слова ,которые были зашифрованы методом Вижнера.Для этого мы смотрим на индекс зашифрованной буквы и записываем её в отдельную переменную ,затем находим индекс остатка от деления индекса буквы в слове на длину key и записывает в другую переменную, остаток от деления разности этих двух переменных на длину алфавита присваиваем индексу дешифрованной буквы в алфавите.После последовательное выполнение аналогичных действий с оставшимися буквами зашифрованного слова мы получаем дешифрованное значение.
    
    :param text: это слово ,которое необходимо дешифровать
    :type text: str
    :param key: это ключ шифрования
    :type key: str 
    
    :return: дешифрованное слово
    :rtype: str
 
    """
def decrypt_vigner(key, text):
    result = []
    space = 0
    for i, char in enumerate(text):
        if char != ' ':
            cj = tabula_recta.index(char)
            kj = tabula_recta.index(key[(i - space) % len(key)])
            mj = (cj - kj) % len(tabula_recta)
            result.append(tabula_recta[mj])
        else:
            space += 1
            result.append(' ')
    return ''.join(result)

