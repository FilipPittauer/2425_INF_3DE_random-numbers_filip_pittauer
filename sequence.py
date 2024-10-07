import random

def generate_sequence(n):
    return [random.randint(1, n) for _ in range(n)]
    
# Otestování funkce
print(generate_sequence(10))  # Vygeneruje 10 náhodných čísel
