
secuencias = input("Dame secuencias separadas por comas: ").split(",")

# lista de secuencias de ARN usando list comprehesion 
secuencias_arn = [secuencia.replace("T", "U") for secuencia in secuencias]

print(secuencias_arn)