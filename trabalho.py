import time
import math # Importa a biblioteca de matemática

def run_quiz():
    """
    Função principal que executa o quiz de Python com foco em matemática.
    """

    # Define uma largura padrão para os separadores, facilitando a manutenção
    LARGURA_TERMINAL = 90

    perguntas = [
        {
            "pergunta": (
                "1. O código abaixo tenta realizar uma divisão.\n\n"
                "if ______________:\n"
                "    resultado = 100 / divisor\n"
                "    print(f'O resultado é {resultado}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "divisor == 0 - dividir por um número par",
                "b": "divisor != 0 - dividir por zero",
                "c": "divisor > 0 - dividir por um número negativo",
                "d": "divisor < 100 - dividir por um número maior que 100"
            },
            "resposta": "b",
            "explicacao": "A condição 'divisor != 0' (diferente de zero) é essencial para prevenir o erro 'ZeroDivisionError', que ocorre ao tentar dividir qualquer número por zero."
        },
        {
            "pergunta": (
                "2. O objetivo é calcular a raiz quadrada de um número.\n\n"
                "if ______________:\n"
                "    raiz = math.sqrt(numero)\n"
                "    print(f'A raiz é {raiz}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "numero > 0 - calcular a raiz de um número ímpar",
                "b": "numero != 0 - calcular a raiz de zero",
                "c": "numero >= 0 - calcular a raiz quadrada de um número negativo",
                "d": "numero == 0 - calcular a raiz de um número positivo"
            },
            "resposta": "c",
            "explicacao": "A função 'math.sqrt()' só aceita números não negativos (zero ou positivos). A condição 'numero >= 0' garante que o programa não tente calcular a raiz de um número negativo."
        },
        {
            "pergunta": (
                "3. Este código tenta calcular o logaritmo de base 10.\n\n"
                "if ______________:\n"
                "    log = math.log10(x)\n"
                "    print(f'O logaritmo é {log}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "x > 0 - calcular o logaritmo de um número não positivo (zero ou negativo)",
                "b": "x >= 0 - calcular o logaritmo de um número negativo",
                "c": "x != 1 - calcular o logaritmo de 1",
                "d": "x > 10 - calcular o logaritmo de um número menor que 10"
            },
            "resposta": "a",
            "explicacao": "Logaritmos são definidos apenas para números positivos. A condição 'x > 0' exclui tanto o zero quanto os números negativos, evitando o erro."
        },
        {
            "pergunta": (
                "4. O trecho de código visa calcular o fatorial de um número inteiro.\n\n"
                "if ______________:\n"
                "    fatorial = math.factorial(n)\n"
                "    print(f'O fatorial é {fatorial}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "n > 0 - calcular o fatorial de zero",
                "b": "n != 0 - calcular o fatorial de números ímpares",
                "c": "n >= 0 - calcular o fatorial de um número negativo",
                "d": "n < 100 - calcular o fatorial de um número muito grande"
            },
            "resposta": "c",
            "explicacao": "A função fatorial é definida apenas para números inteiros não negativos (0, 1, 2, ...). A condição 'n >= 0' impede que um número negativo seja passado, o que causaria um erro."
        },
        {
            "pergunta": (
                "5. O código deve calcular a operação de módulo (resto da divisão).\n\n"
                "if ______________:\n"
                "    resto = dividendo % divisor\n"
                "    print(f'O resto é {resto}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "divisor != 0 - calcular o módulo por zero",
                "b": "dividendo > divisor - calcular o módulo quando o dividendo é menor",
                "c": "divisor > 0 - calcular o módulo por um número negativo",
                "d": "dividendo != 0 - calcular o módulo de zero"
            },
            "resposta": "a",
            "explicacao": "A operação de módulo é implementada usando a divisão. Portanto, tentar calcular o módulo por zero causa o mesmo erro 'ZeroDivisionError'."
        },
        {
            "pergunta": (
                "6. O código calcula o arco seno de um valor.\n\n"
                "if ______________:\n"
                "    arcoseno = math.asin(valor)\n"
                "    print(f'O arco seno é {arcoseno}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "valor >= 0 - calcular o arco seno de um valor negativo",
                "b": "-1 <= valor <= 1 - calcular o arco seno de um valor fora do intervalo [-1, 1]",
                "c": "valor != 0 - calcular o arco seno de zero",
                "d": "valor > 1 - calcular o arco seno de um valor pequeno"
            },
            "resposta": "b",
            "explicacao": "A função seno só produz valores entre -1 e 1. Consequentemente, a sua função inversa, o arco seno, só aceita valores dentro desse mesmo intervalo."
        },
        {
            "pergunta": (
                "7. Este código eleva uma base a um expoente.\n\n"
                "if ______________:\n"
                "    resultado = base ** expoente\n"
                "    print(f'O resultado é {resultado}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "base != 0 or expoente >= 0 - elevar zero a uma potência negativa",
                "b": "base > 0 and expoente > 0 - usar números negativos",
                "c": "expoente != 0 - elevar um número a zero",
                "d": "base is int and expoente is int - usar números com ponto flutuante"
            },
            "resposta": "a",
            "explicacao": "A operação 0⁻² é equivalente a 1/0², o que causa um erro de divisão por zero. A condição garante que isso não ocorra."
        },
        {
            "pergunta": (
                "8. O código deve criar uma sequência de números com 'range'.\n\n"
                "if ______________:\n"
                "    for i in range(1, 10, passo):\n"
                "        print(i)\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "passo > 10 - usar um passo maior que o limite",
                "b": "passo < 0 - usar um passo negativo",
                "c": "passo != 0 - usar um passo de valor zero",
                "d": "passo == 1 - usar um passo diferente de 1"
            },
            "resposta": "c",
            "explicacao": "A função 'range' não pode ter um passo de valor zero, pois isso criaria um loop infinito. A condição 'passo != 0' previne esse erro."
        },
        {
            "pergunta": (
                "9. O código verifica se três lados podem formar um triângulo.\n\n"
                "if ______________:\n"
                "    print('É um triângulo válido.')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "a + b > c and a + c > b and b + c > a - formar um triângulo com esses lados",
                "b": "a == b and b == c - formar um triângulo escaleno",
                "c": "a**2 + b**2 == c**2 - formar um triângulo qualquer",
                "d": "a + b != c - formar um triângulo equilátero"
            },
            "resposta": "a",
            "explicacao": "A desigualdade triangular afirma que a soma de quaisquer dois lados de um triângulo deve ser maior que o terceiro lado. Esta é a única condição que garante a formação de um triângulo."
        },
        {
            "pergunta": (
                "10. O objetivo é calcular o inverso de um número.\n\n"
                "if ______________:\n"
                "    inverso = 1 / numero\n"
                "    print(f'O inverso é {inverso}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "numero > 1 - calcular o inverso de um número menor que 1",
                "b": "numero != 0 - calcular o inverso de zero",
                "c": "numero < 0 - calcular o inverso de um número positivo",
                "d": "numero == 1 - calcular o inverso de 1"
            },
            "resposta": "b",
            "explicacao": "Calcular o inverso de um número é uma forma de divisão (1 / numero). Portanto, tentar calcular o inverso de zero resulta em um erro de divisão por zero."
        }
    ]

    pontuacao = 0
    titulo_principal = "--- INÍCIO DO QUIZ DE MATEMÁTICA COM PYTHON ---"
    print("=" * LARGURA_TERMINAL)
    print(titulo_principal.center(LARGURA_TERMINAL))
    print("=" * LARGURA_TERMINAL)

    for i, q in enumerate(perguntas):
        print(f"\n{q['pergunta']}")
        print("_" * LARGURA_TERMINAL)
        print("\nQual alternativa preenche corretamente as lacunas para evitar o erro?\n")
        
        for alternativa, texto_opcao in q["opcoes"].items():
            partes = texto_opcao.split(" - ")
            if len(partes) == 2:
                print(f"  {alternativa}) if {partes[0].strip()}:\n     ...")
                print(f"     else:\n         print('Não é possível {partes[1].strip()}')\n")
            else:
                print(f"  {alternativa}) {texto_opcao}\n")

        print("_" * LARGURA_TERMINAL)
        
        resposta_usuario = ""
        while resposta_usuario not in ["a", "b", "c", "d"]:
            resposta_usuario = input("\nQual a sua resposta (a, b, c, d)? ").lower().strip()

        if resposta_usuario == q["resposta"]:
            print("\n✅ Correto!")
            pontuacao += 1
        else:
            print(f"\n❌ Incorreto! A resposta certa era a letra '{q['resposta']}'.")
        
        # Pausa para o usuário ver o resultado antes da próxima pergunta.
        time.sleep(1.5)
        # Adiciona um espaço extra antes da próxima questão para melhor legibilidade.
        print()


    titulo_final = "--- FIM DO QUIZ ---"
    print("\n" + "=" * LARGURA_TERMINAL)
    print(titulo_final.center(LARGURA_TERMINAL))
    print("=" * LARGURA_TERMINAL)
    
    resultado_final = f"Sua pontuação final foi: {pontuacao} de {len(perguntas)}!"
    print("\n" + resultado_final.center(LARGURA_TERMINAL))
    print("\n" + "=" * LARGURA_TERMINAL)

if __name__ == "__main__":
    run_quiz()
