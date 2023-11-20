# Setter verdien av 'n' til 100. Dette vil være den øvre grensen for vår rekkevidde.
n = 100

# Starter en 'for'-løkke som itererer over en sekvens av tall.
# 'range(n)' genererer en sekvens fra 0 til n-1 (her: 0 til 99).
# Variabelen 'i' vil ta hver verdi i denne sekvensen, en etter en, for hver iterasjon.
for i in range(n):
    # Inne i løkken, sjekker vi om det nåværende tallet 'i' er et partall.
    # Dette gjøres ved å bruke modulusoperatoren '%'.
    # 'i % 2' returnerer resten når 'i' deles på 2.
    # Hvis resten er 0 (dvs. 'i % 2 == 0'), er 'i' et partall.
    if i % 2 == 0:
        # Hvis 'i' er et partall, skrives det ut.
        print(i)

# Resultatet av denne koden vil være at alle partall fra 0 til 98 skrives ut.
# Dette inkluderer 0 (som er et partall) og ekskluderer 100, siden range går til n-1.
