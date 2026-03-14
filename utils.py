# %%
import numpy as np
import random

# %%
""" 
1. Crear un tablero 10x10
"""

def crea_tablero(lado=10):
    return np.full((lado, lado), " ")


def mostrar_tablero(tablero):

    """ Muestra el tablero visualmente de forma legible"""

    lado = tablero.shape[0]

    print("    " + "".join(f"{i:^3}" for i in range(1, lado + 1))) 
    
    """
    Imprime numeros de columnas, 
    range(1, lado+1) → números del 1 al 10
    {i:^3} → Centra numero en un espacio de 3 caracteres
    """

    for i, fila_tablero in enumerate(tablero, start=1):
        fila = "".join(f"[{celda}]" if celda != " " else "[ ]" for celda in fila_tablero)
        print(f"{i:>2}  {fila}")

    """
    for i, fila_tablero in enumerate(tablero, start=1) → Recorrer cada fila del tablero
    fila = "".join(f"[{celda}]" if celda != " " else "[ ]" for celda in fila_tablero) → Convierte cada celda en [ ]
    print(f"{i:>2}  {fila}") → Alinea el numero en un espacio de 2 caracteres
    """


# %%
""" 
2. Este apartado indica que cuando se esten creando los barcos y posicionandolos aleatoriamente, 
si se sale del tablero o lo coloca encima de otro barco, de error y vuelva a intentarlo
"""

def coloca_barco_plus(tablero, barco, mostrar_info=True):
    tablero_temp = tablero.copy()

    for pieza in barco:
        fila, columna = pieza

        """
        for pieza in barco (por cada coordenada en el barco indicado de eslora x) permite unificar una coordenada (fila, columna) en una sola variable (pieza)
        """

        if fila < 0 or fila >= tablero.shape[0] or columna < 0 or columna >= tablero.shape[1]:
            if mostrar_info:
                print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        
        """
        Comprueba que no se salga del tamaño del tablero al colocar el barco
        """

        if tablero_temp[fila, columna] != " ":
            if mostrar_info:
                print(f"No puedo poner la pieza {pieza} porque ya hay un barco")
            return False
        
        """
        Comprueba que no haya un barco ya
        """

    for pieza in barco:
        fila, columna = pieza
        tablero_temp[fila, columna] = "O"

        """
        Si no hay problema alguno para colocar el barco, se infica con una "O"
        """

    return tablero_temp

# %%
""" 
3. En este apartado se creara la funcion para colocar barcos aleatoriamente con los parametros indicados
"""

def coloca_barco(tablero, eslora=4, nombre="", num_intentos=100, mostrar_info=True):

    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]

    while True:

        """
        Probara colocar posiones hasta que se coloquen todos los barcos
        """

        barco = []
        pieza_original = (
            random.randint(0, num_max_filas - 1),
            random.randint(0, num_max_columnas - 1)
        )

        barco.append(pieza_original)

        """
        Este apartado es muy importante porque indicara la ubicacion del barco aunque no se imprima
        """

        orientacion = random.choice(["N", "S", "O", "E"])

        fila = pieza_original[0]
        columna = pieza_original[1]

        for i in range(eslora - 1):
            if orientacion == "N":
                fila -= 1
            elif orientacion == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1

            pieza = (fila, columna)
            barco.append(pieza)

        """
        for i in range(eslora - 1): → Como la primera pieza ya existe, solo se añadiran las restantes
        """

        tablero_temp = coloca_barco_plus(tablero, barco, mostrar_info=mostrar_info)

        """
        Aca se intenta colocar los barcos en el tablero
        """

        if type(tablero_temp) == np.ndarray:
            if mostrar_info:
                print(f"{nombre} colocado en coordenadas: {barco}")
            return tablero_temp
        
        """
        Si se logra colocar, se imprimen las coordenadas
        """

        if mostrar_info:
            print(f"No se pudo colocar {nombre}, reintentando...")

        """
        Si no se puede colocar, reintenta hasta lograrlo
        """

# %%
"""
4. En este apartado se indicara que si se da a un barco, pase de 0 a X, 
si es agua pasa de " " a "-" y si es otro barco, de error.
"""

