def encrypt_caesar(plaintext: str, shift: int = 3) -> str:

 ciphertext = ""
 mal=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 zag=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 while shift>=26:
     shift-=26
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
         if plaintext[i].islower():
             index=mal.index(plaintext[i])
             if index+shift<26:
                index+=shift
                ciphertext+=mal[index]
             else:
                index=index+shift-26
                ciphertext+=mal[index]      
         else:
                index=zag.index(plaintext[i])
                if index+shift<26:
                  index+=shift
                  ciphertext+=zag[index]
                else:
                   index=index+shift-26
                   ciphertext+=zag[index]

        
 return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
 
 plaintext = ""
 mal=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 zag=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 while shift>=26:
     shift-=26
 for i in range(len(ciphertext)):
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
             if ciphertext[i].islower():
                index=mal.index(ciphertext[i])
                if index-shift>=0:
                    index-=shift
                    plaintext+=mal[index]
                else:
                    index=index-shift+26
                    plaintext+=mal[index]      
             else:
                 index=zag.index(ciphertext[i])
                 if index-shift>=0:
                    index-=shift
                    plaintext+=zag[index]
                 else:
                   index=index-shift+26
                   plaintext+=zag[index]

 return plaintext






