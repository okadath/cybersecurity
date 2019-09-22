#!/usr/bin/env python
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr
import sys
net=".".join(sys.argv[1].split(".")[:-1])+"."
for x in range(int(sys.argv[2].split(".")[-1]),int(sys.argv[3].split(".")[-1])+1):
	a,b=sr(IP(dst=net+str(x))/ICMP(),timeout=6,verbose=False)
	#si a esta vacio es que no hubo respuestas del host
	print(net+str(x)+": Host no accesible") if (not a) else print(net+str(x)+": Host encontrado") 
