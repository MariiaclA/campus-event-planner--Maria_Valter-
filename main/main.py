# 👥Estudante A: Módulo de Gerenciamento de Eventos
#modelo de evento
evento = {
    "nome" : "teste",
    "data" : "10/09/2026",
    "local" : "Brasília",
    "categoria": "teste"
}

def adicionarEvento(listaEventos, nome, data, local, categoria):

    novoEvento = {
        "nome" : nome,
        "data" : data,
        "local" : local, 
        "categoria": categoria
    }

    listaEventos.append(novoEvento)

def listarEventos(listaEventos):
    if  len(listaEventos) == 0:
        print("Sem eventos !!")
        return
    

    for nv in (listaEventos):
        print("Nome:" + nv["nome"])
        print("Data:" + nv["data"])
        print("Local:" + nv["local"])
        print("Categoria:" + nv["categoria"])











#========================================================================'''



# 👥 Estudante B: Módulo de Interação com Usuário e Relatórios


def menu():
    print("\n1. Adicionar Evento. \n")
    print("\n2. Ver todos os Eventos. \n")
    print("\n3. Filtrar Por Categoria. \n")
    print("\n4. Marcar Evento Como Participado. \n")
    print("\n5. Gerar Relatório. \n")
    print("\n6. Sair")


while True:

    menu()

    try: 
        opcao = int(input())

        match opcao:

            case 1:

                pass
            case 2:
                pass
            case 3:        
                pass
            case 4:
                pass
            case 5:        
                pass
            case 6:
                print("Obrigado, volte sempre.")
                break

    except:
        print("opção inválida")
