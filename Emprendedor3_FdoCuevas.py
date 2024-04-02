print("ADVERTENCIA: Por favor, asegúrate de ingresar números válidos. Los valores negativos o cero pueden causar errores o resultados inesperados.")
# importa librería math
import math
# Solicitud de Inputs
P_Supcripcion = float(input("Ingrese el precio de suscripción en [$]:\n>"))
N_Usuarios = float(input("Ingrese el número de usuarios:\n>"))
G_Totales = float(input("Ingrese los gastos totales en [$]:\n>"))
U_Anterior = float(input("Ingrese las utilidades del año anterior en [$]:\n>"))
# Formula
# aproximación al sgte entero
U_Actual = math.ceil((P_Supcripcion*N_Usuarios)-G_Totales)
# aproximación a 2 decimal
RazonUtil = round(100*(U_Anterior/U_Actual),2)
# Resultado 
print(f'La utilidad actual es de: {U_Actual} [$]')
print(f'Razón Utilidad Actual / Utilidad Anterior: {RazonUtil:.2f} [%]')