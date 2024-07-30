from classes import *

lista_aptos = ListaDeAptos()
fila_espera = FilaEspera()

menu_texto = """
----------------------------------------
Sistema de Gestão de Condomínios
----------------------------------------
0 - Sair
1 - Adicionar Torre
2 - Adicionar Apartamento
3 - Listar Apartamentos com Vaga de Garagem
4 - Mostrar Fila de Espera
5 - Remover Apartamento
6 - Adicionar Apartamento à Lista de Espera
7 - Remover Apartamento da Lista de Espera
"""

def adicionar_torre():
    if len(lista_aptos) == 0:
        print("Não é possível adicionar Torres sem apartamentos cadastrados.")
        input("Pressione Enter para continuar.")
    else:
        nome_torre = input("Nome da Torre: ")
        endereco_torre = input("Endereço da Torre: ")
        nova_torre = Torre(nome_torre, endereco_torre)
        if len(lista_aptos) < 10:
            print(str(lista_aptos))
            indice_ap = int(input("Digite o índice do apartamento para esta Torre: "))
            apto = lista_aptos[indice_ap]
            apto.associar_torre(nova_torre)
        else:
            print(str(fila_espera))
            indice_ap = int(input("Digite o número do apartamento na Fila de Espera: "))
            apto = fila_espera[indice_ap]
            apto.associar_torre(nova_torre)

def adicionar_apartamento():
    numero_ap = int(input("Número do Apartamento: "))
    novo_ap = Apartamento(numero_ap)
    if len(lista_aptos) < 10:
        nova_vaga = len(lista_aptos) + 1
        novo_ap.vaga_garagem = nova_vaga
        lista_aptos.inserir_no_fim(novo_ap)
        print("Apartamento adicionado com sucesso.")
    else:
        print("A lista de apartamentos está cheia. Adicione à lista de espera usando a opção 6 do menu.")

def adicionar_apartamento_lista_espera():
    numero_ap = int(input("Número do Apartamento: "))
    novo_ap = Apartamento(numero_ap)
    fila_espera.inserir_na_fila(novo_ap)
    print("Apartamento adicionado à lista de espera com sucesso.")

def remover_apartamento_lista_espera():
    if len(fila_espera) > 0:
        try:
            apto_removido = fila_espera.remover_da_fila()
            print(f"Apartamento removido da fila de espera: {apto_removido}")
        except IndexError as e:
            print(f"Erro ao remover da fila de espera: {e}")
    else:
        print("A lista de espera está vazia.")

def menu():
    while True:
        print(menu_texto)
        opcao = int(input("Opção: "))
        if opcao == 0:
            print("Saindo...")
            break
        elif opcao == 1:
            adicionar_torre()
        elif opcao == 2:
            adicionar_apartamento()
        elif opcao == 3:
            print(str(lista_aptos))
            input("Pressione Enter para continuar.")
        elif opcao == 4:
            print(str(fila_espera))
            input("Pressione Enter para continuar.")
        elif opcao == 5:
            escolha = int(input("Digite 1 para remover da Fila de Espera ou 2 para remover da Lista de Apartamentos: "))
            if escolha == 1:
                remover_apartamento_lista_espera()
            elif escolha == 2:
                print(str(lista_aptos))
                indice_ap = int(input("Digite o índice do apartamento para remover: "))
                del lista_aptos[indice_ap]
                print("Apartamento removido da lista de apartamentos.")
            else:
                print("Opção inválida.")
        elif opcao == 6:
            adicionar_apartamento_lista_espera()
        elif opcao == 7:
            remover_apartamento_lista_espera()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()