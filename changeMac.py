import subprocess as sp
import re

def showInterface():
    ifConfOut = str(sp.check_output(["ifconfig", "-a"]))
    inf = re.findall(r'\w*: ', ifConfOut,re.MULTILINE)
    newList = []
    for i in inf:
        newList.append(i.split(":")[0])
    return newList

def selectInt(intList):
    loopbkInt = 'lo'
    selection = False
    userInput = ''

    print("The interfaces that you can change are: ")
    
    for i in intList:
        if loopbkInt not in i:
            print ("-" + i) 

    while(not selection):
        userInput = input("Enter the interface that you want to change: ")
        
        if userInput in intList:
            print("Interface {} was selected.".format(userInput))
            selection = True
        else:
            print("Not a valid interface.")
 
    return userInput

def getMac(interface):
    ifConfOut = str(sp.check_output(["ifconfig", interface]))
    macAddr = re.findall(r'\w+:\w+:\w+:\w+:\w+:\w+', ifConfOut)
    macAddr = macAddr[0]

    return(macAddr)

def changeMac():
    validMac = False
    
    while(not validMac):
        newMac = input("Enter the new Mac address in format XX:XX:XX:XX:XX:XX : ")
        
        correctFormat = re.match(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", newMac)
        
        if(correctFormat):
            
    

if __name__ == "__main__":
    
    interfaces = showInterface()
    intToChange = selectInt(interfaces)
    
    print(getMac(intToChange))


