#Receber dados para cadastrar peças:
#id
#peso
#cor
#comprimento

#avaliar se está aprovada ou reprovada, sob os seguintes critérios de qualidade:
#Peso entre 95 g e 105 g
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
    opcao = input("Selecione uma das seguintes opções: \n")

    if opcao == '1':
        print("Iniciando cadastro de nova peça...\n")


        id_peca = input("Digite o nome da peça: ")
        peso = float(input("Digite o peso da peça (g): "))
        cor = input("Digite a cor da peça: ").lower() # variável precisa ser em minúsculo para ==
        comprimento = float(input("Digite o comprimento da peça (cm): "))
    
    
        # avaliar a peça cadastrada neste momento para aprová-la ou não
        
        motivos_reprovacao = []
        
        # peso entre 95 g e 105 g
        # peso >= 95 e <= 105
        # cor precisa ser azul ou verde
        # cor == azul or verde
        # comprimento entre 10 cm e 20 cm
        # comprimento >=10 e <= 20
        # o que reprovar inclui na lista motivos_reprovacoes

        if not (peso >= 95.00 and peso <= 105.00):
            motivos_reprovacao.append(peso)
        
        if cor not in ['azul', 'verde']:
            motivos_reprovacao.append(cor)
        
        if not comprimento >= 10 and comprimento <= 20:
            motivos_reprovacao.append(comprimento)
        
        
        if len(motivos_reprovacao) == 0:
            status == "Aprovada"
        else:
            status == "Reprovada"

        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento
            "motivos": motivos_reprovacao
            "status": status
        }

        pecas_cadastradas.append(peca) # nesta lista irão todas as peças

        if status == "Aprovada":
            caixa_atual.append(peca)
            print(f"\nPeça {id_peca} aprovada e adicionada") # a peça aprovada vai para a caixa atual (até conter 10)
            # Verificar se a caixa atual já contém 10 para que se possa fechá-la

            if len(caixa_atual) == 10:
                caixa_fechada.append(caixa_atual)
                print("Caixa cheia! Abrindo mais uma caixa...")
        else:
            print(f"\nATENÇÃO! Peça {id_peca} não passou no teste de qualidade")
            print("Seu(s) requisito(s) de qualidade não alcançado(s)")
            for motivos in motivos_reprovacao:
                print(motivos_reprovacao)
    

    elif opcao == '2':
        print("\nListando peças cadastradas...")

        if pecas_cadastradas == 0:
            print("Nenhuma peça cadastrada até o momento")
        else:
            for peca in pecas_cadastradas:
            print(f"peça: " {id_peca}
            "peso: " {peso}
            "cor: " {cor}
            "comprimento: " {comprimento}
            "status: " {status}

            ) # listar a peca selecionada com seus criterios
    
            if status == "Reprovada":
                print(motivos_reprovacao)


    elif opcao == '3':
        print("\nRemovendo peça...")
    
    elif opcao == '4':
        print("\nListando caixas fechadas...")

        for caixa in caixas_fechadas:
            print() # uma caixa fechada é uma caixa atual com 10 pecas cadastradas
    
    elif opcao == '5':
        print("\nGerando relatório...")
    
    elif opcao == '0':
        print("\nSistema encerrado!")
    
    else:
        print("\nOpção inválida! Por favor, digite um número entre 0 e 5.")
    break


