pecas_cadastradas = []  # cada peça com suas características
caixas_fechadas = []    # caixas que já atingiram a capacidade máxima (10)
caixa_atual = []        # caixa que está sendo usada no momento


def exibir_menu():
    print("\n" + "="*30)
    print("SISTEMA DE GESTÃO DE PEÇAS")
    print("="*30)
    print("1. Cadastrar nova peça")
    print("2. Listar peças cadastradas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair do programa")
    print("="*30 + "\n")


while True:
    exibir_menu()
    opcao = input("Selecione uma das seguintes opções: \n")

    if opcao == '1':
        print("Iniciando cadastro de nova peça...\n")

        id_peca = input("Digite o ID da peça: ")
        peso = float(input("Digite o peso da peça (g): "))
        cor = input("Digite a cor da peça: ").strip().lower()
        comprimento = float(input("Digite o comprimento da peça (cm): "))

        motivos_reprovacao = []

        if not (95.00 <= peso <= 105.00):
            motivos_reprovacao.append(f"Peso fora do padrão ({peso}g)")

        if cor not in ['azul', 'verde']:
            motivos_reprovacao.append(f"Cor inválida ({cor})")

        if not (10 <= comprimento <= 20):
            motivos_reprovacao.append(f"Comprimento fora do padrão ({comprimento}cm)")

        # FIX 1: atribuição com = em vez de comparação com ==
        if len(motivos_reprovacao) == 0:
            status = "Aprovada"
        else:
            status = "Reprovada"

        # FIX 11: peca criada depois que status está definido
        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento,
            "motivos": motivos_reprovacao,
            "status": status
        }

        pecas_cadastradas.append(peca)

        if status == "Aprovada":
            caixa_atual.append(peca)
            print(f"\nPeça {id_peca} aprovada e adicionada.")

            if len(caixa_atual) == 10:
                # FIX 2: nome correto da lista é caixas_fechadas
                caixas_fechadas.append(caixa_atual.copy())
                caixa_atual.clear()
                print("Caixa cheia! Abrindo mais uma caixa...")
        else:
            print(f"\nATENÇÃO! Peça {id_peca} não passou no teste de qualidade.")
            print("Seu(s) requisito(s) de qualidade não foi alcançado(s):")
            for motivo in motivos_reprovacao:
                print(f"  - {motivo}")

    elif opcao == '2':
        print("\nListando peças cadastradas...")

        # FIX 3: comparar len() com 0, não a lista diretamente
        if len(pecas_cadastradas) == 0:
            print("Nenhuma peça cadastrada até o momento.")
        else:
            # FIX 4 e 5: indentação correta e ", ".join()
            for peca in pecas_cadastradas:
                print(f"ID: {peca['id']} | Status: {peca['status']}")
                print(f"Medidas: {peca['peso']}g, {peca['cor'].capitalize()}, {peca['comprimento']}cm")

                if peca['status'] == "Reprovada":
                    motivos_nome = ", ".join(peca['motivos'])
                    print(f"  Falhas encontradas: {motivos_nome}")

    elif opcao == '3':
        print("\nRemovendo peça...")

        id_remover = input("Digite o ID da peça que você deseja remover: ")

        peca_encontrada = False

        for peca in pecas_cadastradas:
            if peca['id'] == id_remover:
                pecas_cadastradas.remove(peca)
                peca_encontrada = True
                print(f"Peça ID {id_remover} removida com sucesso!")
                break

        # FIX 6: bloco if/else fora do for, executado após o loop terminar
        if not peca_encontrada:
            print(f"Peça ID {id_remover} não encontrada.")
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

        # FIX 7 e 8: indentação correta do else e remoção do ) indevido na f-string
        if len(caixas_fechadas) == 0:
            print("Nenhuma caixa foi fechada ainda.")
            print(f"Status da caixa atual: {len(caixa_atual)} de 10 peças.")
        else:
            for indice, caixa in enumerate(caixas_fechadas):
                print(f"CAIXA {indice + 1} (10 peças):")

                # FIX 9: sintaxe correta peca['id'] em vez de peca:['id']
                for peca in caixa:
                    print(f"  Peça ID: {peca['id']}; Cor: {peca['cor'].capitalize()}")

    elif opcao == '5':
        print("\nGerando relatório...")

        if len(pecas_cadastradas) == 0:
            print("Não há dados suficientes para gerar o relatório.")
        else:
            total_cadastradas = len(pecas_cadastradas)
            total_aprovadas = 0
            total_reprovadas = 0
            contador_motivos = {}

            for peca in pecas_cadastradas:
                if peca['status'] == "Aprovada":
                    total_aprovadas += 1
                else:
                    total_reprovadas += 1

                    for motivo in peca['motivos']:
                        if motivo in contador_motivos:
                            contador_motivos[motivo] += 1
                        else:
                            contador_motivos[motivo] = 1

            total_caixas = len(caixas_fechadas)
            if len(caixa_atual) > 0:
                total_caixas += 1

            print(f"Total de peças cadastradas: {total_cadastradas}")
            print(f"Total de peças aprovadas: {total_aprovadas}")
            print(f"Total de peças reprovadas: {total_reprovadas}")
            print(f"Total de caixas utilizadas (fechadas e em uso): {total_caixas}")

            if total_reprovadas > 0:
                print("Os motivos para reprovação registrados são:")
                for motivo, quantidade in contador_motivos.items():
                    print(f"  {motivo}: {quantidade} vez(es)")

    elif opcao == '0':
        print("\nSistema encerrado!")
        # FIX 10: break apenas aqui, dentro do bloco do opcao '0'
        break

    else:
        print("\nOpção inválida! Por favor, digite um número entre 0 e 5.")
