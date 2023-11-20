### Vanlige Feil Nybegynnere i Python Uten Programmeringsbakgrunn Gjør

1. **Ikke Forstå Variabeltyper og Typekonvertering**
   - Forvirring mellom `int`, `float`, og `str`.
   - **Eksempel:**
     ```python
     nummer = "5" + 2
     ```
   - **Feilforklaring:** Her prøver man å legge sammen en streng (`"5"`) og et heltall (`2`), noe som fører til `TypeError`.
   - **Løsning:**
     ```python
     nummer = int("5") + 2
     ```

2. **Feil med Indentering**
   - Uregelmessig eller inkonsekvent indentering.
   - **Eksempel:**
     ```python
     def funksjon():
     print("Hei")  # Feil indentering
     ```
   - **Feilforklaring:** `print`-funksjonen er ikke riktig indentert innenfor funksjonsdefinisjonen.
   - **Løsning:**
     ```python
     def funksjon():
         print("Hei")
     ```

3. **Feil i Syntaks**
   - Glemme kolon (`:`) etter `if`, `for`, `while`, `def`.
   - **Eksempel:**
     ```python
     if x == 5
         print("x er 5")  # Mangler kolon
     ```
   - **Feilforklaring:** Mangler kolon etter betingelsen i `if`-setningen.
   - **Løsning:**
     ```python
     if x == 5:
         print("x er 5")
     ```

4. **Misforståelse av Løkker**
   - Uendelige løkker ved feil i `while`-betingelser.
   - **Eksempel:**
     ```python
     while True:
         print("Uendelig løkke")  # Ingen avslutningsbetingelse
     ```
   - **Feilforklaring:** Løkken har ingen betingelse for å stoppe, og vil derfor kjøre uendelig.
   - **Løsning:**
     ```python
     teller = 0
     while teller < 5:
         print("Ikke uendelig løkke")
         teller += 1
     ```

5. **Feil Håndtering av Lister og Ordbøker**
   - Forvirring om indeksering og manipulering.
   - **Eksempel:**
     ```python
     min_liste = [1, 2, 3]
     print(min_liste[3])  # Feil indeksering
     ```
   - **Feilforklaring:** Prøver å aksessere et element utenfor listenes rekkevidde (indekser starter på 0).
   - **Løsning:**
     ```python
     print(min_liste[2])  # Korrekt indeks for det tredje elementet
     ```

6. **Feil Bruk av Funksjoner**
   - Glemme å kalle funksjoner med parenteser.
   - **Eksempel:**
     ```python
     def min_funksjon():
         return "Hei"
     print(min_funksjon)  # Skriver ut funksjonsobjektet, ikke kallet
     ```
   - **Feilforklaring:** Utskriften viser funksjonsobjektet, ikke resultatet av funksjonskallet.
   - **Løsning:**
     ```python
     print(min_funksjon())
     ```

7. **Feilhåndtering og Unntak**
   - Ikke bruke `try` og `except` blokker riktig.
   - **Eksempel:**
     ```python
     try:
         x = 1 / 0
     except:
         print("En feil oppstod")  # Generell feilhåndtering uten spesifikk feiltype
     ```
   - **Feilforklaring:** Fanger alle typer unntak, noe som kan skjule andre feil.
   - **Løsning:**
     ```python
     try:
         x = 1 / 0
     except ZeroDivisionError:
         print("Kan ikke dele med null")
     ```

8. **Feil i Bruk av Strenger**
   - Forvirring med strengkonkatenering og formatering.
   - **Eksempel:**
     ```python
     print("Summen er: " + 5)  # TypeError
     ```
   - **Feilforklaring:** Forsøk på å konkatere en streng med et heltall.
   - **Løsning:**
     ```python
     print("Summen er: " + str(5))
     ```

9. **Misforståelse av Variabel Scope**
   - Forvirring om variabeltilgjengelighet.
   - **Eksempel:**
     ```python
     def min_funksjon():
         a = 5
     print(a)  # `a` er ikke definert utenfor funksjonen
     ```
   - **Feilforklaring:** Variabelen `a` er definert innenfor en funksjon og er ikke tilgjengelig utenfor.
   - **Løsning:**
     ```python
     def min_funksjon():
         a = 5
         return a
     a = min_funksjon()
     print(a)
     ```

10. **Ikke Bruke Kommentarer og Dokumentasjon**
    - Skrive kode uten forklarende kommentarer.
    - **Eksempel:** Kompleks kode uten kommentarer.
    - **Feilforklaring:** Koden kan være vanskelig å forstå og vedlikeholde uten kommentarer.
    - **Løsning:** Legg til kommentarer som forklarer hva koden gjør.
      ```python
      # Beregner summen av to tall og skriver resultatet
      def sum(a, b):
          return a + b
      resultat = sum(5, 3)
      print("Resultatet er:", resultat)
      ```