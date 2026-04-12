# 🏭 Sistema de Controle de Produção e Qualidade de Peças

Protótipo desenvolvido em Python para a disciplina **Algoritmos e Lógica de Programação**</br>
**UniFeCAF/Rocketseat · 1º Semestre — Inteligência Artificial e Automação Digital**</br>
README.md mais detalhado para consultas posteriores com fins acadêmicas.

---

## 📋 Sobre o Projeto

Este sistema simula o controle de qualidade de uma linha de produção industrial. Permite automatizar o controle de produção, inspeção de qualidade e armazenamento de peças em uma linha de montagem industrial, substituindo um processo que, feito manualmente, seria suscetível a erros e inconsistências.

### Funcionalidades Menu

* **Cadastrar peça** — registra uma peça com ID, peso, cor e comprimento, validando automaticamente se ela atende aos critérios de qualidade.
* **Listar peças** — exibe todas as peças cadastradas com status (Aprovada/Reprovada) e detalhes das falhas encontradas.
* **Remover peça** — remove uma peça pelo ID e reorganiza as caixas automaticamente.
* **Listar caixas fechadas** — exibe as caixas já fechadas com suas respectivas peças.
* **Gerar relatório final** — exibe totais de peças aprovadas, reprovadas, caixas utilizadas e motivos de reprovação.

---

## :memo: Como funciona

O sistema opera via terminal (linha de comando) através de um menu interativo. Ele recebe os dados de cada peça fabricada e avalia automaticamente se ela está aprovada ou reprovada com base em critérios rigorosos de qualidade.

### Critérios de Qualidade

| Atributo | Valor aceito |
| :--- | :--- |
| **Peso** | 95g a 105g |
| **Cor** | azul ou verde |
| **Comprimento** | 10cm a 20cm |

### Empacotamento

* Peças aprovadas são alocadas automaticamente à caixa atual. Cada caixa comporta no máximo **10 peças**.
* Quando a capacidade é atingida, a caixa é fechada e uma nova é iniciada.
* Peças que não atendem a um ou mais critérios são marcadas como **Reprovadas** e não são adicionadas às caixas.
* Ao remover uma peça, todas as caixas são reorganizadas.

---

## 📌 Exemplos de Entradas e Saídas

Abaixo, alguns exemplos de como o sistema interage com o usuário no terminal.

### Exemplo 1: Cadastrando uma Peça Aprovada

**Entrada:**

Selecione uma das seguintes opções:</br>
1</br>
Iniciando cadastro de nova peça...</br>
Digite o ID da peça: 1</br>
Digite o peso da peça (g): 100</br>
Digite a cor da peça: azul</br>
Digite o comprimento da peça (cm): 15</br>

**Saída**

✔ Peça 1 aprovada e adicionada.

### Exemplo 2: Cadastrando uma Peça Reprovada

**Entrada:**

Selecione uma das seguintes opções:</br>
1</br>
Iniciando cadastro de nova peça...</br>
Digite o ID da peça: 2</br>
Digite o peso da peça (g): 90</br>
Digite a cor da peça: vermelho</br>
Digite o comprimento da peça (cm): 15</br>

**Saída**

✘ ATENÇÃO! Peça 2 não passou no teste de qualidade.</br>
Nem todos os requisitos de qualidade foram alcançados:</br>
- Peso fora do padrão (90.0g)</br>
- Cor inválida (vermelho)

### Exemplo 3: Cadastrando uma Peça Reprovada

**Entrada:**

Selecione uma das seguintes opções:</br>
2

**Saída**

ID: 1 | Status: Aprovada</br>
Medidas: 100.0g, Azul, 15.0cm</br>
ID: 2 | Status: Reprovada</br>
Medidas: 23.0g, Branca, 34.0cm</br>
  Falhas encontradas: Peso fora do padrão (23.0g), Cor inválida (branca), Comprimento fora do padrão (34.0cm)

### Exemplo 4: Gerando Relatório

**Entrada**

Selecione uma das seguintes opções:</br>
5

**Saída**

RELATÓRIO FINAL:</br>
Total de peças cadastradas: 2</br>
✔ Total de peças aprovadas: 1</br>
✘ Total de peças reprovadas: 1</br>
📦 Total de caixas utilizadas (fechadas e em uso): 1</br>
Os motivos para reprovação registrados são:</br>
Peso fora do padrão (90.0g): 1 vez(es)</br>
Cor inválida (vermelho): 1 vez(es)

