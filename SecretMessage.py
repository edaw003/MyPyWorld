def alphabetList():
    alphaList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ','!',
 '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', '<', ',', '>', '.', '?', '`' ,'~']

    return alphaList


def keyAndMsg():
    key2EncodeIndex = []
    msg2EncodeIndex = []
    
    key2Encode = input("Enter key: ")
    msg2Encode = input("Enter message: ").lower()
    
    key2Encode = (key2Encode * (len(msg2Encode)//len(key2Encode) + 1))[:len(msg2Encode)]
      
    
    for i in key2Encode:
        key2EncodeIndex.append(alphabetList().index(i))
    

    for i in msg2Encode:
        msg2EncodeIndex.append(alphabetList().index(i))

    return key2EncodeIndex, msg2EncodeIndex

def keyAndCodedMsg():
    key2Decodeindex = []
    
    key2Decode = input("Enter key: ")
    msg2Decode = input("Enter message: ")
    
    key2Decode = (key2Decode * (len(msg2Decode)//len(key2Decode) + 1))[:len(msg2Decode)]
    
    for i in key2Decode:
        key2Decodeindex.append(alphabetList().index(i))
        
    return key2Decodeindex, msg2Decode

def userOpt():
    
    preference = True
    
    while(preference):
        userOption = input("Do you what to encode or de code a message.\n Write 'd' if you uant to decode or 'e' if you want to encode: ")
        
        if(userOption.lower() == 'd'):
            print("You have selected to decode a message")
            keyUserOpt, msgUserOpt = keyAndCodedMsg()
            
            decode(keyUserOpt, msgUserOpt)
            
            preference = False
            
        elif(userOption.lower() == 'e'):
            print("You have selected to encode a message")
            keyUserOpt, msgUserOpt = keyAndMsg()
            
            encode(keyUserOpt, msgUserOpt)
            
            preference = False
            
        else:
            print("Invalid OPTION selected!")
            

def encode(keyMsgIndex, encodeMsgIndex):
    codedmsg = ''
    
    for i in range(len(encodeMsgIndex)):
        result = keyMsgIndex[i] + encodeMsgIndex[i]
    
        codedmsg = codedmsg + alphabetList()[result]
    
    print(codedmsg)
    
def decode(keyMsgIndex, decodeMsg):
    decodemsg = ''
    indexJ = 0
    
    for i in decodeMsg:
        decodemsg = decodemsg + (alphabetList()[alphabetList().index(i) - keyMsgIndex[indexJ]])
        indexJ += 1
        
    print(decodemsg)
    
    

if __name__ == "__main__":
    
    userOpt()
    
    
            
        
    

