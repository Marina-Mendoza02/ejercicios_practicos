
secuencias = input("Dame secuencias separadas por comas: ").split(",")

# lista de secuencias invertidas usando list comprehension
secuencias_invertidas = [seq.strip()[::-1] for seq in secuencias]

print(secuencias_invertidas)
