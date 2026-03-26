# ============================================================
#  TC.5 + PRJ.2 — Algoritmos Recursivos
#  Matemática para Computação
# ============================================================

import sys

# ============================================================
#  CLASSES — Orientação a Objetos
# ============================================================

class Sequencia:
    """TC.5 — Sequência que multiplica por 8, primeiro elemento vale 5."""
    def calcular(self, n):
        if n == 1:
            return 5
        else:
            return self.calcular(n - 1) * 8


class Fatorial:
    """PRJ.2 (a) — Fatorial de n."""
    def calcular(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calcular(n - 1)


class Potencia:
    """PRJ.2 (b) — Base elevado a expoente."""
    def calcular(self, base, exp):
        if exp == 0:
            return 1
        else:
            return base * self.calcular(base, exp - 1)


class Fibonacci:
    """PRJ.2 (c) — N-ésimo termo da série de Fibonacci."""
    def calcular(self, n):
        if n == 1 or n == 2:
            return 1
        else:
            return self.calcular(n - 1) + self.calcular(n - 2)


class Tribonacci:
    """PRJ.2 (d) — N-ésimo termo onde cada termo depende dos 3 anteriores."""
    def calcular(self, n):
        if n == 1 or n == 2 or n == 3:
            return 1
        else:
            return self.calcular(n - 1) + self.calcular(n - 2) + self.calcular(n - 3)


# ============================================================
#  ÁRVORES DE CHAMADAS
# ============================================================

def mostrar_arvore_sequencia(n, nivel=0):
    """Exibe a árvore de chamadas da sequência TC.5."""
    indent = "    " * nivel
    print(f"{indent}sequencia({n})")
    if n == 1:
        print(f"{indent}  └─ retorna 5  [CASO BASE]")
        return 5
    else:
        resultado_anterior = mostrar_arvore_sequencia(n - 1, nivel + 1)
        resultado = resultado_anterior * 8
        print(f"{indent}  └─ retorna {resultado_anterior} * 8 = {resultado}")
        return resultado


def mostrar_arvore_fatorial(n, nivel=0):
    """Exibe a árvore de chamadas do fatorial."""
    indent = "    " * nivel
    print(f"{indent}fatorial({n})")
    if n == 0:
        print(f"{indent}  └─ retorna 1  [CASO BASE]")
        return 1
    else:
        resultado_anterior = mostrar_arvore_fatorial(n - 1, nivel + 1)
        resultado = n * resultado_anterior
        print(f"{indent}  └─ retorna {n} * {resultado_anterior} = {resultado}")
        return resultado


def mostrar_arvore_potencia(base, exp, nivel=0):
    """Exibe a árvore de chamadas da potência."""
    indent = "    " * nivel
    print(f"{indent}potencia({base}, {exp})")
    if exp == 0:
        print(f"{indent}  └─ retorna 1  [CASO BASE]")
        return 1
    else:
        resultado_anterior = mostrar_arvore_potencia(base, exp - 1, nivel + 1)
        resultado = base * resultado_anterior
        print(f"{indent}  └─ retorna {base} * {resultado_anterior} = {resultado}")
        return resultado


def mostrar_arvore_fibonacci(n, nivel=0):
    """Exibe a árvore de chamadas do fibonacci."""
    indent = "    " * nivel
    print(f"{indent}fibonacci({n})")
    if n == 1 or n == 2:
        print(f"{indent}  └─ retorna 1  [CASO BASE]")
        return 1
    else:
        resultado_esquerda = mostrar_arvore_fibonacci(n - 1, nivel + 1)
        resultado_direita  = mostrar_arvore_fibonacci(n - 2, nivel + 1)
        resultado = resultado_esquerda + resultado_direita
        print(f"{indent}  └─ retorna {resultado_esquerda} + {resultado_direita} = {resultado}")
        return resultado


def mostrar_arvore_tribonacci(n, nivel=0):
    """Exibe a árvore de chamadas do tribonacci."""
    indent = "    " * nivel
    print(f"{indent}tribonacci({n})")
    if n == 1 or n == 2 or n == 3:
        print(f"{indent}  └─ retorna 1  [CASO BASE]")
        return 1
    else:
        resultado_esquerda = mostrar_arvore_tribonacci(n - 1, nivel + 1)
        resultado_meio     = mostrar_arvore_tribonacci(n - 2, nivel + 1)
        resultado_direita  = mostrar_arvore_tribonacci(n - 3, nivel + 1)
        resultado = resultado_esquerda + resultado_meio + resultado_direita
        print(f"{indent}  └─ retorna {resultado_esquerda} + {resultado_meio} + {resultado_direita} = {resultado}")
        return resultado


# ============================================================
#  DEMONSTRAÇÃO DE ESTOURO DE PILHA
# ============================================================

def demonstrar_estouro():
    """Demonstra o estouro de pilha (RecursionError)."""
    print("\n--- Demonstração de Estouro de Pilha ---")
    print(f"Limite padrão do Python: {sys.getrecursionlimit()} chamadas recursivas")
    print("Tentando calcular fatorial(10000)...")
    try:
        f = Fatorial()
        f.calcular(10000)
    except RecursionError:
        print("ERRO: RecursionError — estouro de pilha!")
        print("A pilha de chamadas excedeu o limite máximo permitido.")


# ============================================================
#  EXECUÇÃO PRINCIPAL
# ============================================================

if __name__ == "__main__":

    # --- TC.5 ---
    print("=" * 55)
    print("TC.5 — SEQUÊNCIA (multiplica por 8, começa em 5)")
    print("=" * 55)
    s = Sequencia()
    print("Primeiros 5 termos:")
    for i in range(1, 6):
        print(f"  seq({i}) = {s.calcular(i)}")
    print("\nÁrvore de chamadas — sequencia(4):")
    mostrar_arvore_sequencia(4)

    # --- (a) Fatorial ---
    print("\n" + "=" * 55)
    print("PRJ.2 (a) — FATORIAL")
    print("=" * 55)
    f = Fatorial()
    for n in [0, 1, 5, 10]:
        print(f"  fatorial({n}) = {f.calcular(n)}")
    print("\nÁrvore de chamadas — fatorial(4):")
    mostrar_arvore_fatorial(4)

    # --- (b) Potência ---
    print("\n" + "=" * 55)
    print("PRJ.2 (b) — POTÊNCIA")
    print("=" * 55)
    p = Potencia()
    for base, exp in [(2, 10), (3, 4), (5, 3)]:
        print(f"  potencia({base}, {exp}) = {p.calcular(base, exp)}")
    print("\nÁrvore de chamadas — potencia(2, 4):")
    mostrar_arvore_potencia(2, 4)

    # --- (c) Fibonacci ---
    print("\n" + "=" * 55)
    print("PRJ.2 (c) — FIBONACCI")
    print("=" * 55)
    fib = Fibonacci()
    print("Primeiros 8 termos:")
    print(f"  {[fib.calcular(i) for i in range(1, 9)]}")
    print("\nÁrvore de chamadas — fibonacci(5):")
    mostrar_arvore_fibonacci(5)

    # --- (d) Tribonacci ---
    print("\n" + "=" * 55)
    print("PRJ.2 (d) — TRIBONACCI (soma dos 3 anteriores)")
    print("=" * 55)
    trib = Tribonacci()
    print("Primeiros 8 termos:")
    print(f"  {[trib.calcular(i) for i in range(1, 9)]}")
    print("\nÁrvore de chamadas — tribonacci(5):")
    mostrar_arvore_tribonacci(5)

    # --- Estouro de pilha ---
    demonstrar_estouro()

    print("\n" + "=" * 55)
    print("Fim da execução.")
    print("=" * 55)