from collections import defaultdict, Counter
from enum import Enum
import random
'''
    Clase para enumerar los estados de cada producto, 
    el modulo Enum permite definir constantes simbolicas 
    por medio de la enumeración.
'''
class OrderStatus(Enum):
    PENDING = 1 # Pendiente
    SHIPPED = 2 # Enviado 
    DELIVERED = 3 # Entregado

'''
    Funcion que genera una lista random, de un determinado tamaño,
    con los valores proporcionados de la lista de entrada. 
    Simula una lista de pedidos
'''
def generate_order(products: list[str], size: int) -> list[str]:
    # Creacion de una lista de un determinado tamaño.
    return random.choices(products, k=size) # (k=size) permite seleccionar multiples elementos y hasta repetirlos 

'''
    Funcion que permite asignar de forma aleatoria un estado a 
    cada producto de la lista.
    Esta funcion recibe una lista y retorna un objeto de tipo 
    defaultdict.
'''
def assign_status(orders: list[str]) -> defaultdict:
    # Crear un objeto, en base a una lista, y agrupa sus elementos.
    products_count = defaultdict(list)
    for product in orders:
        # Asigna a cada instancia de elemento un "estado" aleatorio.
        products_count[product].append(random.randint(1, 3))
    return products_count

'''
    Funcion para revisar, o traducir, el estatus de cada producto 
    base a su estado (agregado aleatoriamente) usando la 
    enumeracion designada de la clase OrderStatus.
    Esta funcion recibe un objeto de tipo OrderStatus y retorna 
    un string.
'''
def check_order(status: OrderStatus) -> str:
    if status == OrderStatus.PENDING.value:
        return "Pendiente"
    elif status == OrderStatus.SHIPPED.value:
        return "Enviado"
    elif status == OrderStatus.DELIVERED.value:
        return "Entregado"
    else:
        return "Orden no encontrada"

# Lista de productos
products: list[str] = ["laptop", "smartphone", "tablet", "PC"]
# Creacion de la lista.
database = generate_order(products, 10)
# Asignacion aleatoria de estatus a cada producto de la lista.
orders = assign_status(database)

'''
    Bucle de resultados:
    Iteramos dentro de cada tipo de producto, y cada uno de los diferentes
    tipos del mismo. Imprimiendo el tipo de producto, cuantos pedidos 
    fueron (veces que se repitio en la orden), y el estado de cada uno de 
    estos en referencia. Usamos el modulo Counter permite contabilizar bajo
    semejanzas.
'''
for order, status in orders.items(): # Iteramos entre cada elemento del objeto lista pedido.
    # Imprimimos un producto y el numero de veces que aparece repetido en el objeto lista pedido.
    print(f"Producto: {order}, Pedido: {Counter(database)[order]}")
    print("Estado de cada producto de la orden: ")
    # Iteramos entre cada una de las diferentes versiones del mismo producto y revisamos su estatus.
    # la funcion enumerate() permite acceder a el índice (posición) como el valor de cada elemento en 
    # -- una secuencia (como una lista o tupla) mientras la recorres. Devuelve pares de (índice, valor).
    for index, value in enumerate(status):
        print(f"{'- Pedido':>10} #{index + 1}: {check_order(value)}")