### Exemplo 4: Remover peça

**Entrada**

Selecione uma das seguintes opções:</br>
3</br>
Digite o ID da peça que você deseja remover: 2

**Saída**

Peça ID 2 removida com sucesso!</br>
Caixas reorganizadas após a remoção da peça 2.

---

## 🚀 Como Rodar o Programa

### Pré-requisitos</br>
Python 3.7 ou superior instalado.

### Verificar a versão do Python:
`python --version`
ou
`python3 --version`

### Passo a passo:
Faça o clone deste repositório ou baixe o arquivo `.py` com o código-fonte.
Abra o terminal (ou prompt de comando) do seu sistema operacional.
Navegue até a pasta onde o arquivo foi salvo usando o comando `cd`.

Execute o programa com o comando:
`python nome_do_arquivo.py`

---

## 🏗 Estrutura do Código

### Funções

| Função | Descrição |
| :--- | :--- |
| `exibir_menu()` | Exibe o menu principal com as opções disponíveis |
| `validar_peca(peso, cor, comprimento)` | Valida os atributos de uma peça e retorna lista de motivos de reprovação |
| `adicionar_a_caixa(peca)` | Adiciona uma peça à caixa atual e fecha a caixa quando cheia |
| `reorganizar_caixas()` | Reconstrói todas as caixas após remoção de uma peça |
| `cadastrar_peca()` | Coleta dados via input, valida e cadastra uma nova peça |
| `listar_pecas()` | Lista todas as peças cadastradas com status e medidas |
| `remover_peca()` | Remove uma peça pelo ID e reorganiza as caixas |
| `listar_caixas()` | Lista as caixas fechadas e o status da caixa atual |
| `gerar_relatorio()` | Gera um relatório com totais e motivos de reprovação |
| `main()` | Loop principal que exibe o menu e despacha as opções |

### Listas

| Variável | Descrição |
| :--- | :--- |
| `pecas_cadastradas` | Armazena todas as peças cadastradas (aprovadas e reprovadas) |
| `caixas_fechadas` | Armazena as caixas que já foram fechadas (cada caixa é uma lista de peças) |
| `caixa_atual` | Armazena as peças da caixa em aberto no momento |
| `motivos` | Lista temporária com os motivos de reprovação de uma peça |

### Dicionários

| Variável | Descrição |
| :--- | :--- |
| `peca` | Dicionário que representa cada peça, com as chaves: id, peso, cor, comprimento, motivos, status |
| `contador_motivos` | Dicionário temporário usado no relatório para contar quantas vezes cada motivo de reprovação aparece |
| `OPCOES` | Dicionário que mapeia cada opção do menu ('1' a '5') para sua função correspondente |

---

## 🛠️ Tecnologias e Conceitos Aplicados

**Python** — linguagem utilizada, sem bibliotecas externas.

**Estrutura de dados:**</br>
*Listas* — armazenamento de peças e caixas.</br>
*Dicionários* — representação de cada peça com seus atributos.</br>
*Conjuntos (set)* — CORES_VALIDAS, para verificação eficiente de pertencimento.

**Funções:**</br>
*Funções puras* — `validar_peca` retorna um resultado sem efeitos colaterais.</br>
*Funções de efeito colateral* — `adicionar_a_caixa`, `reorganizar_caixas` modificam o estado global.

**Controle de fluxo:**</br>
Loop principal `(while True)` — mantém o programa rodando até o usuário sair.</br>
`break` — encerra o loop ao escolher a opção 0.

**Boas práticas:**</br>
Constantes — `PESO_MIN`, `PESO_MAX`, etc., centralizadas no topo.</br>
`if __name__ == "__main__"` — protege a execução ao importar o módulo.</br>
`next()` com valor padrão — busca segura de peça por ID.</br>
Expressões geradoras — `sum(1 for p in ...)` para contagem eficiente.</br>
`.copy()` — tira uma "foto" da caixa cheia antes de limpar a variável para começar de novo.</br>
`f-strings` — formatação de strings legível e direta.</br>

---

## 📄 Licença
Projeto desenvolvido para fins acadêmicos. Uso livre para estudo e referência.

Feito por Bruna Gabriela Ribeiro Sartor</br>
Acadêmica em Inteligência Artificial e Automação Digital

