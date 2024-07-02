






xf = "hola mundo"
ye = "hola mundo"

m=0.0
c=0.0
h=0.0


while True:
    
    print("seleccione una opcion")
    print("1. ingresar nombre")
    print("2. ingresar apellido")
    print("3. ingresar notas")
    print("4. obtener datos")
    print("5. cerrar sesion")

    l = int(input("Seleccione del 1 al 5"))


    if l == 1:
        xf = input("ingrese su nombre")
    elif l == 2:
        ye = input("Ingrese su apellido")
    elif l == 3:
        m = float(input("ingrese su nota de matematicas"))
        c = float(input("ingrese su nota de ciencias"))
        h = float(input("ingrese su nota de historia"))
    elif l == 4: 


        diccionario = {
        "nombre:": xf,
        "apellido": ye,
        "notas": [m, c, h]}



    




   

    

    
    
    

        
        antepromedio = (m+c+h)
        promedio = (antepromedio/3)




        import json
        datos = {
        "nombre:": xf,
        "apellido": ye,
        "Notas" :[m, c, h],
        "Promedio": promedio}

        with open('archivo.json', 'r') as archivo:
            datos_leidos = json.load(archivo)
        
        print(datos_leidos)
    
    elif l == 5:
        print("cerrando sesion")
    else:
        print("Error, marrque una opcion valida")   
        
    

        







