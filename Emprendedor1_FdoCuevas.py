print("ADVERTENCIA: Por favor, asegúrate de ingresar números válidos. Los valores negativos o cero pueden causar errores o resultados inesperados.")
# importa librería math
import math
# Solicitud de Inputs
P_Supcripcion = float(input("Ingrese el precio de suscripción en [$]:\n>"))
N_Usuarios = float(input("Ingrese el número de usuarios:\n>"))
G_Totales = float(input("Ingrese los gastos totales en [$]:\n>"))
# Formula
Utilidades = (P_Supcripcion*N_Usuarios)-G_Totales
# Entrega el resultado aproximado al entero siguiente
print(f'Las utilidades de: {math.ceil(Utilidades)} [$]')