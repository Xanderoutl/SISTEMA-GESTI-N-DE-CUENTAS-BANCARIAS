import os
from datetime import datetime

clientes = {}  # cc -> datos cliente
productos = {}  # id_producto -> datos producto
movimientos = []  # lista de dicts con historial

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    limpiar()
    print("SISTEMA GESTIÓN DE CUENTAS BANCARIAS")
    print("1. Crear cuenta")
    print("2. Depositar dinero")
    print("3. Solicitar crédito")
    print("4. Retirar dinero")
    print("5. Pagar cuota crédito")
    print("6. Cancelar cuenta")
    print("7. Salir")

def crear_cuenta():
    cc = input("Cédula: ").strip()
    if cc in clientes:
        print("Ya existe un cliente con esa cédula.")
        return
    nombre = input("Nombre: ")
    email = input("Email: ")
    edad = input("Edad: ")
    movil = input("Teléfono móvil: ")
    fijo = input("Teléfono fijo: ")
    pais = input("País: ")
    depto = input("Departamento: ")
    ciudad = input("Ciudad: ")

    clientes[cc] = {
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "contacto": {"movil": movil, "fijo": fijo},
        "ubicacion": {"pais": pais, "depto": depto, "ciudad": ciudad},
        "productos": {}
    }
    print("Cliente registrado con éxito.")

def depositar():
    cc = input("Cédula: ").strip()
    if cc not in clientes:
        print("Cliente no encontrado.")
        return
    monto = float(input("Monto a depositar: "))
    # Aquí solo simulo un producto
    if "ahorros" not in clientes[cc]["productos"]:
        clientes[cc]["productos"]["ahorros"] = {"saldo": 0}
    clientes[cc]["productos"]["ahorros"]["saldo"] += monto
    movimientos.append({
        "id": len(movimientos)+1,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "valor": monto,
        "tipo": "deposito"
    })
    print("Depósito realizado.")

# Bucle principal
while True:
    menu()
    op = input("Opción: ").strip()
    if op == "1":
        crear_cuenta()
    elif op == "2":
        depositar()
    elif op == "3":
        print("Solicitar crédito no implementado.")
    elif op == "4":
        print("Retiro no implementado.")
    elif op == "5":
        print("Pago de cuota no implementado.")
    elif op == "6":
        print("Cancelar cuenta no implementado.")
    elif op == "7":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")
