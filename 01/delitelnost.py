def delitelnost(a, b):
    for i in range(100):
        if i % a == 0 or i % b == 0:
            print(f"Číslo {i} je dělitelné {a} nebo {b}.")
        

delitelnost(5, 6)