import persistencia_pickle as pp
import car_class
import random as rd
FILE = "Coches_obj.txt"

lista_coches = pp.retrive(FILE)
if lista_coches == None:
    lista_coches = []

while True:
    marca = input("marca :")
    if marca == "fin":
        break
    modelo = input("modelo: ")
    combustible = input("cilindrada: ")
    cilindrada = input("cilindrada: ")
    ancho = input("ancho de la rueda: ")
    rodadura = input("rodadura: ")
    diametro = input("diametro: ")

    wheel = car_class.wheel(ancho, rodadura, diametro)
    coches = car_class.car(marca, modelo, combustible, cilindrada, wheel)

    lista_coches.append(coches)

    coches.wheel.set_presure(input("presion deseada :"))

    coches.move_to(rd.random()+100, rd.random()+600)
    print("position: ", coches.get_pos)
    coches.move_inc(rd.random()+10, rd.random()+60)
    print("position: ", coches.get_pos)
    del (coches)
    del (wheel)

pp.store(lista_coches, FILE)
lista_coches = []
print(lista_coches)

lista_coches = pp.retrieve(FILE)
for car in lista_coches:
    print("marca :", car.marca)
    print("modelo :", car.modelo)
    print("tipo de combustible: ", car.combustible)
    print("cilindrada : ", car.cilindrada)
    print(car.wheel.print_info())
    print("posicion: ",car. get_pos)

