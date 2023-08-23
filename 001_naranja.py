while True:
    color = input("Introduce un color: ")
    if color.lower().strip() == "naranja":
        print("Me parece una buena elección, aunque cualquier decisión tuya me habría parecido bien.")
        break
    else:
        print("¿No sería mejor elegir naranja?")