def recibir_disparo(tablero, coordenada):

    if tablero[coordenada] == "O":
        tablero[coordenada] = "X"
        print("Le has dado! \n")
    elif tablero[coordenada] == "X":
        print("Ya has disparado aca, a tomar ginseng para esa memoria...\n")
    else:
        tablero[coordenada] = "-"
        print("Ha caido en el mar :/ \n")

# %%
"""
5. Coloca 6 barcos aleatoriamente en el tablero:
- 3 barcos de eslora 2
- 2 barcos de eslora 3
- 1 barco de eslora 4
"""

def colocar_barcos(tablero, mostrar_info=True):

    esloras = [2,2,2,3,3,4]

    for i, eslora in enumerate(esloras):
        tablero = coloca_barco(
            tablero,
            eslora=eslora,
            nombre=f"Buque {i+1}",
            mostrar_info=mostrar_info)

    """
    Por cada numero que se indica en esloras, se enumera hasta ese numero (1,2,3...)
    luego se modifica el tablero correspondiente añadiendose todos los barcos con las esloras indicadas, el nombre del Barco (Buque),
    y si se puede o no mostrar las coordenadas
    """

    return tablero

# %%
"""
6. Verifica so quedan barcos vivos en el tablero
Retorna True si ya no quedan barcos (todas las "0" fueron destruidas).
"""

def ha_ganado(tablero):
    num_barcos_vivos = np.count_nonzero(tablero == "O")
    return num_barcos_vivos == 0

# %%
"""
7. Muestra el tablero enemigo ocultando los barcos no impactados.
- Muestra "X" (barcos tocados)
- Muestra "-" (agua disparada)
- Oculta "O" (barcos no descubiertos) → los muestra como " "
"""

def mostrar_tablero_enemigo(tablero):
    tablero_oculto = tablero.copy()
    tablero_oculto[tablero_oculto == "O"] = " "
    return tablero_oculto

# %%
"""
8. Pide coordenadas al jugador (1-10) y dispara.
Retorna True si acertó, False si falló.
"""

def disparo_jugador(tablero_enemigo):
    print("\n TU TURNO - Introduce coordenadas (1-10): ")

    fila_usuario = int(input("FILA: "))
    columna_usuario = int(input("COLUMNA: "))

    fila = fila_usuario - 1
    columna = columna_usuario - 1
    coordenada = (fila, columna)

    acierto = tablero_enemigo[coordenada] == "O"
    recibir_disparo(tablero_enemigo, coordenada)

    return acierto

# %%
"""
9. El NPC dispara a una coordenada aleatoria.
Retorna True si acertó, False si falló.
"""

def disparo_npc(tablero_jugador):

    num_filas = tablero_jugador.shape[0]
    num_columnas = tablero_jugador.shape[1]

    fila = random.randint(0, num_filas - 1)
    columna = random.randint(0, num_columnas -1)

    coordenada = (fila, columna)

    """
    Se indica una coordenada aleatoria para la maquina que vaya del 0-9
    """

    print(f"\n La maquina dispara a: ({fila + 1},{columna +1})")

    acierto = tablero_jugador[coordenada] == "O"
    recibir_disparo(tablero_jugador, coordenada)

    """
    Con la misma funcion creada para recibir disparo, se aplica en el tablero del enemigo para que pueda recibir un disparo tabien
    """

    return acierto

# %%
"""
10. Procesa los comandos del usuario.
Retorna:
- "DISPARO" si el usuario quiere disparar
- "SALIR" si quiere salir
- "CONTINUAR" si solo mostró tableros
"""

def procesar_comando(comando, tablero_jugador, tablero_npc):

    comando = comando.lower().strip()

    if "mi tablero" in comando:
        print("\n TU TABLERO:")
        mostrar_tablero(tablero_jugador)
        return "CONTINUAR"
    
    elif "tablero enemigo" in comando:
        print("\n TABLERO ENEMIGO:")
        mostrar_tablero(mostrar_tablero_enemigo(tablero_npc))
        return "CONTINUAR"
    
    elif "salir" in comando:
        return "SALIR"
    
    else:
        return "DISPARO"


