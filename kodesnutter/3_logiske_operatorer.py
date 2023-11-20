# Vi ber brukeren om å skrive inn sitt navn.
# 'input()' funksjonen lar brukeren skrive inn en tekststreng.
# Denne teksten blir så lagret i variabelen 'navn'.
navn = input("Skriv inn navnet ditt: ")

# Vi oppretter en variabel 'rolle' og initialiserer den med en tom tekststreng.
# Denne variabelen vil senere bli brukt til å lagre rollen til personen.
rolle = ""

# Vi bruker en if-elif-else struktur for å bestemme rollen til personen basert på navnet de oppga.
# Denne strukturen lar oss utføre forskjellige handlinger basert på ulike betingelser.
if navn == "Terje":
    # Hvis navnet er "Terje", settes rollen til "lærer".
    rolle = "lærer"
elif navn == "Martin":
    # Hvis navnet er "Martin", settes rollen til "foredragsholder".
    rolle = "foredragsholder"
else:
    # Hvis navnet ikke er noen av de ovennevnte, settes rollen til "ukjent".
    rolle = "ukjent"

# Vi skriver ut rollen til personen.
# Tekststrenger kan kombineres (konkateneres) ved å bruke '+' operatoren.
print("Rollen til personen er: " + rolle)
