def encrypt_vigenere(plaintext: str, keyword: str) -> str:

    ciphertext =""
    mal=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    zag=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    n=keyword
    while len(n)<len(plaintext):
            n+=n
    for i in range(len(plaintext)):
      if plaintext[i]==' ':
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
    mal=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    zag=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    n=keyword
    while len(n)<len(ciphertext):
            n+=n
    for i in range(len(ciphertext)):
      if ciphertext[i]==' ':
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





