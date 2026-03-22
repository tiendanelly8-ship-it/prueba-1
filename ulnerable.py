import os
import subprocess

# Simulación de entrada de usuario (vulnerable a command injection)
user_input = input("Ingrese el nombre del archivo: ")

# Vulnerable 1: Concatenación directa en os.system
os.system("cat " + user_input)

# Vulnerable 2: f-string + shell=True en subprocess.call
cmd = f"ls -l {user_input}"
subprocess.call(cmd, shell=True)

# Vulnerable 3: f-string + shell=True en subprocess.run
subprocess.run(f"echo {user_input}", shell=True)

# Caso seguro (no debe detectarse)
os.system("echo 'Sistema listo'")
