import random


sifre = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("lütfen şifrenizin uzunluğunu giriniz: "))

parola = ""

for i in range(uzunluk):
    parola += random.choice(sifre)




print(parola)
