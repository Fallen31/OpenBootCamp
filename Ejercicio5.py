def bisiesto (anio):
    if anio % 4 == 0 and anio % 100 == 0 and anio % 400 ==0:
            print(f"El año '{anio}' es año bisiesto")
    elif anio % 4 == 0 and anio % 100 != 0:
        print(f"El año '{anio}' es año bisiesto")
    else: print(f"El año '{anio}' no es un año bisiesto")
bisiesto()                   


