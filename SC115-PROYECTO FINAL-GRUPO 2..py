from datetime import datetime,date,timedelta

pedidos = []
platillos = {"ENTRADAS": [], "PLATOS FUERTES": [], "POSTRES": [], "BEBIDAS": []}

def agregar_cliente():
    correo = input("Ingrese el correo electrónico del cliente: ")
    nombre = input("Ingrese el nombre completo del cliente: ")
    tarjeta = input("Ingrese el número de tarjeta de crédito del cliente: ")
    fecha_vencimiento = input("Ingrese la fecha de vencimiento de la tarjeta (mm/aaaa): ")
    codigo_seguridad = input("Ingrese el código de seguridad de la tarjeta: ")
    print("Cliente agregado con éxito.")



def agregar_pedido():
    hora_pedido = datetime.now()
    platillos_pedido = []
    if len(pedidos) > 0:
        tiempo_espera = len(pedidos) * 15
        hora_entrega = pedidos[-1]['hora_entrega'] + timedelta(minutes=15)
    else:
        tiempo_espera = 15
        hora_entrega = hora_pedido + timedelta(minutes=15)
    while True:
        tipo = input("Ingrese el tipo de platillo {ENTRADAS}{PLATOS FUERTES}{POSTRES}{BEBIDAS} o presione 'ENTER' para finalizar el pedido:")
        if tipo == '':
            break
        elif tipo.upper() not in platillos:
            print("ERROR: Favor intentar nuevamente")
        else:
            platillo = input("Ingrese la descripción del platillo: ")
            platillo_encontrado = False
            for p in platillos[tipo.upper()]:
                if p['descripcion'] == platillo:
                    platillo_encontrado = True
                    platillos_pedido.append(p)
                    print(f"El platillo '{p['descripcion']}' se ha agregado correctamente a la orden.")
                    break
            if not platillo_encontrado:
                print("ERROR: El platillo ingresado no fue encontrado. Favor intentar nuevamente.")
    hora_entrega_str = hora_entrega.strftime("%H:%M")
    pedidos.append({'hora_pedido': hora_pedido, 'platillos_pedido': platillos_pedido, 'hora_entrega': hora_entrega})
    print(f"Pedido registrado con éxito. Su tiempo de espera aproximado es de {tiempo_espera} minutos. Su pedido estará listo a las {hora_entrega_str}.")

#===========================================================================================================================================================

def menu_administrador():
    while True:
        print("-------------------------------------------")
        print("Menú Administrador")
        print("Seleccione una opción:\n1.Agregar platillo\n2.Ver platillos\n3.Generar factura\n4.Ver pedidos en cola\n5.Regresar al menú principal")
        print("-------------------------------------------")
        opcion = input()

        if opcion == "1":
            agregar_platillo()

        elif opcion == "2":
            ver_platillos()

        elif opcion == "3":
            generar_factura()
            

        elif opcion == "4":
            ver_pedidos_en_cola()

        elif opcion == "5":
            break

        else:
            print("Opción Inválida, por favor seleccione de nuevo")

#===========================================================================================================================================================

def menu_cliente():
    while True:
        print("-------------------------------------------")
        print("Menú Cliente")
        print("Seleccione una opción:\n1.Ver platillos\n2.Solicitar pedido\n3.Regresar al menú principal")
        print("-------------------------------------------")
        opcion = input()

        if opcion == "1":
            ver_platillos()

        elif opcion == "2":
            agregar_pedido()

        elif opcion == "3":
            break

        else:
            print("Opción Inválida, por favor seleccione de nuevo")

#===========================================================================================================================================================

def agregar_platillo():
    while True:
        tipo = input("Ingrese el tipo de platillo {ENTRADAS}{PLATOS FUERTES}{POSTRES}{BEBIDAS}:")
        if tipo.upper() in platillos:
            break
        else:
            print("ERROR: Favor intentar nuevamente")

    descripcion = input("Ingrese la descripcion del platillo")
    while True:
        try:
            precio = int(input("Ingrese el precio sin IVA del platillo"))
            break
        except ValueError:
            print("ERROR: Favor ingresar un número entero para el precio del producto.")

    platillo = {"descripcion": descripcion, "precio": precio}
    platillos[tipo.upper()].append(platillo)
    print(f"El platillo '{descripcion}' se ha agregado correctamente a la sección '{tipo.upper()}'\n")


#===========================================================================================================================================================

def ver_platillos():
    for tipo in platillos:
        print(f"{tipo}:")
        for platillo in platillos[tipo]:
            print(f"{platillo['descripcion']} ₡{platillo['precio']}")
        print("")

#===========================================================================================================================================================




def generar_factura():
    fecha_actual = date.today()

    fecha_nacimiento = input("Ingrese su fecha de nacimiento (yyyy-mm-dd): ")
    anio_nacimiento = int(fecha_nacimiento[:4])
    mes_nacimiento = int(fecha_nacimiento[5:7])
    dia_nacimiento = int(fecha_nacimiento[8:])

    edad = fecha_actual.year - anio_nacimiento - ((fecha_actual.month, fecha_actual.day) < (mes_nacimiento, dia_nacimiento))

    agregar_cliente()  
    subtotal = 0
    platillos_pedidos = []
    for tipo in platillos:
        for platillo in platillos[tipo]:
            platillos_pedidos.append(platillo)
            subtotal += platillo['precio']

    iva = round(subtotal * 0.13, 2)
    total_con_iva = round(subtotal * 1.13, 2)
    descuento=0

    

    if fecha_actual.month == mes_nacimiento and fecha_actual.day == dia_nacimiento:
        descuento = total_con_iva * 0.12
        total_con_iva -= descuento
        print(f"¡Feliz cumpleaños! Se le ha aplicado un descuento del 12%.")

    
    print(f"Subtotal: ₡{subtotal} colones")
    print(f"IVA (13%): ₡{iva} colones")
    if descuento> 0:
        print(f"Descuento (12%): ₡{descuento} colones")
    print(f"Total a pagar: ₡{total_con_iva} colones")


#===========================================================================================================================================================

 
    
def ver_pedidos_en_cola():
    if len(pedidos) == 0:
        print("No hay pedidos en cola.")
    else:
        print("Lista de Pedidos:")
        for i, pedido in enumerate(pedidos):
            platillos = ", ".join([p['descripcion'] for p in pedido['platillos_pedido']])
            print(f"Pedido {i+1}: {platillos} / Hora de pedido: {pedido['hora_pedido'].strftime('%H:%M:%S')} / Hora de entrega: {pedido['hora_entrega'].strftime('%H:%M:%S')}")

#===========================================================================================================================================================

while True:
    print("===========================Bienvenido a STEAM CENTER===========================")
    print("Seleccione una opción:\n1.Menú Administrador\n2.Menú Cliente\n3.Salir")
    opcion = input()

    if opcion == "1":
        menu_administrador()

    elif opcion == "2":
        menu_cliente()

    elif opcion == "3":
        print("Hasta Pronto")
        break

    else:
        print("Opción Opción Inválida, por favor seleccione de nuevo")





    

   

        











   
