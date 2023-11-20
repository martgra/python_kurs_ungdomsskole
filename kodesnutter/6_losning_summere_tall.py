# Vi oppretter en variabel kalt "total" og setter verdien til 0
total = 0

# Vi oppretter en variabel "n" som sier hvor mange tall vi ønsker å legge sammen
n = 100

# Vi lager en for-løkke som skal "gjenta" en operasjon "n" ganger. Varibelen "i" holder styr på hvor vi er. 
for i in range(n):
    total = total + i

# Vi skriver ut totalen
print(total)