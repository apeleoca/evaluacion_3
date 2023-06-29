from libro import *
import numpy as np
import random as rn

arreglo_libr = np.array([])
def grabarLibro(arreglo):
    libr=libro()

    c = False
    while c== False:
        c = libr.setcodigo(input("ingrese el coigo del libro"))

        libr.titulo =input("ingrese el nombre del titulo")
        libr.autor =input("ingrese el autor del libro")

    c = False
    while c == False:
        try:
            c = libr.setPrecio(input("ingrese el precio"))

        except BaseException as error:
            print(f"error{error}")

    c = False
    while c == False:
        try:
            c = libr.setano_public(input("ingrese el año de publicacion del de livro"))

        except BaseException as error:
            print(f"error{error}")

    c = False
    while c == False:
        try:
            c = libr.setcategoria(input(input("ingrese la categoria")))
        except BaseException as error:
            print(f"error{error}")
    return np.append(arreglo_libr)
def buscarLibro(arreglo_libr):
    codigo = input("ingrese el codigo")
    flag = True
    for libro in arreglo_libr :
        if libro.codigo == codigo:
            flag = True
            print("datos del libro")
            print(f"titulo {libro.titulo}")
            print(f"autor {libro.autor}")
            print(f"categoria {libro.categoria}")
            print(f"pais {libro.pais}")
            print(f"precio {libro.precio}")
            if (2023 - libro.ano_public)> 0.30:
                print("libro de edicion especial")
                break
    if flag == False:
        print("el libro no existe")

def imprirLibro(arreglo_libr):
    categoria = input("ingrese categoria")
    flag = True
    total  = 0
    for libro in arreglo_libr:
        if libro.categoria == categoria:
            flag = True
            print("datos del libro")
            print("datos del libro")
            print(f"titulo {libro.titulo}")
            print(f"autor {libro.autor}")
            print(f"categoria {libro.categoria}")
            print(f"pais {libro.pais}")
            print(f"precio {libro.precio}")
            if (2023 - libro.ano_public) > 5 :
                libro.precio = libro.precio *0.85
            total += libro.precio
            print(f"ttotal{total}")
            print("libro de edicion especial")
            break
    if flag == False :
            print("no vallido")




arreglo_libr = np.array([])
ciclo = True


def imprimirlibro(arreglo_libr):
    print("1)informes del pais")
    print("2)informes de categoria")
    try:
        op_imprimir =int(input("seleccione del 1 al 2"))
        nume = rn.randint(1500,5000)
        match op_imprimir:
            case 1:
                imprimirlibro(arreglo_libr)
            case 2:
                imprimirlibro(arreglo_libr)

    except BaseException as error:
        print(f"error{error}")

ciclo =True

while ciclo:

    print("libreria mayor")
    print("--------------")
    print("1)GRABAR")
    print("2)BUSCAR")
    print("3)IMPRIMIR INFORMES")
    print("4)SALIR")
    try:
        op=int(input("seleccionde del 1 al 4"))
        match op :
            case 1:
                print("grabar")
                grabarLibro(arreglo_libr)
            case 2:
                print("buscar")
                buscarLibro(arreglo_libr)

            case 3:
                imprimirlibro(arreglo_libr)

            case 4:
                print("salir")
                ciclo = False

            case _:
                print("opcion no valida")


    except BaseException as error:
        print(f"error{error}")