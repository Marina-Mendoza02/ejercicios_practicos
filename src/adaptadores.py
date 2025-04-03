
input_file = "data/4_input_adapters.txt"
output_file = "results/4_input_no_adapters.txt"

# checar si el archivo de entrada existe
import os
if not os.path.exists(input_file):
    print(f"Error: {input_file} no encontrado")
else:

# Leer el archivo de entrada y escribir en el archivo de salida
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            trimmed_sequence = line[14:].strip()  # Cortar los primeros 14 caracteres y eliminar espacios en blanco
            outfile.write(f"{trimmed_sequence} \n")  # Escribir en el archivo de salida
    
    print(f"Output escrito en {output_file}")