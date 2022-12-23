alfavit = 'абвгдеёжзийклмнопрстуфхцчшщьыьэюяабвгдеёжзийклмнопрстуфхцчшщьыьэюя'
def encrypt_cezar(message,key):
       """
           Функция шифрует слова методом Цезаря .Для этого мы перебирая буквы исходного слова находим их индексы в алфавите и присваиваем переменной place, затем создаём новый индекс для зашифрованного текста , который будет равен сумме индекса исходной буквы и значению ключа key.Соединив послеовательно получившиеся буквы, мы получаем зашифрованное слово.
           
           :param message: это слово ,которое необходимо зашифровать
           :type message: str
           :param key: это ключ шифрования
           :type key: int
           
           :return: зашифрованное слово
           :rtype: str
        
    """       
       itog = ''
       for i in message:
              place = alfavit.find(i)   # Алгоритм для шифрования сообщения на русском 
              new_place = place + key
              if i in alfavit:
                     itog += alfavit[new_place]
              else:
                     itog += i
       return itog

def decrypt_cezar(message,key):
       """
           Функция шифрует слова методом Цезаря .Для этого мы перебирая буквы зашифрованного слова находим их индексы в алфавите и присваиваем переменной place, затем создаём новый индекс для дешифрованного текста , который будет равен разности индекса зашифроованной буквы и значения ключа key.Соединив послеовательно получившиеся буквы, мы получаем расшифрованное слово.
           
           :param message: это слово ,которое необходимо расшифровать
           :type message: str
           :param key: это ключ шифрования
           :type key: int
           
           :return: расшифрованное слово
           :rtype: str
        
    """       
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
       """
            Функция шифрует слова методом Атбаш.Шифрование заключается в замене каждой буквы исходного текста на «симметричную» ей букву алфавита.И возвращает зашифрованный текст
           
           :param plain_text: это текст, который необходимо зашифровать
           :type plain_text: str
           
           :return: зашифрованное слово
           :rtype: str
        
    """       
     
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
       """
            Функция дешифрует слова методом Атбаш.Дешифрование заключается в замене каждой буквы зашифрованного текста на «симметричную» ей букву алфавита.И возвращает зашифрованный текст
           
           :param ciphered_text: это текст, который необходимо расшифровать
           :type ciphered_text: str
           
           :return: расшифрованное слово
           :rtype: str
        
    """       
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


tabula_recta = 'абвгдеоеёжзийклмнопрстуфхцчшщийъыьэюя'
def encrypt_vygner(key, text):
       """
           Функция шифрует русские слова методом Вижнера.Для этого мы берём переменную и записываем туда индекс символа,затем находим индекс остатка от деления индекса буквы в слове на длину key и записывает в другую переменную,затем эти переменные складываются и остаток от деления суммы на длину алфавита присваивается индексу зашифрованной буквы.После последовательное выполнение аналогичных действий с оставшимися буквами исходного слова мы получаем зашифрованное значение.
           
           
           :param text: это слово ,которое необходимо зашифровать
           :type text: str
           :param key: это ключ шифрования
           :type key: str 
           
           :return: зашифрованное слово
           :rtype: str
        
    """       
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

def decrypt_vigner(key, text):
       """
           Функция дешифрует русские слова ,которые были зашифрованы методом Вижнера.Для этого мы смотрим на индекс зашифрованной буквы и записываем её в отдельную переменную ,затем находим индекс остатка от деления индекса буквы в слове на длину key и записывает в другую переменную, остаток от деления разности этих двух переменных на длину алфавита присваиваем индексу дешифрованной буквы в алфавите.После последовательное выполнение аналогичных действий с оставшимися буквами зашифрованного слова мы получаем дешифрованное значение.
           
           :param text: это слово ,которое необходимо дешифровать
           :type text: str
           :param key: это ключ шифрования
           :type key: str 
           
           :return: дешифрованное слово
           :rtype: str
        
    """       
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


import string
def encode_kod_word(word,codeword):
       """
           Функция зашифровывает слова методом кодового слова .
           
           :param word: это слово ,которое необходимо дешифровать
           :type word: str
           :param codeword: это ключевое слово
           :type key: str 
           
           :return: зашифрованное слово
           :rtype: str
        
    """       
       alphabet = string.ascii_lowercase  # латинский алфавит
       for x in alphabet:
              if x not in codeword:
                     new_alphabet = codeword + ''.join([x])
       dct = dict(zip(alphabet, new_alphabet))  # словарь замены символов
       new_word = ''.join(map(dct.get, word))
       return new_word
