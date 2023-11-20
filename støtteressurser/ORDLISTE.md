
# Ordliste for Python

## Python-konsepter

Selvfølgelig, jeg vil inkludere både forklaringer og eksempler for hvert punkt på listen. Dette vil gi en bedre forståelse og kontekst for hvert konsept, spesielt nyttig for nybegynnere i alderen 13 til 15 år.

1. **Grunnleggende konsepter:**
   - **Algoritme:** En trinnvis prosedyre for å løse et problem, som en oppskrift i matlaging. 
     - *Eksempel:* En algoritme for å finne det største tallet i en liste av tall.
   - **Syntaks:** Reglene for hvordan du skriver kode. Ukorrekt syntaks fører til feil.
     - *Eksempel:* I Python må en if-setning avsluttes med et kolon, som `if alder > 18:`.
   - **Kildekode (Source Code):** Den originale koden som en programmerer skriver.
     - *Eksempel:* En Python-fil som inneholder `print("Hei, verden!")`.
   - **Interpreter:** Et program som kjører og utfører din Python-kode, linje for linje.
     - *Eksempel:* Python interpreteren leser og kjører koden `print("Hei, verden!")` og viser resultatet.
   - **Skript:** Et enkeltstående program skrevet for å utføre en spesifikk oppgave.
     - *Eksempel:* Et Python-skript som automatisk organiserer filene i en mappe basert på filtype.

2. **Utviklingsverktøy:**
   - **Integrert Utviklingsmiljø (IDE):** Et program som gir verktøy for å skrive og teste kode.
     - *Eksempel:* VSCode, som hjelper med kodeforslag og feilsøking.
   - **Debugging:** Prosessen med å finne og rette feil i programvaren.
     - *Eksempel:* Bruke en debugger for å finne ut hvorfor et program krasjer når en bestemt knapp trykkes.
   - **Versjonskontroll:** Et system som registrerer endringer i en fil eller sett av filer over tid.
     - *Eksempel:* Bruke Git til å holde styr på endringer i et spillutviklingsprosjekt.

3. **Gjenbruk og Organisering av Kode:**
   - **Modul:** En fil som inneholder Python-kode, som kan være en samling av funksjoner.
     - *Eksempel:* En `mattefunksjoner.py` modul som inneholder funksjoner for å legge sammen og multiplisere tall.
   - **Bibliotek (Library):** En samling av forhåndsskrevne kode som utvider funksjonaliteten i dine programmer.
     - *Eksempel:* Bruke NumPy-biblioteket for å utføre komplekse matematiske operasjoner.
   - **Import:** Å hente og bruke kode skrevet i en annen modul eller et bibliotek.
     - *Eksempel:* Skrive `import math` for å bruke matematiske funksjoner som `math.sqrt(16)`.
   - **PIP (Pip Installs Packages):** Et verktøy for å installere og håndtere ekstra biblioteker.
     - *Eksempel:* Bruke PIP til å installere Flask-biblioteket for webutvikling.

## Programmeringskonsepter

1. **Variable**: Et navn du gir til noe i programmet ditt slik at du kan bruke det senere.
   - Eksempel: `age = 12`

2. **Data Types**: Dette er forskjellige typer data som Python forstår.
    - **Integer**: Et helt tall, som 3, 100, eller -5.
    - **Float**: Et tall med desimaler, som 3.14 eller 0.5.
    - **String**: En rekke bokstaver, tall eller andre tegn satt sammen, skrevet med anførselstegn.
      - Eksempel: `greeting = "Hello"`
    - **Boolean**: Kan bare være True eller False.
      - Eksempel: `is_sunny = True`

3. **List**: En samling av elementer i en spesifikk rekkefølge.
   - Eksempel: `fruits = ['apple', 'banana', 'cherry']`

4. **Print**: Hvordan du forteller Python å vise noe på skjermen.
   - Eksempel: `print("Hello, world!")`

5. **Input**: Å få informasjon fra brukeren.
   - Eksempel: `name = input("Hva heter du? ")`

