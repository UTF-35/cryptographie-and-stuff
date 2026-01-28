import socket

cible = "127.0.0.1" # a changer celon la cible 
ports = [21, 22, 80, 443, 3306]

for p in ports:
    testeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    testeur.settimeout(0.5)
    truc = testeur.connect_ex((cible, p))
    if truc == 0:
        print(f"Port {p} est ouvert") #indique la que les ports que ta mis dans la variable ports sont ouvert
    else:
        pass
    testeur.close()