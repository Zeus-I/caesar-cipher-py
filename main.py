def cipher():
    pt = [*text]
    nil = ""
    j = 0
    for i in text:
        if i == " ":
            pt[j] = " " 
            j = j+1
        elif i.isdigit() == True:
            pt[j] = i
            j = j+1
        elif i.isalpha() == True:
            alp_pos = alphabets.rfind(i)
            key_pos = alp_pos + key
            if key_pos > 25:
                key_pos = key_pos - 26
                pt[j] = alphabets[key_pos]
                j = j+1
            else:    
                pt[j] = alphabets[key_pos]
                j = j+1
        else:
            pt[j] = i
            j = j+1
    print("\nYour ciphered message is: " + nil.join(pt))

def decipher():
    ct = [*text]
    nil = ""
    j = 0
    for i in text:
        if i == " ":
            ct[j] = " "
            j = j+1
        elif i.isdigit() == True:
            ct[j] = i
            j = j+1
        elif i.isalpha() == True:
            alp_pos = alphabets.rfind(i)
            key_pos = alp_pos - key
            if key_pos < 0:
                key_pos = key_pos + 26
                ct[j] = alphabets[key_pos]
                j = j+1
            else:    
                ct[j] = alphabets[key_pos]
                j = j+1
        else:
            ct[j] = i
            j = j+1
    print("\nYour original message is: " + nil.join(ct))

alphabets = "abcdefghijklmnopqrstuvwxyz" 




print("""
  ______________________________
 / \                             \.
|   |                            |.
 \_ |                            |.
    |                            |.
    |         Caesar             |.
    |                            |.
    |              Cipher        |.
    |                            |.
    |                            |.
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/____________________________/.
\n\n""")
text = (input("Enter your message: \n")).lower()
key= int(input("\nEnter secret key between 1-10: \n"))
if key > 0 and key <=10:
    choice = int(input("\nEnter 1 to Cipher or 2 to Decipher: \n"))
    if choice == 1:
        cipher()
    elif choice == 2:
        decipher()
    else:
        print("\nInvalid Input!!! Please Enter only '1' or '2'\n")
else:
    print("\nInvalid Input!!! Please choose a key between 1 and 10")