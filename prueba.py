import random


def generar_numero_aleatorio(genes):
    # Usa operaciones a nivel de bit para generar un número entero y luego lo convierte a binario
    numero = format(random.getrandbits(genes), f"0{genes}b")
    return numero


def binario_a_decimal(binario):
    # Convierte directamente de binario a decimal teniendo en cuenta el signo y la parte decimal
    signo = -1 if binario[0] == "1" else 1
    parte_entera = int(binario[1:-1], 2)  # Convierte la parte entera directamente
    parte_decimal = 0.5 if binario[-1] == "1" else 0

    # Calcula el número decimal total
    decimal = signo * (parte_entera + parte_decimal)

    return decimal


def expression(x):
    resultado = -15 * x**2 + 0.5 * x + 25
    return resultado


def ordenar(personas):
    return sorted(
        personas,
        key=lambda persona: (expression(binario_a_decimal(persona))),
        reverse=True,
    )


def mejor_mejor(persona):
    nueva_gen = []
    for j in range(0, len(persona), 2):
        hijo_1 = persona[j][:partir] + persona[j + 1][partir:]
        hijo_2 = persona[j + 1][:partir] + persona[j][partir:]
        print(
            f"Hijo 1 {persona[j][:partir]} + {persona[j + 1][partir:]} == {expression(binario_a_decimal(hijo_1))}"
        )
        print(
            f"Hijo 2 {persona[j + 1][:partir]} + {persona[j][partir:]} == {expression(binario_a_decimal(hijo_2))}"
        )
        nueva_gen.append(hijo_1)
        nueva_gen.append(hijo_2)
    return nueva_gen


def mejor_peor(poblacion):
    nueva_gen = []
    for j in range(0, len(poblacion) // 2):
        hijo_1 = poblacion[j][:partir] + poblacion[-(j + 1)][partir:]
        hijo_2 = poblacion[-(j + 1)][:partir] + poblacion[j][partir:]
        print(
            f"Hijo 1 {poblacion[j][:partir]} + {poblacion[-(j+1)][partir:]} == {expression(binario_a_decimal(hijo_1))}"
        )
        print(
            f"Hijo 2 {poblacion[-(j+1)][:partir]} + {poblacion[j][partir:]} == {expression(binario_a_decimal(hijo_2))}"
        )
        nueva_gen.append(hijo_1)
        nueva_gen.append(hijo_2)
    return nueva_gen


def aleatorio(poblacion):
    indices = list(range(len(poblacion)))
    random.shuffle(indices)
    print("indices ", indices)
    nueva_gen = []
    for j in range(0, len(poblacion), 2):
        hijo_1 = poblacion[indices[j]][:partir] + poblacion[indices[j + 1]][partir:]
        hijo_2 = poblacion[indices[j + 1]][:partir] + poblacion[indices[j]][partir:]
        print(
            f"Hijo 1 {poblacion[indices[j]][:partir]} + {poblacion[indices[j + 1]][partir:]} == {expression(binario_a_decimal(hijo_1))}"
        )
        print(
            f"Hijo 2 {poblacion[indices[j + 1]][:partir]} + {poblacion[indices[j]][partir:]} == {expression(binario_a_decimal(hijo_2))}"
        )
        nueva_gen.append(hijo_1)
        nueva_gen.append(hijo_2)
    return nueva_gen

def invertir(bit):
    return 1 if bit == 0 else 0

def devolver_vector(matriz=[]):
    new_vector = []
    # print(matriz," matrizzzz")
    for fila in matriz:
        cadena_concatenada = ""
        for elemento in fila:
            cadena_concatenada += str(elemento)
        new_vector.append(cadena_concatenada)
    return new_vector

genes = random.randint(3, 5)
pob = []
next_pob = []
tam_poblacion = 2 ** genes

print("La poblacion inicial sera de", tam_poblacion)

while len(pob) < tam_poblacion:
    nueva_persona = generar_numero_aleatorio(9)
    if nueva_persona not in pob:
        pob.append(nueva_persona)
# ordenar
pob = ordenar(pob)
# mostrar.
for per in pob:
    print(
        per,
        " y es ",
        binario_a_decimal(per),
        " y su expresion es ",
        expression(binario_a_decimal(per)),
    )

# Cuantos digitos va a separar para las generaciones
partir = random.randint(1, 7)
print("<-- cortar a los -->", partir)



generaciones = int(input("Cuantas generaciones va a avanzar "))
for i in range(generaciones):
    mutacion = random.randint(0, 1)
    print(
        f"==================================GENERACION {i+1}========================================= {"(Mutacion)" if mutacion==1 else ""}"
    )
    next_pob = []

    metodo = random.randint(1, 3)
    print(f"Se va a usar el metodo de cruzamiento {metodo}")
    if metodo == 1:
        next_pob = mejor_mejor(pob)
    if metodo == 2:
        next_pob = mejor_peor(pob)
    if metodo == 3:
        next_pob = aleatorio(pob)

    next_pob = ordenar(next_pob)

    if mutacion == 1:
        print("Poblacion antes de la mutacion")
        for per in next_pob:
            print(
                per,
                " y es ",
                binario_a_decimal(per),
                " y su expresion esa ",
                expression(binario_a_decimal(per)),
            )
        matriz_personas = []
        #convertir en un arreglo cada string de persona
        for persona in next_pob:
            fila = [int(digito) for digito in persona]
            matriz_personas.append(fila)

        # Decidir aleatoriamente si se mutará un solo dígito o dos
        cantidad_mutaciones = random.randint(1, 2)
        for _ in range(cantidad_mutaciones):
                # Seleccionar aleatoriamente la fila y columna a mutar
                columna = random.randint(0, len(matriz_personas) - 1)
                fila = random.randint(0, len(matriz_personas[0]) - 1)

                # Mostrar los cambios específicos realizados
                print(
                    f"Mutación en la fila {columna}, columna {fila}: {matriz_personas[columna]} -> ",
                    end="",
                )

                # Mutar el dígito
                matriz_personas[columna][fila] = invertir(matriz_personas[columna][fila])
                print(f"{matriz_personas[columna]}")
                
        next_pob=[]
        # print(f"vaciar arreglo {next_pob}")
        next_pob=devolver_vector(matriz_personas)
        print(f"Poblacion despues de la mutacion")

    next_pob = ordenar(next_pob)
    pob = []
    pob = next_pob.copy()
    # print(pob)
    for per in pob:
        print(
            per,
            " y es ",
            binario_a_decimal(per),
            " y su expresion esa ",
            expression(binario_a_decimal(per)),
        )
