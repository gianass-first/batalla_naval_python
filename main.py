# %%
from utils import crea_tablero, colocar_barcos, mostrar_tablero

# %%
"""
Función principal del juego Batalla Naval.
"""

def jugar_batalla_naval():
    
    print("=" * 60)
    print(" BIENVENIDO A BATALLA NAVAL ")
    print("=" * 60)
    
    # ===== CREAR TABLEROS =====
    print("\n Creando tableros...")
    
    # ====== Tu tablero ======
    tablero_jugador = crea_tablero(10)
    print("\n Colocando tus barcos...")
    print("\n")
    tablero_jugador = colocar_barcos(tablero_jugador, mostrar_info=True)
    print("\n Tus barcos colocados:")
    print("\n")
    mostrar_tablero(tablero_jugador)
    
    # ===== Tablero del NPC =====
    tablero_npc = crea_tablero(10)
    print("\n Colocando barcos del NPC...")
    print("\n")
    tablero_npc = colocar_barcos(tablero_npc, mostrar_info=False)
    print("\n Barcos del NPC colocados (ocultos)\n")
    
    # ===== BUCLE PRINCIPAL =====
    turno = 0
    turno_jugador = True
    
    while True:
        turno += 1
        print("\n" + "=" * 60)
        print(f" TURNO {turno}")
        print("=" * 60)
        
        # ===== TURNO DEL JUGADOR =====
        if turno_jugador:
            print("\n TU TURNO")
            print("\nComandos disponibles:")
            print("  - 'Mi tablero'")
            print("  - 'Tablero enemigo'")
            print("  - 'Salir'")
            print("  - O presiona enter para introducir coordenada")
            
            comando = input("\n Introduce un comando: ").strip()
            
            accion = procesar_comando(comando, tablero_jugador, tablero_npc)
            
            if accion == "SALIR":
                print("\n ¡Hasta luego!")
                return
            
            elif accion == "CONTINUAR":
                continue
            
            elif accion == "DISPARO":
                acierto = disparo_jugador(tablero_npc)
                
                if ha_ganado(tablero_npc):
                    print("¡FELICIDADES! ¡HAS GANADO!")
                    break
                
                if acierto:
                    print(" Boom!! Le diste! Sigue disparando.")
                    turno_jugador = True
                else:
                    print(" Fallaste :/ Turno del NPC.")
                    turno_jugador = False
        
        # ===== TURNO DEL NPC =====
        else:
            print("\n🤖 TURNO DEL NPC")
            
            # ===== NPC dispara =====
            acierto = disparo_npc(tablero_jugador)
            
            print("\n TU TABLERO:")
            print(tablero_jugador)
            
            # ===== Verificar si el NPC ganó =====
            if ha_ganado(tablero_jugador):
                print("EL NPC HA GANADO :/")
                break
            
            # ===== Si acertó, repite turno =====
            if acierto:
                print(" ¡El NPC te dio! Dispara de nuevo.")
                turno_jugador = False
            else:
                print(" El NPC falló. Tu turno.")
                turno_jugador = True
            
            input("\nPresiona ENTER para continuar...")
    
    print(f"\n FIN DEL JUEGO - Total de turnos: {turno}")

# %%
if __name__ == "__main__":
    jugar_batalla_naval()


