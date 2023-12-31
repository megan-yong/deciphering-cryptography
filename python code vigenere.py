### The Vigenère Cipher ###

def vigenere_decoder(coded_message, keyword):
    letter_pointer = 0
    keyword_final = ""
    for i in range(0,len(coded_message)):
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ""
    for i in range(0,len(coded_message)):    
        if not coded_message[i] in punctuation:
            ln = alphabets.find(coded_message[i]) - alphabets.find(keyword_final[i])
            translated_message += alphabets[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message

message_four = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

print(vigenere_decoder(message_four, keyword))
# you were able to decode this? nice work! you are becoming quite the expert at crytography!


def vigenere_coder(message, keyword):
    letter_pointer = 0
    keyword_final = ""
    for i in range(0,len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ""
    for i in range(0,len(message)):
        if message[i] not in punctuation:
            ln = alphabets.find(message[i]) + alphabets.find(keyword_final[i])
            translated_message += alphabets[ln % 26]
        else:
            translated_message += message[i]
    return translated_message

message_five = "learning so many great ciphers with python!"
keyword = "thanks"

print(vigenere_coder(message_five,keyword))
print(vigenere_decoder(vigenere_coder(message_five, keyword), keyword))
# elaexagn sb wsgf geosm jicrwkz wvdz iftuyf!
# learning so many great ciphers with python!