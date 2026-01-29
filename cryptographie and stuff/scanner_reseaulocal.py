from scapy.all import ARP, Ether, srp

cible = "x.x.x.x" # ipv4 de ton reseau ou autre ....
paquet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=cible)

reponse = srp(paquet, timeout=2, verbose=0)[0]

for envoyé, reçu in reponse:
    print(f"IP: {reçu.psrc} | MAC: {reçu.hwsrc}")
