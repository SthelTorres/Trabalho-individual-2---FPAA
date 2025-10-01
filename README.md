# trabalho_individual_2_FPAA

## Descrição
Este trabalho implementa o **algoritmo de seleção simultânea do mínimo e do máximo** de uma sequência de números utilizando a técnica de **Divisão e Conquista**.

O programa recebe como entrada uma sequência de números inteiros ou reais e retorna:
- O **menor valor** (`min`)
- O **maior valor** (`max`)
- Opcionalmente, o **número de comparações** realizadas durante a execução (quando usado o parâmetro `--count`).

## Como executar
1. Salve o código no arquivo `main.py`.
2. Execute no terminal:

```bash
python main.py 1 7 3 9 2 5
```
saida esperada:
min=1.0 max=9.0

comdando para exibir também o número de comparações:
```bash
python main.py --count 1 7 3 9 2 5
```
saida esperada:
min=1.0 max=9.0 comparacoes=8

Também é possível fornecer a entrada via stdin:
```bash
echo "1 7 3 9 2 5" | python main.py
```
## Funcionamento do Algoritmo
O algoritmo segue a estratégia recursiva:

## Explicação do Código (linha a linha)
- `_maxmin_divconq(arr)`: Função recursiva que retorna `(min, max, comparacoes)`.
  - `n==0`: lança `ValueError("Sequência vazia.")`.
  - `n==1`: retorna `(arr[0], arr[0], 0)`.
  - `n==2`: faz **1 comparação** entre `a` e `b` e retorna `(min, max, 1)`.
  - `n>2`: divide em duas metades (`arr[:mid]`, `arr[mid:]`), resolve recursivamente e **combina** com **2 comparações**: `min(lmin, rmin)` e `max(lmax, rmax)`.

- `maxmin_select(seq, count=False)`: Interface pública.
  - Converte `seq` em lista, chama `_maxmin_divconq`.
  - Se `count=True`, inclui o total de comparações no retorno.

- `_parse_numbers_from_stdin_or_args(args_list)`: 
  - Se houver números após as opções, usa-os.
  - Senão, lê da **stdin** (aceita espaços ou vírgulas).
  - Se nada for fornecido, mostra instrução de uso e encerra.

- `main(argv=None)`:
  - Lê `--count`, obtém os números (args ou stdin).
  - Chama `maxmin_select` e imprime:
    - `min=... max=...` ou `min=... max=... comparacoes=...`.

- `
if n == 0:
    raise ValueError("Sequência vazia.")`
    - Caso a lista esteja vazia, o programa interrompe a execução e lança um erro, já que não é possível calcular min e max.

- `
if n == 1:
    return arr[0], arr[0], 0`
    - Com apenas um elemento, o menor e o maior são iguais, sem necessidade de comparações.

- `
if n == 2:
    a, b = arr
    if a < b:
        return a, b, 1
    else:
        return b, a, 1`
        - Com dois elementos, basta 1 comparação para decidir quem é o menor e quem é o maior.

- `
mid = n // 2
lmin, lmax, lcomp = _maxmin_divconq(arr[:mid])
rmin, rmax, rcomp = _maxmin_divconq(arr[mid:])`
- Divide a lista em duas metades e resolve cada uma recursivamente. O número de comparações é acumulado.

- `
min_final = min(lmin, rmin)   # 1 comparação
max_final = max(lmax, rmax)   # 1 comparação`
- Combina os resultados parciais com 2 comparações adicionais.
O total de comparações é a soma das comparações das chamadas recursivas mais as 2 comparações finais.


-- Contagem de Comparações Detalhada

- n = 1 → 0 comparações
- n = 2 → 1 comparação
- n = 4 → duas chamadas de n=2 (1 + 1) + 2 comparações na combinação = 4
- n = 6 → divide em 3 e 3:
  - cada lado ≈ 3 comparações
  - total = 3 + 3 + 2 = 8
- n = 8 → duas chamadas de n=4 (4 + 4) + 2 = 10

Percebe-se que, em geral, o número de comparações cresce proporcionalmente a **n**.
Logo, o total é **T(n) ≈ n − 1** comparações, resultando em **O(n)**.


### Casos base:
n = 1 → min = max = único elemento, 0 comparações.
n = 2 → uma única comparação para decidir quem é min e quem é max.

### Passo recursivo:
Divide a sequência em duas metades: esquerda e direita.
Resolve recursivamente em cada metade.
Combina os resultados com 2 comparações:
- Uma para decidir o menor valor global.
- Outra para decidir o maior valor global.

### Exemplo ilustrativo
Para a entrada [1, 7, 3, 9, 2, 5], o algoritmo:
- Divide em [1, 7, 3] e [9, 2, 5]
- Resolve recursivamente cada parte
- Combina com 2 comparações adicionais
- Resultado final: min=1, max=9

## Análise de Complexidade
### Recorrência
Seja T(n) o número de comparações realizadas para um vetor de tamanho n:
T(1) = 0
T(2) = 1
T(n) = T(⌈n/2⌉) + T(⌊n/2⌋) + 2, para n > 2

### Complexidade de tempo
A cada chamada a entrada é dividida ao meio, mas todos os elementos são processados.
Assim, o custo final é Θ(n) comparações.

### Complexidade de espaço
O custo de espaço é O(log n) devido à pilha de chamadas recursivas.

## Exemplo de Comparações
Entrada [1, 7] → comparacoes=1
Entrada [1, 7, 3, 9, 2, 5] → comparacoes=8

O número exato varia conforme o tamanho n, mas cresce de forma linear com a entrada.

## Teorema Mestre

A recorrência do algoritmo é:
T(n) = 2T(n/2) + O(1)

Comparando com a fórmula geral:
T(n) = aT(n/b) + f(n)

Temos:
- a = 2
- b = 2
- f(n) = O(1)

Cálculo de log_b a:
log₂ 2 = 1 → p = 1

Agora, comparamos f(n) com n^p:
- f(n) = O(1) = O(n^0)
- Como 0 < 1, estamos no **Caso 1 do Teorema Mestre**.

Portanto:
T(n) = Θ(n^p) = Θ(n)


## Diagrama de Execução
flowchart TD

  A([Início]) --> Z{Sequência vazia?}
  
  Z -- sim --> X[[Erro: "Sequência vazia"]]
  
  Z -- não --> B{n <= 2?}
  
  B -- sim --> C[Retorna min e max diretamente]
  
  B -- não --> D[Divide em esquerda e direita]
  
  D --> E1[Resolve recursivamente esquerda]
  
  D --> E2[Resolve recursivamente direita]
  
  E1 --> F[Combina resultados<br/>(2 comparações)]
  
  E2 --> F
  
  F --> G([Retorna (min, max)])
  

## Conclusão
O algoritmo MaxMin Select por Divisão e Conquista:
Resolve corretamente o problema de selecionar min e max simultaneamente.
Tem complexidade Θ(n) em tempo e O(log n) em espaço.
Permite contabilizar o número de comparações, fornecendo base para análise experimental.
Foi testado em entradas pequenas e maiores, confirmando a validade da solução.

