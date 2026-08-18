# 👥Estudante A: Módulo de Gerenciamento de Eventos












'''========================================================================'''



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
