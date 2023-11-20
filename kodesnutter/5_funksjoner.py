# Denne funksjonen tar inn to tall, a og b, beregner summen av dem og skriver ut resultatet.
# Den returnerer ingenting (void).

def add_numbers(a, b):
    # Beregner summen av a og b og lagrer resultatet i variabelen result.
    result = a + b
    
    # Skriver ut resultatet ved hjelp av print-funksjonen.
    print("Summen av", a, "og", b, "er:", result)

# Bruk av funksjonen:
add_numbers(5, 3)  # Denne linjen vil skrive ut: Summen av 5 og 3 er: 8


# Denne funksjonen tar inn to tall, a og b, beregner summen av dem og returnerer resultatet.

def add_numbers(a, b):
    # Beregner summen av a og b og lagrer resultatet i variabelen result.
    result = a + b
    
    # Returnerer resultatet ved hjelp av return.
    return result

# Bruk av funksjonen og lagring av resultatet i en variabel:
summen = add_numbers(5, 3)
# Denne linjen bruker funksjonen til å beregne summen av 5 og 3 og lagrer resultatet i variabelen summen.
print("Summen av 5 og 3 er:", summen)  # Denne linjen skriver ut: Summen av 5 og 3 er: 8
