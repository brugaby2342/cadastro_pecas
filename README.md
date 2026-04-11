# Sistema de Gestão de Peças

Sistema de controle de produção e qualidade de peças, desenvolvido em Python. Permite cadastrar, validar, listar, remover peças e gerenciar seu empacotamento em caixas.

## Funcionalidades

- **Cadastrar peça** — registra uma peça com ID, peso, cor e comprimento, validando automaticamente se ela atende aos critérios de qualidade
- **Listar peças** — exibe todas as peças cadastradas com status (Aprovada/Reprovada) e detalhes das falhas encontradas
- **Remover peça** — remove uma peça pelo ID e reorganiza as caixas automaticamente
- **Listar caixas fechadas** — exibe as caixas já fechadas com suas respectivas peças
- **Gerar relatório final** — exibe totais de peças aprovadas, reprovadas, caixas utilizadas e motivos de reprovação

## Critérios de Qualidade

| Atributo     | Valor aceito             |
|--------------|--------------------------|
| Peso         | 95g a 105g               |
| Cor          | `azul` ou `verde`        |
| Comprimento  | 10cm a 20cm              |

Peças que não atendem a um ou mais critérios são marcadas como **Reprovadas** e não são adicionadas às caixas.

## Empacotamento

Peças aprovadas são automaticamente adicionadas à caixa atual. Quando uma caixa atinge **10 peças**, ela é fechada e uma nova caixa é aberta. Ao remover uma peça, todas as caixas são reorganizadas.

## Como executar

Requer Python 3.

```bash
python main.py
```

## Estrutura do projeto

```
cadastro_de_pecas/
└── main.py   # código principal do sistema
```
