import random

usuarios = ["usuario_1", "usuario_2","usuario_3","usuario_4","usuario_5","usuario_6","usuario_7","usuario_8", "usuario_9","usuario_10" ]
pass_size = 8
pass_lista = []

#lista de cuentas
cuentasUsuarios = []

# genera cuentas a partir de la lista de nombres de usuarios.
def main():
    #dict que almacenará cada cuenta de usuario.
    
    # recorrer la lista de nombres de usuarios para generar las cuentas.
    for usuario in usuarios :
        cuenta = {}
        cuenta['nick'] = usuario
        cuenta['pass'] = crearPass(pass_size)
        cuenta['telefono'] = solicitarTelefono(usuario)
        cuentasUsuarios.append(cuenta)
    
    # # recorre la lista de cuentas creadas para listarlas
    for usuario in cuentasUsuarios:
        nick = usuario['nick']
        contrasenia = usuario['pass']
        fono = usuario['telefono']
        
        print(f'Usuario : {nick} | Contraseña : {contrasenia} | Teléfono: {fono}')

def crearPass(size):
    while True:
        pass_caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        pass_random = [random.choice(pass_caracteres) for _ in range(size)]
        mayuscula = any(i.isupper() for i in pass_random)
        minuscula = any(i.islower() for i in pass_random)
        digito = any(i.isdigit() for i in pass_random)
        if mayuscula and minuscula and digito:
            pass_random = "".join(pass_random)
            return pass_random

def solicitarTelefono(usuario):
    #preguntará por el numero de telefono hasta que sean 8 dígitos.
    while True:
        fono = input(f'Ingrese el número de teléfono del usuario {usuario} (8 dígitos):  ')
        
        if len(fono) == 8 and fono.isdigit():
            return fono
        else: 
            print("El número de teléfono ingresado deben ser 8 dígitos")


if __name__ == "__main__":
    main()

