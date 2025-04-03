secuencias = input("Dame las secuencias separadas por comas: ").split(",")

# lista de codones de inicio usando list comprehension
codones_inicio = [secuencia.strip()[:3] for secuencia in secuencias]

print(codones_inicio)