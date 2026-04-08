#Receber dados para cadastrar peças:
#id
#peso
#cor
#comprimento

#avaliar se está aprovada ou reprovada, sob os seguintes critérios de qualidade:
#Peso entre 95 kg e 105 kg
#cor azul ou verde
#comprimento entre 10 cm e 20 cm

#remover peça cadastrada
#armazenar as peças em caixas (10 peças por caixa)
#quando alcancar as 10 peças, fechar a caixa e abrir uma nova

#Relatórios:
#Total de peças aprovadas
#Total de peças reprovadas, com o motivo da reprovação
#Quantidade de caixas

pecas_cadastradas = [] # cada peça com suas características
caixas_fechadas = [] # caixas que já atingiram a capacidade máxima (10)
caixa_atual = [] # caixa que está sendo usada no momento

def exibir_menu():
    print("\n" + "="*30 + "\n")
    print("SISTEMA DE GESTÃO DE PEÇAS")
    print("\n" + "="*30)
    print("1. Cadastrar nova peça")
    print("2. Listar peças cadastradas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair do programa")
    print("="*30 + "\n")


# Exibir o menu para que o usuário digite uma entrada

while True:
    exibir_menu()
    opcao = input("Selecione uma das seguintes opções: ")

    if opcao == '1':
        print("Iniciando cadastro de nova peça...")
        
        id_peca = input("Digite o nome da peça: ")
        peso = float(input("Digite o peso da peça (g): "))
        cor = input("Digite a cor da peça: ")
        comprimento = float(input("Digite o comprimento da peça (cm): "))

        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento
        }
    

    elif opcao == '2':
        print("Listando peças cadastradas...")
    
    elif opcao == '3':
        print("Removendo peça...")
    
    elif opcao == '4':
        print("Listando caixas fechadas...")
    
    elif opcao == '5':
        print("Gerando relatório...")
    
    elif opcao == '0':
        print("Sistema encerrado!")
    
    else:
        print("Opção inválida! Por favor, digite um número entre 0 e 5.")
    break


