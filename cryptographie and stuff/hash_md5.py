import hashlib

fichier = "tonimage.jpg" 
h = hashlib.md5()

with open(fichier, "rb") as f:
    h.update(f.read())

print(h.hexdigest())
