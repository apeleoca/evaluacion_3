class libro:
    codigo=''
    precio=0
    titulo=''
    autor=''
    pais=''
    categoria=''
    ano_public=0

    def __int__(self):
        self.codigo='ACC-022'
        self.precio=10000
        self.titulo='50 SOMBRAS DE JUANIN'
        self.autor="Janin juan harrys"
        self.pais='chile'
        self.categoria='novela'
        self.ano_public=2017

    def setPrecio(self,precio):
        if precio >=10000 and precio <=150000:
            self.precio=precio
            return True
        else:
            print ("el valor del livro  es incorrecto")
            return False


    def setano_publicacion(self,ano_public):
        if ano_public >= 1780 and ano_public <= 2023:
            self.ano_public=ano_public
            return True
        else:
            print("el año del libro es incorrecto")
            return False

    def setcodigo(self,codigo):
        if codigo[0:3].isdigit() and (codigo).isalpha() and codigo[4:7].isdigit():
            self.codigo=codigo
            return True
        else:
            print("el codigo es invalido")
            return False


    def setcategoria(self,categoria):
        if categoria is 'NOVELA' or 'FANTASIA' or 'ACCION':
            self.categoria
            return
        else:
            print("categoria no valida")
            return False
