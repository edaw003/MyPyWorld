from socket import *
import time
import sys
import ipaddress

startTime = time.time()

if __name__ == '__main__':
    startIP = input('Enter start point of IP range: ')
    stopIP = input('Enter stop point of IP range: ')
    portToScan = int(input('Enter port: '))
    listIPs = []
    print("Start scanning...")
   
    startSearch = True
    while(startSearch):
        if(startIP > stopIP):
            startSearch = False
            break
        s = socket(AF_INET, SOCK_STREAM)
      
        
        conn = s.connect_ex((startIP, portToScan))
        if(conn == 0) :
            print (startIP + " with port " + str(portToScan) + " open.")
            s.close()
            listIPs.append(startIP)
        
        startIP = str(ipaddress.IPv4Address(startIP) + 1)
        print(".", end="")
    
    print("Search completed")
    print(listIPs)
      
      
                
            
            
    
    

