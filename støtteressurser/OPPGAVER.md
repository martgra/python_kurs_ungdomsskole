## Oppgaver

### Oppgave 1: "Hei, Verden!" med en vri

**Mål:** Å forstå grunnleggende utskrift og brukerinput.

**Oppgave:** 
1. Skriv et program som spør brukeren om deres navn.
2. Programmet skal deretter skrive ut en hilsen, for eksempel "Hei, [navn]!"

**Eksempel:**
```
Hva heter du? Emma
Hei, Emma!
```

### Oppgave 2: Gjett tallet

**Mål:** Å bruke løkker, betingelser og brukerinput.

**Oppgave:** 
1. Programmet velger et hemmelig tall mellom 1 og 10 (du kan hardkode dette tallet).
2. Brukeren får gjette på tallet.
3. Programmet gir tilbakemelding om gjetningen er for høy, for lav, eller korrekt.
4. Spillet fortsetter til brukeren gjetter riktig tall.

**Eksempel:**
```
Gjett tallet: 5
For lavt!
Gjett tallet: 8
For høyt!
Gjett tallet: 7
Riktig! Gratulerer!
```

### Oppgave 3: Regneoperasjoner

**Mål:** Å forstå grunnleggende aritmetikk og brukerinput.

**Oppgave:** 
1. Skriv et program som ber om to tall fra brukeren.
2. Programmet skal deretter utføre og vise resultatet av grunnleggende operasjoner (addisjon, subtraksjon, multiplikasjon, divisjon) med disse tallene.

**Eksempel:**
```
Første tall: 7
Andre tall: 3
7 + 3 = 10
7 - 3 = 4
7 * 3 = 21
7 / 3 = 2.3333
```

### Oppgave 4: Tallrekkefølge

**Mål:** Å bruke løkker for å generere mønstre.

**Oppgave:** 
1. Skriv et program som skriver ut de første 10 tallene i følgende rekkefølge: 1, -2, 3, -4, 5, -6, osv.
2. Hvert tall skal vises på en ny linje.

**Eksempel:**
```
1
-2
3
-4
5
-6
7
-8
9
-10
```

### Oppgave 5: Enkel kalkulator

**Mål:** Å kombinere betingelser, løkker og funksjoner.

**Oppgave:** 
1. Lag en enkel kalkulator som kan utføre addisjon, subtraksjon, multiplikasjon og divisjon basert på brukerens valg.
2. Programmet skal spørre brukeren om å velge en operasjon.
3. Deretter skal det be om to tall og utføre den valgte operasjonen.
4. Programmet skal fortsette å kjøre til brukeren velger å avslutte.

**Eksempel:**
```
Velg operasjon (add, sub, mul, div) eller 'avslutt' for å stoppe: add
Første tall: 5
Andre tall: 3
Resultat: 8
Velg operasjon (add, sub, mul, div) eller 'avslutt' for å stoppe: avslutt
```


## Løsningsforslag

### Oppgave 1: "Hei, Verden!" med en vri

**Pseudokode:**
1. Be brukeren om å oppgi sitt navn.
2. Les inn navnet og lagre det i en variabel.
3. Skriv ut en hilsen som inkluderer det innskrevne navnet.

**Python-kode med kommentarer:**
```python
# Be brukeren om å oppgi sitt navn
navn = input("Hva heter du? ")  # 'input' brukes for å få brukerinput som en streng

# Skriv ut en hilsen som inkluderer det innskrevne navnet
print("Hei, " + navn + "!")  # 'print' brukes for å skrive ut tekst til konsollen
```

`input()` er en funksjon som lar programmet ditt motta input fra brukeren. Den returnerer det brukeren skriver som en streng.

### Oppgave 2: Gjett tallet

**Pseudokode:**
1. Velg et hemmelig tall.
2. Be brukeren om å gjette et tall.
3. Sammenlign brukerens gjetning med det hemmelige tallet.
4. Gi tilbakemelding basert på gjetningen.
5. Gjenta prosessen til brukeren gjetter riktig tall.

