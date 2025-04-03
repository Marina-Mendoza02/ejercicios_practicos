import os

input_file = "data/dna_sequences.txt"
output_file = "results/dna_sequence.fa"

if not os.path.exists(input_file):
    print(f"Error: {input_file} no encontrado.")
else:
    print(f"Leyendo archivo: {input_file}")

# abrir y leer el archivo de entrada
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # dividir cada línea en ID y secuencia con el tabulador como separador
        id, seq = line.strip().split("\t")
        outfile.write(f">{id}\n{seq.upper()}\n")
        
print(f"Archivo generado correctamente en: {output_file}")