import os

inputfile = "data/secuencias.fasta"

if not os.path.exists(inputfile):
    print(f"Error: {inputfile} no encontrado")
else:
    with open(inputfile, "r") as infile:
        # leer las lineas del archivo y almacenarlas en una lista
        lines = infile.readlines()

    # lista de todas las secuencias que comienzan con '>'
    filtered_lines = [line for line in lines if line.startswith(">")]
    
    print(f"Sequence total: {len(filtered_lines)}")

