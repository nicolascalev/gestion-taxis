from store import store

print('Bienvenido al gestor de taxis')
print('1. Ver taxis')
print('2. Ver transacciones')
print('3. Añadir taxi')
print('4. Añadir usuario')
print('5. Usuarios que han usado el servicio')
print('6. Salir')


def findTaxis():
    contador = 1
    for taxi in store['taxis']:
        print(
            f'{contador}. Placa: {taxi["placa"]}, Conductor: {taxi["conductor"]}, Disponible: {taxi["disponible"]}')
        getRide = int(input('1. Solicitar ride 2. Salir'))
        if getRide is 1:
            selectedTaxi = int(input('Digite el número del taxi disponible '))
            createTransaccion(selectedTaxi)
        contador = contador + 1


def createTransaccion(idTaxi):
    contador = 1
    for usuario in store['usuarios']:
        print(
            f'{contador}. Nombre: {usuario["nombre"]}, Teléfono: {usuario["numeroTelefono"]}')
    selectedUser = int(input('Selecciona un usuario '))
    registroUsuario = store['usuarios'][selectedUser - 1]
    store['registroUsuarios'].append(registroUsuario)
    minutos = int(input('Cuánto va a tardar su viaje en minutos?'))
    transaccion = {
        'idTaxi': idTaxi,
        'idUser': selectedUser,
        'minutosViaje': minutos
    }
    store['transacciones'].append(transaccion)


def showRecentUsers():
    contador = 1
    for usuario in store['registroUsuarios']:
        print(f'{contador}. Nombre: {usuario["nombre"]}, Teléfono: {usuario["numeroTelefono"]}')

def findTransacciones():
    contador = 1
    for trans in store['transacciones']:
        print(f'{contador}. Id Taxi: {trans["idTaxi"]}, Id Usuario: {trans["idUser"]}, Minutos: {trans["minutosViaje"]}')


def createTaxi():
    placa = input('Cuál es su número de placa? ')
    conductor = input('Cuál es su nombre? ')
    store['taxis'].append({
        'placa': placa,
        'conductor': conductor,
        'disponible': True
    })


def createUsuario():
    nombre = input('Cuál es su nombre? ')
    numeroTelefono = input('Cuál es su número telefónico? ')
    store['usuarios'].append({
        'nombre': nombre,
        'numeroTelefono': numeroTelefono
    })
    print(f'Usuario creado, usted es {nombre}')


option = int(input('Digite la opcion que desea '))
while option != 6:
    if option == 1:
        findTaxis()
    if option == 2:
        print(findTransacciones())
    if option == 3:
        createTaxi()
    if option == 4:
        createUsuario()
    if option == 5:
        showRecentUsers()
    option = int(input('Digite la opcion que desea '))

print('Hasta luego')
