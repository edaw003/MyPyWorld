import scapy.all as scapy


deg findMac(ip):
    arpReq = scapy.ARP(pdest=ip)
    arpBroad = scapy.Ether(dest="ff:ff:ff:ff:ff:ff")

    arpReqBroad = arpBroad/arpReq
    
