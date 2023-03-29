def agregar_cliente():
    correo = input("Ingrese el correo electrónico del cliente: ")
    nombre = input("Ingrese el nombre completo del cliente: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del cliente (dd‘/‘mm‘/‘aaaa): ")
    tarjeta = input("Ingrese el número de tarjeta de crédito del cliente: ")
    fecha_vencimiento = input("Ingrese la fecha de vencimiento de la tarjeta (mm/aaaa): ")
    codigo_seguridad = input("Ingrese el código de seguridad de la tarjeta: ")
    print("Cliente agregado con éxito.")


    
#Registro de Platillos
platillos={"ENTRADAS":[],"PLATOS FUERTES":[],"POSTRES":[],"BEBIDAS":[]}

while True:
    print("Bienvenido a STEAM CENTER")
    print("Seleccione una opción:\n1.Agregar platillo\n2.Ver platillos\n3.Generar factura\n4.Salir")
    opcion=input()

    if opcion=="1":
        while True:
            tipo=input("Ingrese el tipo de platillo {ENTRADAS}{PLATOS FUERTES}{POSTRES}{BEBIDAS}:")
            if tipo.upper() in platillos:
                break
            else:
                print("ERROR:Favor intentar nuevamente")

        descripcion=input("Ingrese la descripcion del platillo")
        while True:
            try:
                precio=int(input("Ingrese el precio sin IVA del plastillo"))
                break
            except ValueError:
                 print("ERROR:Favor ingresar un número entero para el precio del producto.")

        platillo={"descripcion":descripcion,"precio":precio}
        platillos[tipo.upper()].append(platillo)
        print(f"El platilllo '{descripcion}'se ha agregado correctamente a la sección '{tipo.upper()}'\n") 


    elif opcion =="2":
        for tipo in platillos:
            print(f"{tipo}:")
            for platillo in platillos[tipo]:
                print(f"{platillo['descripcion']} ₡{platillo['precio']}")
            print("")
       
          

    elif opcion=="3":
        agregar_cliente()
        subtotal = 0
        platillos_pedidos = []
        for tipo in platillos:
            for platillo in platillos[tipo]:
                platillos_pedidos.append(platillo)
                subtotal += platillo['precio']
        total_con_iva = round(subtotal * 1.13, 2)
        print(f"Total a pagar: ₡{total_con_iva} colones")
        
    elif opcion=="4":
        print("Hasta Pronto")
        break
    else:
        print("Opción Inválida, por favor seleccione de nuevo")
        


    


#Lista de Ordenes

ordenes=[]

while True:
    número_ordenes=input("Ingrese el número de la orden")
    usuario=input("Favor ingresar el nombre del usuario que solicita la orden.") 
    platillos=input("Ingresa el platillo ordenado")

    texto_de_solicitud=f"Número de la orden:{número_ordenes} / Usuario:{usuario} / Platillos:{platillos}"

    ordenes.append(texto_de_solicitud)

    print("Lista de órdenes")
    for i,orden in enumerate(ordenes):
        print(f"{i+1}.{orden}")

    finalizar=input("Desea finalizar una orden?:{SI} {NO}")
    if finalizar.upper()=="SI":
        orden_a_finalizar=int(input("Que orden desea finalizar?"))
        valor=ordenes[orden_a_finalizar-1]
        ordenes.remove(valor)



    

  

        

    

    
    
    





    

    

                
    
