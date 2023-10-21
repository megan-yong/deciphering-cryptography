### The Caesar Cipher ###

alphabets = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!?.':, " #includes a space as punctuation

def caesar_decoder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabets.find(letter)
            translated_message += alphabets[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message
    
def caesar_coder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabets.find(letter)
            translated_message += alphabets[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message


## With offset of 10 

message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
# output of `decoder` for the first message with an offset of 10

print(decoder(message_one, 10))
# the offset for the second message is fourteen.

message_two = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
print(decoder(message_two, 14))
# performing multiple caesar ciphers to code your messages is even more secure!


## With unknown shift value

message_three = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# try all 26 different shifts
for i in range(1,26):
    print("offset: " + str(i))
    print("\t " + decoder(message_three, i) + "\n")

# offset: 1 wigjonylm bupy lyhxylyx uff iz nbymy ifx wcjbylm um ivmifyny. qy'ff bupy ni lyuffs mnyj oj iol augy cz qy quhn ni eyyj iol gymmuaym muzy.  
# offset: 2 xjhkpozmn cvqz mziyzmzy vgg ja ocznz jgy xdkczmn vn jwnjgzoz. rz'gg cvqz oj mzvggt nozk pk jpm bvhz da rz rvio oj fzzk jpm hznnvbzn nvaz.  
# offset: 3 ykilqpano dwra najzanaz whh kb pdaoa khz yeldano wo kxokhapa. sa'hh dwra pk nawhhu opal ql kqn cwia eb sa swjp pk gaal kqn iaoowcao owba.  
# offset: 4 zljmrqbop exsb obkaboba xii lc qebpb lia zfmebop xp lyplibqb. tb'ii exsb ql obxiiv pqbm rm lro dxjb fc tb txkq ql hbbm lro jbppxdbp pxcb.  
# offset: 5 amknsrcpq fytc pclbcpcb yjj md rfcqc mjb agnfcpq yq mzqmjcrc. uc'jj fytc rm pcyjjw qrcn sn msp eykc gd uc uylr rm iccn msp kcqqyecq qydc.  
# offset: 6 bnlotsdqr gzud qdmcdqdc zkk ne sgdrd nkc bhogdqr zr narnkdsd. vd'kk gzud sn qdzkkx rsdo to ntq fzld he vd vzms sn jddo ntq ldrrzfdr rzed.  
# offset: 7 computers have rendered all of these old ciphers as obsolete. we'll have to really step up our game if we want to keep our messages safe.  
# ...
# offset: 25 ugehmlwjk zsnw jwfvwjwv sdd gx lzwkw gdv uahzwjk sk gtkgdwlw. ow'dd zsnw lg jwsddq klwh mh gmj ysew ax ow osfl lg cwwh gmj ewkksywk ksxw. 