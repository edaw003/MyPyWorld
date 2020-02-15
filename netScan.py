import scapy.all as scapy
import datetime


def findMac(ip):
    arpReq = scapy.ARP(pdst=ip) # create ARP request
    macFile = open("macTrace.txt","a+")    
    currentDate = str(datetime.datetime.now())

    #print(arpReq.summary())
    #scapy.ls(scapy.ARP())

    arpBroad = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # create Ethernet object
    #print(arpBroad.summary())
    #scapy.ls(scapy.Ether())

    arpReqBroad = arpBroad/arpReq

    #arpReqBroad.show()
    answ, unasnw = scapy.srp(arpReqBroad, timeout=1)

    macFile.write("IP \t MAC\t\t {} \n".format(currentDate) )
    for i in answ:
        print(i[1].psrc + " " + i[1].hwdst)
        macFile.write(i[1].psrc + " " + i[1].hwdst +"\n")

    macFile.close()

def countMac():
    openFile = open("macTrace.txt","r")
    outputFile = openFile.read()
    openFile.close()
    countMac = dict()

    macAddr = re.findall(r'\w+:\w+:\w+:\w+:\w+:\w+', outputFile)
    
    for i in macAddr:
        if i in countMac:
            countMac[i] +=1
        else:
            countMac[i] = 1

    print(countMac)
    for j in countMac:
        print("MAC : {} , Nr : {}".format(j,countMac[j]))

if __name__ == "__main__":
    ipAddr = input("Enter the IP addreass or to search a range of IP address use IP/Netmask (ex: 10.0.2.1/24)")
    findMac(ipAddr)

    countMac()
    