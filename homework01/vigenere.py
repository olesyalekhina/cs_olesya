def encrypt_vigenere(plaintext: str, keyword: str) -> str:

    ciphertext =""
    n=key
    while len(n)<len(word):
            n+=n
    for i in range(len(word)):
        index_key=mal.index(n[i])
        if word[i].islower():
            index=mal.index(word[i])
            if index+index_key<26:
                index+=index_key
                ciphertext+=mal[index]
            else:
                index=index+index_key-26
                ciphertext+=mal[index]
        else:
            index=zag.index(word[i])
            if index+index_key<26:
                index+=index_key
                ciphertext+=zag[index]
            else:
                index=index+index_key-26
                ciphertext+=zag[index]
        
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
 
    plaintext = ""
    n=key
    while len(n)<len(word):
            n+=n
    for i in range(len(word)):
        index_key=mal.index(n[i])
        if word[i].islower():
            index=mal.index(word[i])
            if index-index_key>=0:
                index-=index_key
                plaintext+=mal[index]
            else:
                index=index-index_key+26
                plaintext+=mal[index]
        else:
            index=zag.index(word[i])
            if index+index_key>=0:
                index-=index_key
                plaintext+=zag[index]
            else:
                index=index-index_key+26
                plaintext+=zag[index]
    return plaintext

mal=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
zag=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

ch=input('Зашифровать слово или расшифровать?')
word=input('Введите слово = ')
key=input('Введите слово-ключ = ')
if (ch=='Зашифровать') or (ch=='зашифровать'):
   key=key.lower()
   print(encrypt_vigenere(word,key))
if (ch=='Расшифровать') or (ch=='расшифровать'):
    key=key.lower()
    print(decrypt_vigenere(word,key))
b=int(input('Если хотите воспользоваться программной снова, введите 1, иначе 0'))
while b==1:
    ch=input('Зашифровать слово или расшифровать?')
    word=input('Введите слово = ')
    key=input('Введите слово-ключ = ')
    if (ch=='Зашифровать') or (ch=='зашифровать'):
        key=key.lower()
        print(encrypt_vigenere(word,key))
    if (ch=='Расшифровать') or (ch=='расшифровать'):
        key=key.lower()
        print(decrypt_vigenere(word,key))
    b=int(input('Если хотите воспльзоваться программной снова, введите 1, иначе 0')) 
    



