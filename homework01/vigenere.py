def encrypt_vigenere(plaintext: str, keyword: str) -> str:

    ciphertext =""
    keyword=keyword.lower()
    mal=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    zag=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    n=keyword
    while len(n)<len(plaintext):
            n+=n
    for i in range(len(plaintext)):
     lr=0
     for j in range(26):
      if palintext[i]==mal[j]:
       lr=1
     for j in range(26):
      if palintext[i]==zag[j]:
       lr=1
     if lr==0:
      ciphertext+=plaintext[i]
     else:
        index_key=mal.index(n[i])
        if plaintext[i].islower():
            index=mal.index(plaintext[i])
            if index+index_key<26:
                index+=index_key
                ciphertext+=mal[index]
            else:
                index=index+index_key-26
                ciphertext+=mal[index]
        else:
            index=zag.index(plaintext[i])
            if index+index_key<26:
                index+=index_key
                ciphertext+=zag[index]
            else:
                index=index+index_key-26
                ciphertext+=zag[index]
        
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
 
    plaintext = ""
    keyword=keyword.lower()
    mal=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    zag=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    n=keyword
    while len(n)<len(ciphertext):
            n+=n
    for i in range(len(ciphertext)):
     lr=0
     for j in range(26):
      if ciphertext[i]==mal[j]:
       lr=1
     for j in range(26):
      if ciphertext[i]==zag[j]:
       lr=1
     if lr==0:
      plaintext+=ciphertext[i]
     else:
        index_key=mal.index(n[i])
        if ciphertext[i].islower():
            index=mal.index(ciphertext[i])
            if index-index_key>=0:
                index-=index_key
                plaintext+=mal[index]
            else:
                index=index-index_key+26
                plaintext+=mal[index]
        else:
            index=zag.index(ciphertext[i])
            if index+index_key>=0:
                index-=index_key
                plaintext+=zag[index]
            else:
                index=index-index_key+26
                plaintext+=zag[index]
    return plaintext





