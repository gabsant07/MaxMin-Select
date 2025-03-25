# MaxMin-Select

## Descrição do Projeto

O projeto MaxMin Select consiste na implementação de um algoritmo eficiente para encontrar simultaneamente o maior e o menor elemento de uma sequência de números. Utilizando a técnica de divisão e conquista, o algoritmo reduz o número de comparações em relação a abordagens ingênuas. O projeto foi desenvolvido em Python, visando eficiência e clareza na lógica de implementação.

## Objetivo

O objetivo do projeto é aplicar a técnica de divisão e conquista para encontrar o maior e o menor elementos com a menor complexidade possível, garantindo eficiência em grandes conjuntos de dados.

## Abordagem e Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

### main.py: Contém a implementação do algoritmo MaxMin Select.

### analyze.py: Realiza a análise de complexidade do algoritmo.

### README.md: Documentação completa com explicação da lógica, instruções de execução e análise de complexidade.

## Estrutura dos Arquivos

### main.py: Implementa a função principal que executa o algoritmo.

### analyze.py: Realiza a contagem de operações e apresenta a complexidade assintótica.

### tests/: Conjunto de testes para validação do algoritmo.

## Como executar o projeto

1. Clone o repositório:
   git clone https://github.com/gabsant07/MaxMin-Select.git
   cd MaxMinSelect

2. Crie um ambiente virtual:
   python3 -m venv .venv

3. Ative o ambiente virtual:
   .venv\Scripts\activate

4. Instale as dependências:
   pip install -r requirements.txt

5. Execute o programa:
   python main.py

## Análise de complexidade 

O algoritmo MaxMin Select utiliza a técnica de divisão e conquista, reduzindo o número de comparações para 3n/2 - 2. Isso proporciona uma complexidade assintótica de O(n). A análise detalhada pode ser encontrada no arquivo analyze.py.

## Análise com o Teorema Mestre

A relação de recorrência utilizada é:

T(n) = 2T(n/2) + O(1)

a = 2 (divisão em duas partes)
b = 2 (tamanho dividido ao meio)
f(n) = O(1)

## Complexidade Temporal

De acordo com o Teorema Mestre:

T(n) = O(n)

A eficiência do algoritmo está garantida pela estratégia de divisão e conquista, evitando comparações redundantes.

## Exemplo de saída

Analisando o conjunto: [23, 5, 1, 18, 99, 3]

Maior elemento: 99

Menor elemento: 1

Número de comparações: 8
