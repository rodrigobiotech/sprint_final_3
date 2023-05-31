import random

usuarios = ["usuario_1", "usuario_2","usuario_3","usuario_4","usuario_5","usuario_6","usuario_7","usuario_8", "usuario_9","usuario_10" ]
pass_size = 8
pass_lista = []
space = "--------------------------------------------"
cuentas_usuarios = []

def main():
    for usuario in usuarios :
        cuenta = {}
        cuenta['user'] = usuario
        cuenta['pass'] = crearPass(pass_size)
        cuenta['telefono'] = solicitarTelefono(usuario)
        cuentas_usuarios.append(cuenta)
    
    # # recorre la lista de cuentas creadas para listarlas
    for usuario in cuentas_usuarios:
        user = usuario['user']
        contrasena = usuario['pass']
        phone = usuario['telefono']
        
        print(f'Usuario : {user} | Contraseña : {contrasena} | Teléfono: {phone}')

def crearPass(size):
    while True:
        pass_caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        pass_random = [random.choice(pass_caracteres) for _ in range(size)]
        mayuscula = any(i.isupper() for i in pass_random)
        minuscula = any(i.islower() for i in pass_random)
        digito = any(i.isdigit() for i in pass_random)
        if mayuscula and minuscula and digito:
            pass_random = "".join(pass_random)
            return pass_random

def solicitarTelefono(usuario):
    while True:
        print(space)
        print("Número de teléfono no existente")
        fono = input(f'Ingrese el número de teléfono del usuario {usuario} (8 números):  ')
        
        if len(fono) == 8 and fono.isdigit():
            return fono
        else: 
            print(space)
            print("El número de teléfono ingresado deben ser 8 números")


if __name__ == "__main__":
    main()