**Python-kode med kommentarer:**
```python
# Velger et hemmelig tall
hemmelig_tall = 7  # Tilordner en verdi til variabelen 'hemmelig_tall'

# Starter en løkke som fortsetter til brukeren gjetter riktig tall
while True:
    # Be brukeren om å gjette et tall og konverter svaret til et heltall
    gjett = int(input("Gjett tallet: "))  # 'int' konverterer strengen til et heltall

    # Sammenligner gjetningen med det hemmelige tallet og gir tilbakemelding
    if gjett < hemmelig_tall:
        print("For lavt!")
    elif gjett > hemmelig_tall:
        print("For høyt!")
    else:
        print("Riktig! Gratulerer!")
        break  # Avslutter løkken
```

`while True` skaper en uendelig løkke som bare avsluttes når `break`-kommandoen utføres. `if`, `elif`, og `else` brukes for å utføre forskjellige handlinger basert på betingelser.

### Oppgave 3: Regneoperasjoner

**Pseudokode:**
1. Be brukeren om to tall.
2. Les inn disse tallene.
3. Utfør og vis resultatet av addisjon, subtraksjon, multiplikasjon og divisjon med disse tallene.

**Python-kode med kommentarer:**
```python
# Be brukeren om to tall
tall1 = float(input("Første tall: "))  # Konverterer input til et flyttall
tall2 = float(input("Andre tall: "))   # Konverterer input til et flyttall

# Utfører og viser resultatet av grunnleggende aritmetiske operasjoner
print(f"{tall1} + {tall2} = {tall1 + tall2}")
print(f"{tall1} - {tall2} = {tall1 - tall2}")
print(f"{tall1} * {tall2} = {tall1 * tall2}")
print(f"{tall1} / {tall2} = {tall1 / tall2}")
```

`float()` konverterer en streng til et flyttall, noe som er nyttig for aritmetiske operasjoner.

### Oppgave 4: Tallrekkefølge

**Pseudokode:**
1. Gå gjennom tallene 1 til 10.
2. Skriv ut hvert tall, negativt hvis det er partall, positivt hvis det er oddetall.

**Python-kode med kommentarer:**
```python
# Går gjennom tallene 1 til 10
for i in range(1, 11):  # 'range(1, 11)' gir en sekvens av tall fra 1 til 10
    # Sjekker om tallet er partall eller oddetall
    # Skriver ut tallet som negativt hvis det er partall, ellers som positivt
    if i % 2 == 0:  # '% 2' gir resten av divisjonen med 2, som er 0 for partall
        print(-i)
    else:
        print(i)
```

`for`-løkken brukes her til å gjenta en blokk kode et bestemt antall ganger. `range(1, 11)` genererer tall fra 1 til 10.

### Oppgave 5: Enkel kalkulator

**Pseudokode:**
1. Start en løkke.
2. Be brukeren velge en operasjon eller avslutte.
3. Utfør den valgte operasjonen med to tall.
4. Vis resultatet.
5. Avslutt løkken hvis brukeren velger å avslutte.

**Python-kode med kommentarer:**
```python
# Starter en løkke som kjører til brukeren bestemmer seg for å avslutte
while True:
    # Be brukeren velge en operasjon eller avslutte
    operasjon = input("Velg operasjon (add, sub, mul, div) eller 'avslutt' for å stoppe: ")

    # Avslutter løkken hvis brukeren skriver 'avslutt'
    if operasjon == 'avslutt':
        break

    # Be om to tall
    tall1 = float(input("Første tall: "))
    tall2 = float(input("Andre tall: "))

    # Utfører den valgte operasjonen og viser resultatet
    if operasjon == 'add':
        print("Resultat:", tall1 + tall2)
    elif operasjon == 'sub':
        print("Resultat:", tall1 - tall2)
    elif operasjon == 'mul':
        print("Resultat:", tall1 * tall2)
    elif operasjon == 'div':
        print("Resultat:", tall1 / tall2)
```

I denne koden brukes en `while`-løkke for å tillate gjentatte operasjoner til brukeren bestemmer seg for å avslutte. Betingels