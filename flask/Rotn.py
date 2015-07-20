def rotn(hello, number):
    i = 0
    numChar = 0
    word = ""
    for i in range (len(hello)):
        if (ord(hello[i]) >=65 and ord(hello[i]))<=90:
            numChar = ord(hello[i]) + (97-65)
        else:
            numChar = ord(hello[i])
        if (numChar >=97 and numChar <= 122):  
            if (numChar + number > 122):
                numChar = 96 + (numChar + number)- 122
            else:
                numChar += number
        word += chr(numChar)
    print word
    return word
print rotn("hello",13)




