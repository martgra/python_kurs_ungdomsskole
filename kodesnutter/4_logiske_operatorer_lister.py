# Vi ber brukeren om å skrive inn sitt navn.
# 'input()' funksjonen lar brukeren skrive inn en tekststreng.
# Denne teksten blir så lagret i variabelen 'navn'.
navn = input("Skriv inn navnet ditt: ")

# Vi oppretter en variabel 'rolle' og initialiserer den med en tom tekststreng.
# Denne variabelen vil senere bli brukt til å lagre rollen til personen.
rolle = ""

# Her oppretter vi lister med kjente navn for ulike roller.
larere = ["Terje", "Espen", "Anders", "Helene", "Tone"]
foredragsholdere = ["Martin", "Petter"]

# Vi bruker en if-elif-else struktur for å bestemme rollen til personen basert på navnet de oppga.
# Vi bruker "in" operatoren til å sjekke om navnet er i en av listene.
if navn in larere:
    # Hvis navnet er i lærerlisten, settes rollen til "lærer".
    rolle = "lærer"
elif navn in foredragsholdere:
    # Hvis navnet er i foredragsholderlisten, settes rollen til "foredragsholder".
    rolle = "foredragsholder"
else:
    # Hvis navnet ikke er i noen av listene, settes rollen til "ukjent".
    rolle = "ukjent"

# Vi skriver ut rollen til personen.
# Tekststrenger kan kombineres (konkateneres) ved å bruke '+' operatoren.
print("Rollen til personen er: " + rolle)
