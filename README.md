# Lista de Compras - Aplicação Simples

Este projeto é uma aplicação simples em Python que permite ao usuário gerenciar uma lista de compras. O programa oferece funcionalidades para adicionar, remover e visualizar os itens na lista, com tratamento de erros para entradas inválidas e índices inexistentes.

## Funcionalidades

- **Adicionar Produto:** O usuário pode adicionar itens à lista de compras.
- **Remover Produto:** O usuário pode remover um item da lista fornecendo o índice. O código trata casos onde o índice informado não existe.
- **Ver Lista de Compras:** O usuário pode visualizar todos os produtos da lista com seus respectivos índices. Caso a lista esteja vazia, uma mensagem será exibida.

## Como Usar

1. Execute o código em um ambiente Python (IDLE, Jupyter Notebook ou qualquer outro ambiente).
2. O programa apresentará o menu com três opções:
   - **[1] Adicionar**: Insira o nome do produto que deseja adicionar à lista.
   - **[2] Remover**: Informe o índice do produto a ser removido.
   - **[3] Ver lista**: Mostra todos os produtos na lista com seus índices.
3. Caso o usuário forneça um valor inválido, o programa pedirá uma entrada válida.
4. Se um índice inválido for informado para remoção, uma mensagem de erro será exibida.

### Exemplo de Execução

```plaintext
Escolha uma das seguintes opções:
[1]Adicionar
[2]Remover
[3]Ver lista

Escolha uma das seguintes opções:
[1]Adicionar
[2]Remover
[3]Ver lista
1

Informe o produto que deseja adicionar:
Maçã

Escolha uma das seguintes opções:
[1]Adicionar
[2]Remover
[3]Ver lista
3

lista de compras:
0 Maçã
