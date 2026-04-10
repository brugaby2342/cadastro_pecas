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


        id_peca = input("Digite o ID da peça: ")
        peso = float(input("Digite o peso da peça (g): "))
        cor = input("Digite a cor da peça: ").strip().lower() # variável precisa ser em minúsculo para ==
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

        if not ( 95.00 <= peso <= 105.00):
            motivos_reprovacao.append(f"Peso fora do padrão ({peso}g)")
        
        if cor not in ['azul', 'verde']:
            motivos_reprovacao.append(f"Cor inválida ({cor})")
        
        if not (10 <= comprimento <= 20):
            motivos_reprovacao.append(f"Comprimento fora do padrão ({comprimento}cm)")
        
        
        if len(motivos_reprovacao) == 0:
            status == "Aprovada"
        else:
            status == "Reprovada"

        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento,
            "motivos": motivos_reprovacao,
            "status": status
        }

        pecas_cadastradas.append(peca) # nesta lista irão todas as peças

        if status == "Aprovada":
            caixa_atual.append(peca)
            print(f"\nPeça {id_peca} aprovada e adicionada") # a peça aprovada vai para a caixa atual (até conter 10)
            # Verificar se a caixa atual já contém 10 para que se possa fechá-la

            if len(caixa_atual) == 10:
                caixa_fechada.append(caixa_atual.copy())
                caixa_atual.clear()
                print("Caixa cheia! Abrindo mais uma caixa...")
        else:
            print(f"\nATENÇÃO! Peça {id_peca} não passou no teste de qualidade")
            print("Seu(s) requisito(s) de qualidade não foi alcançado(s)")
            for motivo in motivos_reprovacao:
                print(f" - {motivo}")
    

    elif opcao == '2':
        print("\nListando peças cadastradas...")

        if pecas_cadastradas == 0:
            print("Nenhuma peça cadastrada até o momento")
        else:
            for peca in pecas_cadastradas:
            print(f"ID: {peca['id']} | Status: {peca['status']}")
            print(f"Medidas: {peca['peso']}g, {peca['cor'].capitalize()}, {peca['comprimento']}cm")

             
            if peca['status'] == "Reprovada":
                motivos_nome = .join(peca['motivos'])
                print(f"Falhas encontradas: {motivos_nome}")


    elif opcao == '3':
        print("\nRemovendo peça...")

        # precisamos remover a peça da lista geral (pecas_cadastradas)
        # esvaziar todas as caixas
        # reagrupar todas as peças que sobraram, guardando nas caixas as aprovadas

        id_remover = input("Digite o ID da peça você deseja remover: ")

        peca_encontrada = False # partimos do ponto em que ainda não encontramos a peça solicitada
        
        for peca in pecas_cadastradas:
            if peca['id'] == id_remover:
                pecas_cadastradas.remove(peca)
                peca_encontrada = True # encontramos a peça
                print(f"Peça ID {id_remover} removida com sucesso!")
                break # parar o fluxo porque a peça já foi encontrada

            if not peca_encontrada:
                print(f"Peça ID {id_remover} não encontrada") # para o caso do usuário digitar um id inexistente
            else:
                caixas_fechadas.clear()
                caixa_atual.clear()

                for peca in pecas_cadastradas:
                    if peca['status'] == "Aprovada":
                        caixa_atual.append(peca)

                        if len(caixa_atual) == 10:
                            caixas_fechadas.append(caixa_atual.copy())
                            caixa_atual.clear()
                
                print(f"Caixas reorganizadas após a remoção da peça {id_remover}.")

                


    
    elif opcao == '4':
        print("\nListando caixas fechadas...")

        if len(caixas_fechadas) == 0:
            print("Nenhuma caixa foi fechada ainda.")
            print(f"Status da caixa atual): {len(caixa_atual)} de 10 peças.")
        else:

        for indice, caixa in enumerate(caixas_fechadas): # dá um número a cada caixa da lista caixas_fechadas
            print(f"CAIXA {indice + 1} (10 peças)") # uma caixa fechada é uma caixa atual com 10 pecas cadastradas
            # percorrer as peças dentro da caixa selecionada acima

            for peca in caixa:
                print(f"Peça ID: {peca:['id']}; {peca:['cor']}")
    
    elif opcao == '5': # percorrer as listas, contar os totais e agrupar os motivos de reprvação (total peças cadastradas, reprovadas com motivos e total de caixas)
        print("\nGerando relatório...")

        if len(pecas_cadastradas) == 0:
            print("Não há dados suficientes para gerar o relatório")
        else:
            total_cadastradas = len(pecas_cadastradas)
            
            total_aprovadas = 0
            total_reprovadas = 0
            contador_motivos = {} # a quantidade de vezes que aquele motivo foi reportado

            for peca in pecas_cadastradas:
                if peca['status'] == "Aprovada":
                    total_aprovadas += 1
                else:
                    total_reprovadas += 1

                    for motivo in peca['motivos']:
                        # se já há algum registro com aquele motivo, soma + 1
                        if motivo in contador_motivos:
                            contador_motivos[motivo] += 1
                        # se for a primeira vez que esse mmotivo aparece, cria 1
                        else:
                            contador_motivos[motivo] = 1
            
            total_caixas = len(caixas_fechadas)
            # se tiver alguma caixa aberta, precisa contá-la também, pois está sendo utilizada
            if len(caixa_atual) > 0:
                total_caixas += 1
            
            print(f"Total de peças cadastradas: {total_cadastradas}")
            print(f"Total de peças aprovadas: {total_aprovadas}")
            print(f"Total de peças reprovadas: {total_reprovadas}")
            print(f"Total de caixas utilizadas (fechadas e em uso): {total_caixas}")

            if total_reprovadas > 0:
                print("Os motivos para reprovação registrados são:")

                for motivo, quantidade in contador_motivos.items():
                    print(f"{motivo}: {quantidade} vezes")

    
    elif opcao == '0':
        print("\nSistema encerrado!")
    
    else:
        print("\nOpção inválida! Por favor, digite um número entre 0 e 5.")
    break