6. **If Statement**: Forteller Python å gjøre noe bare hvis noe annet er sant.
   - Eksempel: 
     ```python
     is_sunny = True

     if is_sunny:
         print("Ta på solbriller")
     else:
        print("Ta med paraply")
     ```

7. **Loop**: Å gjøre noe om og om igjen.
    - **For Loop**: Går gjennom elementer i en liste eller et område, ett etter ett.
      - Eksempel: 
        ```python
        fruits = ["apple", "banana", "orange"]

        for fruit in fruits:
            print(fruit)
        ```
    - **While Loop**: Fortsetter så lenge en betingelse er sann.
      - Eksempel: 
        ```python
        count = 0
        while count < 5:
            print(count)
            count += 1
        ```

8. **Function**: Et sett med instruksjoner som du kan bruke mange ganger, opprettet ved å bruke `def`.
   - Eksempel: 
     ```python
     def say_hello():
         print("Hello!")
     ```

9. **Return**: Hvordan en funksjon gir noe tilbake etter at den er ferdig.
    - Eksempel: 
      ```python
      def add(a, b):
          return a + b
      ```

10. **Comment**: En merknad i koden din som datamaskinen ignorerer, ment for mennesker å lese. Laget med en `#`.
    - Eksempel: `# Dette er en kommentar`

11. **Indentation**: Å sette inn mellomrom eller tabulatorer i begynnelsen av en linje for å vise hvilke instruksjoner som hører sammen.
    - Eksempel: 
      ```python
      if is_sunny:
          print("Det er en solrik dag!")  # Denne linjen er innrykket
      ```

12. **Error**: Når datamaskinen ikke forstår instruksjonene dine og forteller deg hva som gikk galt.


## Nøkkelord

I Python eksiterer "nøkkelord". Dette er ord man ikke kan navngi variabler med og har en funksjon i programmet.
Under er et utvalg av disse sammen med en enkel forklaring. 

**Datatyper og Verdier**
- `True`: Representerer den boolske verdien Sann.
- `False`: Representerer den boolske verdien Usann.
- `None`: Representerer fraværet av en verdi eller en nullverdi.

**Operatorer**
- `and`: En logisk operator brukt til å kombinere betingede uttrykk.
- `or`: En logisk operator brukt til å kombinere betingede uttrykk.
- `not`: En logisk operator brukt for å snu sannhetsverdien.
- `is`: Brukes for å teste om to variabler er like.
- `in`: Brukes for å sjekke om en verdi finnes i en sekvens.

**Conditional Statements**
- `if`: Brukes for å lage en betinget uttalelse.
- `elif`: Brukes i betingede uttalelser, det samme som "ellers hvis".
- `else`: Brukes i betingede uttalelser.

**Løkker**
- `for`: Brukes for å lage en for-løkke.
- `while`: Brukes for å lage en while-løkke.
- `break`: Brukes for å bryte ut av en løkke.
- `continue`: Brukes for å hoppe over resten av koden inne i en løkke for den gjeldende iterasjonen.

**Funksjons- og Klassedefinisjoner**
- `def`: Brukes for å definere en funksjon.
- `return`: Brukes for å returnere en verdi fra en funksjon.

**Unntakshåndtering**
- `try`: Brukes for å fange unntak i try...except-blokker.
- `except`: Brukes med unntak, hva man skal gjøre når et unntak oppstår.
- `finally`: Brukes med unntak, en blokk med kode som vil bli utført uansett om det er et unntak eller ikke.
- `raise`: Brukes for å utløse et unntak.
- `assert`: Brukes til feilsøking, for å hevde at noe er sant.

**Importering**
- `import`: Brukes for å importere en modul.
- `from`: Brukes for å importere spesifikke deler av en modul.
- `as`: Brukes for å lage et alias ved importering av en modul.

**Diverse**
- `pass`: En null-uttalelse, en uttalelse som ikke vil gjøre noe.
- `del`: Brukes for å slette et objekt.
