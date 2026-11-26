# H-1

age = int(input("Yoshingizni kiriting: "))
if age>= 18:
    print("Siz voyaga yetgansiz!")
else:
    print("Siz voyaga yetmagansiz!")

# H-2

parol = "python123"
parol_soraw = input("Parolni kiriting: ")
if parol == parol_soraw:
    print("Xosh keldiniz!")
else:
    print("Parol naduris!")

# H-3

onim_bahasi = int(input("Mahsulot narxini kiriting: "))
if onim_bahasi > 500000:
    chegirma = onim_bahasi * 0.10
    jami_baha = onim_bahasi - chegirma
    print(f"chegirma: {chegirma} sum")
    print(f"Yakuniy narx: {jami_baha} sum")
else:
    print("chegirma yoq!")

# H-5
jetkerip_beriw = 15000
buyirtpa_bahasi = int(input("Buyirtpa bahasi qansha?: "))
if buyirtpa_bahasi > 100000:
    print("Jetkeziw biypul!")
else:
    print("Jetkerip beriw:",jetkerip_beriw,"sum")
    print("Jami tolem:",jetkerip_beriw + buyirtpa_bahasi,"sum")

# H-6
ball = int(input("Ballingizni kiriting: "))
if 90<= ball <= 100:
    print("Sizning bahoyingiz: A'lo")
elif 75<= ball <=89:
    print("Sizning bahoyingiz: Yaxshi")
elif 60<= ball <=74:
    print("Sizning bahoyingiz: Qoniqarli")
elif 0<= ball <=59:
    print("Sizning bahoyingiz: Qoniqarsiz")


# H-8

mevalar = ["olma","banan","uzum","anor","shaftoli"]
sorash = input("Meva nomin kiriting: ")
if sorash in mevalar:
    print(sorash,"royxatda mavjud!")
else:
    print(sorash,"royxatda mavjud emas!")


# H-9
oquvchilar = ["Ali","Vali","Sardor","Malika","Madina"]
sorash = input("Ism kiriting: ")
if sorash in oquvchilar:
    print(sorash,"royxatda mavjud!")
    print("Birinchi harf:",sorash[0])
else:
    print("Royxatda mavjud emas!")

# H-11

numbers = [2,5,8,11,14,17]
for i in range(len(numbers)):
    if numbers[i] < 10:
        numbers[i] = numbers[i] * 2
    else:
        numbers[i] = numbers[i] + 5

print(numbers)

# H-13

products = ["Non","Sut","Gosht","Olma","Banan"]
prices = [4000,12000,90000,8000,15000]
onim = input("Qanday mahsulot olmoqchisiz?: ")

if i in range(len(products)):
    if products[i].lower() == onim.lower():
       qansha_kerak = int(input(onim + " qancha kerak?: "))
       total = prices[i] * qansha_kerak
       print("Umumiy summa:",total,"sum")
    else:
        print("Bunday mahsulot yoq!")


