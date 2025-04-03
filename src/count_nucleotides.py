
secuencias = input("Dame secuencias separadas por comas: ").upper().split(",")

# para cada secuencia en la lista, crear una sublista:
#   - conteo de adenina como string descriptivo
#   - conteos numéricos de T, G, y C
conteo = [[f"A: {secuencia.count('A')}", secuencia.count("T"), secuencia.count("G"), secuencia.count("C")]  for secuencia in secuencias]

print(conteo)