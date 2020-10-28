def encrypt_caesar(plaintext: str, shift: int = 3) -> str:

    ciphertext = ""
    for i in range(len(word)):
      for i in range(len(word)):
      if (word[i].isdigit())or(word[i]=='.'):
        ciphertext+=word[i]
      else:
        if word[i].islower():
            index=mal.index(word[i])
            if index==23:
                ciphertext+='a'
            if index==24:
                ciphertext+='b'
            if index==25:
                ciphertext+='c'
            if (index!=23)and(index!=24)and(index!=25):
                index=index+3
                ciphertext+=mal[index]
        else:
            index=zag.index(word[i])
            if index==23:
                ciphertext+='A'
            if index==24:
                ciphertext+='B'
            if index==25:
                ciphertext+='C'
            if (index!=23)and(index!=24)and(index!=25):
                index=index+3
                ciphertext+=zag[index]
        
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
 
    plaintext = ""
    for i in range(len(word)):
      if (word[i].isdigit())or(word[i]=='.'):
        plaintext+=word[i]
      else:
        if word[i].islower():
            index=mal.index(word[i])
            if index==0:
                plaintext+='x'
            if index==1:
                plaintext+='y'
            if index==2:
                plaintext+='z'
            if (index!=0)and(index!=1)and(index!=2):
                index=index-3
                plaintext+=mal[index]
        else:
            index=zag.index(word[i])
            if index==0:
                plaintext+='X'
            if index==1:
                plaintext+='Y'
            if index==2:
                plaintext+='Z'
            if (index!=0)and(index!=1)and(index!=2):
                index=index-3
                plaintext+=zag[index]
    return plaintext

mal=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
zag=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

ch=input('Зашифровать слово или расшифровать?')
word=input('Введите слово = ')
if (ch=='Зашифровать') or (ch=='зашифровать'):
   print(encrypt_caesar(word))
if (ch=='Расшифровать') or (ch=='расшифровать'):
    print(decrypt_caesar(word))
b=int(input('Если хотите воспользоваться программной снова, введите 1, иначе 0'))
while b==1:
    ch=input('Зашифровать слово или расшифровать?')
    word=input('Введите слово = ')
    if (ch=='Зашифровать') or (ch=='зашифровать'):
        print(encrypt_caesar(word))
    if (ch=='Расшифровать') or (ch=='расшифровать'):
        print(decrypt_caesar(word))
    b=int(input('Если хотите воспльзоваться программной снова, введите 1, иначе 0')) 
    


