# Vi oppretter en teller 'i' og setter dens verdi til 0.
# Denne telleren vil bli brukt til å kontrollere løkkens progresjon.
i = 0

# Vi lagrer verdien 100 i variabelen 'n'.
# Dette vil være den øvre grensen for vår sjekk (ikke inkludert i utskriften).
n = 100

# Starter en 'while'-løkke. Denne løkken vil fortsette å kjøre så lenge betingelsen 'i < n' er sann.
# I dette tilfellet, så lenge 'i' er mindre enn 'n' (100).
while i < n:
    # Inne i løkken, sjekker vi om det nåværende tallet 'i' er et partall.
    # Dette gjøres ved å bruke modulusoperatoren '%'.
    # 'i % 2' returnerer resten når 'i' deles på 2.
    # Hvis resten er 0 (dvs. 'i % 2 == 0'), er 'i' et partall.
    if i % 2 == 0:
        # Hvis 'i' er et partall, skrives det ut.
        print(i)
    
    # Øker verdien av 'i' med 1.
    # Dette er viktig for å forhindre en uendelig løkke og for å gå videre til neste tall.
    i = i + 1

# Når 'i' blir 100, vil betingelsen 'i < n' ikke lenger være sann,
# og dermed avsluttes 'while'-løkken. 
# Resultatet er at alle partall fra 0 til 98 blir skrevet ut.
