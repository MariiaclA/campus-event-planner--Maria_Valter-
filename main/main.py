import random
from datetime import datetime
# 👥Estudante A: Módulo de Gerenciamento de Eventos
#modelo de evento
evento = {
    "nome" : "teste",
    "data" : "10/09/2026",
    "local" : "Brasília",
    "categoria": "teste"
}


def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def adicionarEvento(listaEventos, nome, data, local, categoria):
    validar = validar_data(data)

    if (validar == True):
        novoEvento = {
            "id": random.randint(),
            "nome" : nome,
            "data" : data,
            "local" : local, 
            "categoria": categoria
        }

        listaEventos.append(novoEvento)

        print("Evento adicionado com sucesso!")
    else:
        print("Não foi possível validar a data do evento")

# Estudante A: Listar todos os eventos
def listarEventos(listaEventos):
    if len(listaEventos) == 0:
        print("Nenhum evento cadastrado")
    else:
        for event in listaEventos:
            print(f"Evento: {event["nome"]}, Data: {event["data"]}, Local: {event["local"]}, Categoria: {event["categoria"]}")
            
#Estudante A: Filtrar eventos por categoria
def procurarEventoPorNome(listaEventos, nome):
    for event in listaEventos:
        if event["nome"].lower() == nome.lower():
            return event
    
    print("Evento não encontrado")
    return None 

    

def deletarEvento(listaEventos, id):
    encontrado = {}
    for event in listaEventos:
        if event["id"] == id:
            encontrado = event
            break
    
    if (encontrado):
        listaEventos.remove(encontrado)
        return 1
    else:
        print("Evento não encontrado")
        return 0






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
