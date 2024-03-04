class Celula():
    valor=None
    proximo=None
    def __init__(self,valor):
        self.valor=valor
class Fila():
    inicio=None
    fim=None
    def estavazia(self):
        return self.inicio==None
    def inserir(self,valor):
        c=Celula(valor)
        if self.estavazia():
            self.inicio=c
        else:
            self.fim.proximo=c
        self.fim=c
    def deletar(self):
        if not self.estavazia():
            aux=self.inicio
            item=self.inicio.valor
            self.inicio=self.inicio.proximo
            del aux
            return item
    def imprimir(self):
        aux=self.inicio
        while aux!=None:
            print(aux.valor)
            aux=aux.proximo
        print("----------------")
