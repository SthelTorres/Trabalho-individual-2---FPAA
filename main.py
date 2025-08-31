"""
Seleciona simultaneamente o menor e o maior elemento de uma sequência.
- Abordagem: recursiva (divide and conquer).
- Retorna (min, max) e, opcionalmente, o número de comparações.
"""
from __future__ import annotations
from typing import Iterable, List, Tuple
import sys
import argparse


def _maxmin_divconq(arr: List[float]) -> Tuple[float, float, int]:
    """
    Versão recursiva que retorna (min, max, comparacoes).

    Casos base:
      - n == 1: 0 comparações, min = max = arr[0]
      - n == 2: 1 comparação para decidir min e max
    Passo recursivo:
      - Divide em metades esquerda e direita
      - Resolve recursivamente
      - Combina com 2 comparações (min(left_min, right_min) e max(left_max, right_max))
    """
    n = len(arr)
    if n == 0:
        raise ValueError("Sequência vazia.")
    if n == 1:
        return arr[0], arr[0], 0
    if n == 2:
        a, b = arr[0], arr[1]
        if a < b:
            return a, b, 1
        else:
            return b, a, 1

    mid = n // 2
    lmin, lmax, lc = _maxmin_divconq(arr[:mid])
    rmin, rmax, rc = _maxmin_divconq(arr[mid:])

    # Combinação: 2 comparações
    comparisons = lc + rc
    mn = lmin if lmin < rmin else rmin; comparisons += 1
    mx = lmax if lmax > rmax else rmax; comparisons += 1
    return mn, mx, comparisons


def maxmin_select(seq: Iterable[float], count: bool = False) -> (
    Tuple[float, float] | Tuple[float, float, int]
):
    """
    Função pública: recebe um iterável e aplica a estratégia recursiva.

    :param seq: iterável de números (int/float).
    :param count: se True, retorna também o total de comparações.
    :return: (min, max) ou (min, max, comparacoes)
    """
    arr = list(seq)
    mn, mx, c = _maxmin_divconq(arr)
    return (mn, mx, c) if count else (mn, mx)


def _parse_numbers_from_stdin_or_args(args_list: List[str]) -> List[float]:
    """
    Se houver números após as opções, usa-os.
    Caso contrário, tenta ler da stdin (se houver dados).
    """
    numbers: List[float] = []
    tail = [a for a in args_list if not a.startswith("-")]
    if tail:
        for t in tail:
            numbers.append(float(t))
        return numbers

    if not sys.stdin.isatty():
        data = sys.stdin.read().strip()
        if data:
            for token in data.replace(",", " ").split():
                numbers.append(float(token))
            return numbers
    raise SystemExit(
        "Forneça os números como argumentos ou via stdin. Ex.:\n"
        "  python main.py 1 7 3 9 2 5\n"
        '  echo "1 7 3 9 2 5" | python main.py'
    )


def main(argv: List[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="MaxMin Select (Divide and Conquer)")
    parser.add_argument("--count", action="store_true", help="Exibe também o total de comparações")
    known, unknown = parser.parse_known_args(argv)
    numbers = _parse_numbers_from_stdin_or_args(unknown)

    if len(numbers) == 0:
        raise SystemExit("Nenhum número fornecido.")
    mn_mx = maxmin_select(numbers, count=known.count)
    if known.count:
        mn, mx, c = mn_mx  # type: ignore
        print(f"min={mn} max={mx} comparacoes={c}")
    else:
        mn, mx = mn_mx  # type: ignore
        print(f"min={mn} max={mx}")


if __name__ == "__main__":
    main()
