'''
En este algoritmo podremos administrar el stock de la itenda "AQUI VENDEMOS"
'''
print('-'*50)
print('Administracion de stock'.center(50, '-'))
print('-'*50)
productos = {'escoba': 5, 'huevos': 25, 'leche': 9}
opciones = ['ver stock del producto', 'añadir producto', 
            'ajustar stock', 'eliminar producto', 'salir']
while True:
    enumerate(opciones)
    ans = input('¿Que quieres hacer?:\n')
    if ans == '1':
        for a in productos.items():
            print(productos)
    elif ans == '2':
        while True:
            nom = input('¿Que productos quiere agregar?')
            if nom.replace(' ', '').isalpha():
                break
            