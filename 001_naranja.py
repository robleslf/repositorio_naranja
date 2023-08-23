from lib_separadores import *

separador_titulo("Naranja 1.0")

while True:
    color = input("Introduce un color: ")
    separador_1()
    if color.lower().strip() == "naranja":
        print("Me parece una buena elección, aunque cualquier decisión tuya me habría parecido bien.")
        print("(=⌒‿‿⌒=)")
        break
    else:
        print("¿No sería mejor elegir naranja?")
