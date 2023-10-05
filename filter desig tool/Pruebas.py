numero = 1
notacion_cientifica = f"{numero:.1e}"
if "e" in notacion_cientifica:
    parte_entera, exponente = notacion_cientifica.split("e")
    exponente = int(exponente)
    if exponente % 3 == 0:
        resultado = f"{int(float(parte_entera))}k"
    else:
        resultado = f"{float(parte_entera)}k"
    print(resultado)
else:
    print(notacion_cientifica)
