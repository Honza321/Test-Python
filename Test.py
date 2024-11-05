print("Vítejte v programu na výpočet ohmova zákona")
while (1):
    print("1. Vypočítejte napětí")
    print("2. Vypočítejte proud")
    print("3. Vypočítejte odpor")
    print("4. Ukončete program")

        

    ask = input("> ")
    if (ask == "1"):
        print("-- Napětí --")
        i = float(input("Odpor: "))
        r = float(input("Proud: "))
        v = i * r
        print("Napětí = V", format(v, ".2f"))

    elif(ask == "2"):
        print("-- Proud --")
        v = float(input("Napětí: "))
        i = float(input("Odpor: "))
        r = v / i
        print("Proud = A", format(v, ".2f"))

    elif(ask == "3"):
        print("-- Odpor --")
        v = float(input("Napětí: "))
        r = float(input("Proud: "))
        i = v / r
        print("Odpor = Ω", format(v, ".2f"))

    elif(ask == "4"):
        break
    else:
        print("Toto není správná možnost, zkus to znovu")




  
 
    
    

    


