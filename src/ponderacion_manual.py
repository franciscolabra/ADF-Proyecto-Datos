# Ejemplo de ponderación manual (TF - Frecuencia de Término)
# Sin usar sklearn para que corra en cualquier sitio

frase = "el sistema de datos es lento y el sistema de seguridad es rápido"
palabras = frase.split()
total_palabras = len(palabras)

# 1. Contamos cuántas veces aparece cada palabra
conteo = {}
for p in palabras:
    conteo[p] = conteo.get(p, 0) + 1

# 2. Calculamos la ponderación (Frecuencia relativa)
print(f"{'PALABRA':<12} | {'PONDERACIÓN':<12}")
print("-" * 25)

for p, cantidad in conteo.items():
    # Peso = veces que aparece / total de palabras
    peso = cantidad / total_palabras
    print(f"{p:<12} | {peso:.4f}")
