from colorama import Fore,init
init()

while True:
    weight = int(input("Enter Your Weight [eg. 67] : "))
    height = float(input("Enter Your Height [eg. 1.8] : "))

    bmi = weight / height ** 2

    if bmi < 18.5 :
        print(Fore.LIGHTBLUE_EX + "\nUnder - Weight\n" + Fore.WHITE)
    elif bmi >= 18.5 and bmi < 25 :
        print(Fore.LIGHTGREEN_EX + "\nNormal Status\n" + Fore.WHITE)
    elif bmi >= 25 and bmi < 30 :
        print(Fore.LIGHTYELLOW_EX + "\nOver - Weight\n" + Fore.WHITE)
    elif bmi >= 30 :
        print(Fore.LIGHTRED_EX + "\nObesity Status !\n" + Fore.WHITE)
    elif weight or height == "exit":
        break
    else:
        print("Error")