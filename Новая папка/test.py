from project import decrypt_vigner,encrypt_cezar,decrypt_cezar
  
def test_decrypt_vigner():
    assert encrypt_vygner('забег','шрйыжф' == 'пришел')
def test_encrypt_vigner():
    assert encrypt_vygner('забег','пришел' == 'шрйыжф')
def test_encode_atbash():
    assert  encode_atbash('aceg' == 'zwtr')
def test_encode_atbash():
    assert  encode_atbash('zwtr' == 'aceg')   
def test_encrypt_cezar(message,key):
    assert encrypt_vygner('место', 3 == 'пзфхс')
def test_decrypt_cezar(message,key):
    assert encrypt_vygner('пзфхс', 3 == 'место')
