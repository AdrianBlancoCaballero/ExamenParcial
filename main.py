# Examen parcial 2021

while True:
    numero = input("Introduzca un número: ")
    if numero == "fin":
        break
    digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    v_freq = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0,}

    for digito in numero:
        if digito in digitos:
            v_freq[digito] += 1

    print("Cantidad de digitos en el número ", numero, ":", v_freq)