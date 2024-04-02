# importa librería math
import math
# Solicitud de Inputs
C_gravitacional = float(input("Ingrese la constante gravitacional en [m/s²]:\n>"))
R_planeta = float(input("Ingrese el radio del planeta en [km]:\n>"))
# Radio en metros
radio_planeta = R_planeta*1000
# Formula de velocidad de escape
V_escape =math.sqrt (2*C_gravitacional*radio_planeta)
# Resultado aproximado a un decimal
print(f'La velocidad de Escape es de: {round(V_escape,1)} [m/s]')

