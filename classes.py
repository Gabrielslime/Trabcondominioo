class Torre:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
    
    def __str__(self):
        return f"Torre: {self.nome}, Endereço: {self.endereco}"
    
    def registrar(self):
        pass

    def imprimir(self):
        return str(self)

class Apartamento:
    def __init__(self, numero):
        self.numero = numero
        self.torre = None
        self.vaga_garagem = 0
    
    def associar_torre(self, torre):
        self.torre = torre
        print("Apartamento associado com sucesso.")
    
    def __str__(self):
        vaga = "Na fila" if self.vaga_garagem > 10 else str(self.vaga_garagem)
        return f"Apartamento: {self.numero}, Torre: {self.torre}, Vaga: {vaga}"
    
    def imprimir(self):
        return str(self)

class FilaEspera:
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.proximo = None
    
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def __iter__(self):
        atual = self.inicio
        while atual:
            yield atual.valor
            atual = atual.proximo
    
    def __str__(self):
        return "\n".join([str(valor) for valor in self]) + "\n"
    
    def __len__(self):
        return self.tamanho
    
    def inserir_na_fila(self, apto):
        novo_nodo = self.Nodo(apto)
        if self.fim is None:
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo
        self.tamanho += 1
    
    def remover_da_fila(self):
        if self.tamanho > 0:
            apto = self.inicio.valor
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
            return apto
        else:
            raise IndexError("Fila vazia.")

class ListaDeAptos:
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.proximo = None
        
        def __str__(self):
            return str(self.valor)
    
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def __getitem__(self, indice):
        if indice < 0:
            indice += self.tamanho
        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice inválido.")
        atual = self.inicio
        for _ in range(indice):
            atual = atual.proximo
        return atual.valor
    
    def __iter__(self):
        atual = self.inicio
        while atual:
            yield atual.valor
            atual = atual.proximo
    
    def __delitem__(self, indice):
        if indice < 0:
            indice += self.tamanho
        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice inválido.")
        if indice == 0:
            self.inicio = self.inicio.proximo
        else:
            atual = self.inicio
            for _ in range(indice - 1):
                atual = atual.proximo
            atual.proximo = atual.proximo.proximo
            if atual.proximo is None:
                self.fim = atual
        self.tamanho -= 1
    
    def __str__(self):
        return "\n".join([str(valor) for valor in self]) + "\n"
    
    def __len__(self):
        return self.tamanho
    
    def inserir_no_fim(self, valor):
        novo_nodo = self.Nodo(valor)
        if self.inicio is None:
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo
        self.tamanho += 1
    
    def inserir_na_posicao(self, indice, valor):
        novo_nodo = self.Nodo(valor)
        if indice <= 0:
            novo_nodo.proximo = self.inicio
            self.inicio = novo_nodo
        else:
            atual = self.inicio
            for _ in range(indice - 1):
                if atual.proximo is None:
                    break
                atual = atual.proximo
            novo_nodo.proximo = atual.proximo
            atual.proximo = novo_nodo
            if novo_nodo.proximo is None:
                self.fim = novo_nodo
        self.tamanho += 1