platillos = [  
    {"id":"01", "Nombre": "Arroz de coco", "Precio": 20000},
    {"id":"02", "Nombre": "Alitas BBQ", "Precio": 24000},
    {"id":"03", "Nombre": "Carne Bistec", "Precio": 30000},
    {"id":"04", "Nombre": "Bandeja Paisa", "Precio": 25000},
    {"id":"05", "Nombre": "Pizza Napoletana", "Precio": 50000}
]

bebidas = [ 
    {"id":"01", "Nombre": "Gaseosa", "Precio": 20000},
    {"id":"02", "Nombre": "Limonada Cereza", "Precio": 24000},
    {"id":"03", "Nombre": "Cerveza", "Precio": 30000},
    {"id":"04", "Nombre": "Agua Mineral", "Precio": 25000},
    {"id":"05", "Nombre": "Mojito", "Precio": 50000}
]

mesas = [ 
    {"id":"m1", "Nombre": "Mesa Inicio", "sillas": 4},
    {"id":"m2", "Nombre": "Mesa izquierda", "sillas": 3},
    {"id":"m3", "Nombre": "Mesa Derecha", "sillas": 3},
    {"id":"m4", "Nombre": "Mesa Centro", "sillas": 5},
    {"id":"m5", "Nombre": "Mesa Rincon", "sillas": 2}
]

cliente = dict()
ventas = list()

total = 0
Cliente_Actual = dict()
Mesa_Actual = None

while True:
    print("\n----Bienvenido al restaurante Don Sebas----")
    print("1. Ingrese Datos del Cliente")
    print("2. Elegir Mesa")
    print("3. Elegir Platillo")
    print("4. Elegir Bebida")
    print("5. Facturación")
    print("6. Buscar Cliente")
    print("7. Registro de Ventas")
    print("0. Salir")

    Opcion = int(input("Digite su opción: "))

    if Opcion == 1:
        Nombre = input("Nombre: ")
        Identificacion = int(input("ID: "))
        Telefono = int(input("Teléfono: "))
        Email = input("Email: ")

        cliente[Identificacion] = {
            "nombre": Nombre,
            "telefono": Telefono,
            "email": Email
        }

        Cliente_Actual = cliente[Identificacion]

    elif Opcion == 2:
        for mesa in mesas:
            print(f"{mesa['id']} {mesa['Nombre']} ({mesa['sillas']} sillas)")

        Mesa_seleccionada = input("Seleccione mesa: ")

        for mesa in mesas:
            if mesa["id"] == Mesa_seleccionada:
                Mesa_Actual = mesa
                print("Mesa seleccionada:", mesa["Nombre"])

    elif Opcion == 3:
        for plato in platillos:
            print(f"{plato['id']} {plato['Nombre']} ${plato['Precio']}")

        opcion_plato = input("Seleccione: ")

        for plato in platillos:
            if plato["id"] == opcion_plato:
                total += plato["Precio"]
                print("Agregado:", plato["Nombre"])

    elif Opcion == 4:
        for bebida in bebidas:
            print(f"{bebida['id']} {bebida['Nombre']} ${bebida['Precio']}")

        opcion_bebida = input("Seleccione: ")

        for bebida in bebidas:
            if bebida["id"] == opcion_bebida:
                total += bebida["Precio"]
                print("Agregado:", bebida["Nombre"])

    elif Opcion == 5:
        if Cliente_Actual == dict() or Mesa_Actual is None:
            print("Debe seleccionar cliente y mesa")
        else:
            subtotal = total
            iva = subtotal * 0.19
            total_pagar = subtotal + iva

            print("\n----- FACTURA -----")
            print("Cliente:", Cliente_Actual["nombre"])
            print("Mesa:", Mesa_Actual["Nombre"])
            print("Subtotal:", subtotal)
            print("IVA:", iva)
            print("Total:", total_pagar)

            ventas.append({
                "cliente": Cliente_Actual["nombre"],
                "mesa": Mesa_Actual["Nombre"],
                "total": total_pagar
            })

    elif Opcion == 6:
        id_cliente = int(input("Ingrese ID: "))

        if id_cliente in cliente:
            print("Cliente encontrado:")
            print(cliente[id_cliente])
        else:
            print("No existe")

    elif Opcion == 7:
        if len(ventas) == 0:
            print("No hay ventas")
        else:
            total_general = 0

            for v in ventas:
                print(v)
                total_general += v["total"]

            print("TOTAL GENERAL:", total_general)

    elif Opcion == 0:
        print("Gracias por usar el sistema")
        break

    else:
        print("Opción inválida")