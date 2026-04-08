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


id = input('Peça: ')
peso = float(input('Qual o peso da peça: '))
cor = input('Qual a cor da peça: ')
comprimento = float(input('Qual o comprimento da peça: '))

pecas_cadastradas = [] # cada peça com suas características
caixas_fechadas = []
caixa_atual = []

def exibir_menu():
    print('Sistema de Gestão de Peças')
    print('1. Cadastrar nova peça')
    print('2. Listar peças cadastradas')
    print('3. Remover peça cadastrada')
    print('4. Listar caixas')
    print('5. Gerar relatório final')
    print('0. Sair do programa')
