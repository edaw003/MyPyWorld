import scapy.all as scapy


def findMac(ip):
    arpReq = scapy.ARP(pdst=ip) # create ARP request
    
    #print(arpReq.summary())
    #scapy.ls(scapy.ARP())

    arpBroad = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # create Ethernet object
    #print(arpBroad.summary())
    #scapy.ls(scapy.Ether())

    arpReqBroad = arpBroad/arpReq

    #arpReqBroad.show()
    answ, unasnw = scapy.srp(arpReqBroad, timeout=1)
    print(answ.summary())

findMac("10.0.2.1/24")