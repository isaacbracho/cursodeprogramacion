def ingresar_nota():
    while True:
        try:
            nota = float(input("Por favor, ingresa una nota entre 0 y 20: "))
            if 0 <= nota <= 20:
                print(f"Has ingresado la nota: {nota}")
                return nota
            else:
                print("Error: La nota debe estar entre 0 y 20. Inténtalo de nuevo.")
        except ValueError:
            print