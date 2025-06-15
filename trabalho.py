import time
import math
import cmath

def run_quiz():
    """
    Função principal que executa o quiz de Python com foco em matemática avançada.
    """
    LARGURA_TERMINAL = 90

    perguntas = [
        {
            "pergunta": (
                "1. Para resolver a equação `ax² + bx + c = 0` e encontrar **raízes reais**, qual condição o código deve verificar?\n\n"
                "if ______________:\n"
                "    # Código para calcular as raízes reais aqui...\n"
                "    print('A equação possui raízes reais.')\n"
                "else:\n"
                "    print('A equação não possui raízes reais ou não é quadrática.')"
            ),
            "opcoes": {
                "a": "a != 0 and (b**2 - 4*a*c) >= 0 - validar e calcular raízes reais",
                "b": "a != 0 - garantir que a equação é quadrática, mas não que as raízes são reais",
                "c": "(b**2 - 4*a*c) >= 0 - garantir raízes reais, mas não que a equação é quadrática",
                "d": "b > 0 and c > 0 - validar apenas coeficientes positivos"
            },
            "resposta": "a",
            "explicacao": "Para a equação ser quadrática, `a` deve ser diferente de zero. Para que as raízes sejam reais, o discriminante (`b² - 4ac`) deve ser maior ou igual a zero. Ambas as condições são necessárias."
        },
        {
            "pergunta": (
                "2. O código calcula o logaritmo de 'x' em uma 'base' customizada.\n\n"
                "if ______________:\n"
                "    logaritmo = math.log(x, base)\n"
                "    print(f'O resultado é {logaritmo}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "x > 0 and base > 0 - usar uma base igual a 1 ou negativa",
                "b": "x > 0 and base != 1 - usar um logaritmando negativo",
                "c": "x > 0 and base > 0 and base != 1 - calcular o logaritmo com argumentos inválidos",
                "d": "isinstance(x, int) and isinstance(base, int) - usar uma base fracionária"
            },
            "resposta": "c",
            "explicacao": "A função logarítmica tem três restrições: o logaritmando 'x' deve ser positivo (`x > 0`), e a 'base' deve ser positiva (`base > 0`) e diferente de 1 (`base != 1`)."
        },
        {
            "pergunta": (
                "3. O código deve determinar se um 'ano' é bissexto no calendário Gregoriano.\n\n"
                "if ______________:\n"
                "    print(f'{ano} é bissexto.')\n"
                "else:\n"
                "    print('A regra não foi aplicada corretamente.')"
            ),
            "opcoes": {
                "a": "ano % 4 == 0 and ano % 100 != 0 - identificar incorretamente anos como 2000",
                "b": "(ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0) - identificar corretamente um ano bissexto",
                "c": "ano % 4 == 0 or ano % 400 == 0 - identificar incorretamente anos como 1900",
                "d": "ano % 4 == 0 - aplicar a regra mais simples e incorreta"
            },
            "resposta": "b",
            "explicacao": "A regra completa e correta para um ano bissexto é uma lógica composta: o ano deve ser divisível por 400, OU divisível por 4 mas não por 100."
        },
        {
            "pergunta": (
                "4. O código usa a Lei dos Cossenos para encontrar um ângulo (em radianos) a partir dos lados 'a', 'b', 'c'.\n\n"
                "if ______________:\n"
                "    # A fórmula é acos((a² + b² - c²) / (2ab))\n"
                "    valor_acos = (a**2 + b**2 - c**2) / (2 * a * b)\n"
                "    angulo = math.acos(valor_acos)\n"
                "    print(f'O ângulo oposto ao lado c é {angulo:.2f} radianos.')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "a > 0 and b > 0 and c > 0 - formar um triângulo com lados inválidos (ex: 1, 2, 5)",
                "b": "a + b > c and a + c > b and b + c > a - formar um triângulo válido",
                "c": "a != 0 and b != 0 - ignorar a desigualdade triangular",
                "d": "a**2 + b**2 != c**2 - calcular apenas para triângulos não retângulos"
            },
            "resposta": "b",
            "explicacao": "Para que os lados formem um triângulo, a desigualdade triangular (`a+b > c`, etc.) deve ser satisfeita. Essa condição também garante que o argumento de `acos` estará no intervalo válido de [-1, 1]."
        },
        {
            "pergunta": (
                "5. O código deve simplificar uma fração 'numerador/denominador' para sua forma irredutível.\n\n"
                "if ______________:\n"
                "    divisor_comum = math.gcd(numerador, denominador)\n"
                "    num_simplificado = numerador // divisor_comum\n"
                "    den_simplificado = denominador // divisor_comum\n"
                "    print(f'A fração simplificada é {num_simplificado}/{den_simplificado}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "denominador != 0 - usar um denominador zero",
                "b": "isinstance(numerador, int) and isinstance(denominador, int) - usar números não inteiros",
                "c": "math.gcd(numerador, denominador) > 1 - simplificar frações já irredutíveis",
                "d": "isinstance(numerador, int) and isinstance(denominador, int) and denominador != 0 - simplificar uma fração inválida"
            },
            "resposta": "d",
            "explicacao": "Três condições são cruciais: o denominador não pode ser zero, e tanto o numerador quanto o denominador devem ser inteiros para que a função `math.gcd` (Máximo Divisor Comum) funcione corretamente."
        },
        {
            "pergunta": (
                "6. Para calcular a **soma e o produto** das raízes de `ax² + bx + c = 0` (Relações de Girard), qual é a única condição essencial sobre os coeficientes?\n\n"
                "if ______________:\n"
                "    soma_raizes = -b / a\n"
                "    produto_raizes = c / a\n"
                "    print(f'Soma={soma_raizes}, Produto={produto_raizes}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "a != 0 - calcular a soma e o produto",
                "b": "a != 0 and (b**2 - 4*a*c) >= 0 - encontrar as raízes, não apenas sua soma/produto",
                "c": "b != 0 and c != 0 - ignorar o coeficiente 'a'",
                "d": "(b**2 - 4*a*c) >= 0 - garantir raízes reais, o que não é necessário para a soma/produto"
            },
            "resposta": "a",
            "explicacao": "As Relações de Girard (Soma = -b/a, Produto = c/a) funcionam até para raízes complexas. A única condição para o cálculo é que `a` seja diferente de zero, para que a divisão seja possível e a equação seja do segundo grau."
        },
        {
            "pergunta": (
                "7. O código calcula as coordenadas do **vértice** de uma parábola `y = ax² + bx + c`. Qual é a condição fundamental para que o vértice possa ser calculado?\n\n"
                "if ______________:\n"
                "    xv = -b / (2 * a)\n"
                "    yv = -(b**2 - 4*a*c) / (4 * a)\n"
                "    print(f'O vértice é ({xv}, {yv})')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "a != 0 - calcular o vértice de uma parábola",
                "b": "(b**2 - 4*a*c) >= 0 - confundir com a condição para raízes reais",
                "c": "a > 0 - calcular o vértice apenas para parábolas com concavidade para cima",
                "d": "b != 0 and c != 0 - calcular o vértice apenas quando b e c não são zero"
            },
            "resposta": "a",
            "explicacao": "O cálculo do vértice, tanto para a coordenada x (`-b/2a`) quanto para a y (`-Δ/4a`), envolve a divisão por 'a'. Portanto, a única condição necessária é que `a` seja diferente de zero, para que a equação seja de fato uma parábola e a divisão seja possível."
        },
        {
            "pergunta": (
                "8. O código valida coordenadas de GPS (latitude e longitude) em graus.\n\n"
                "if ______________:\n"
                "    print('Coordenadas válidas.')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "lat >= -90 and lat <= 90 - validar as coordenadas",
                "b": "lon >= -180 and lon <= 180 - validar as coordenadas",
                "c": "(lat >= -90 and lat <= 90) and (lon >= -180 and lon <= 180) - validar um par de coordenadas (lat, lon)",
                "d": "lat != 0 and lon != 0 - proibir coordenadas na Linha do Equador ou Meridiano de Greenwich"
            },
            "resposta": "c",
            "explicacao": "A validação de coordenadas GPS exige a verificação de ambos os valores: a latitude deve estar no intervalo de [-90, 90] graus, e a longitude deve estar no intervalo de [-180, 180] graus."
        },
        {
            "pergunta": (
                "9. O código calcula a **hipotenusa** de um triângulo retângulo a partir de seus dois catetos. Qual é a condição que garante que os catetos têm comprimentos válidos?\n\n"
                "if ______________:\n"
                "    hipotenusa = math.hypot(cateto_a, cateto_b)\n"
                "    print(f'A hipotenusa é {hipotenusa:.2f}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "cateto_a != 0 and cateto_b != 0 - calcular a hipotenusa (permite lados negativos)",
                "b": "cateto_a >= 0 and cateto_b >= 0 - calcular a hipotenusa (permite lados com valor zero)",
                "c": "cateto_a > 0 and cateto_b > 0 - calcular a hipotenusa com lados válidos",
                "d": "isinstance(cateto_a, (int, float)) - verificar apenas o tipo, não o valor dos lados"
            },
            "resposta": "c",
            "explicacao": "Para formar um triângulo retângulo válido, os comprimentos dos catetos devem ser valores estritamente positivos. Lados com comprimento zero ou negativo não são geometricamente possíveis."
        },
        {
            "pergunta": (
                "10. O código calcula o comprimento da **circunferência** de uma esfera. Qual condição garante que o raio da esfera é um valor geometricamente válido?\n\n"
                "if ______________:\n"
                "    circunferencia = 2 * math.pi * raio\n"
                "    print(f'A circunferência da esfera é {circunferencia:.2f}')\n"
                "else:\n"
                "    print('Não é possível ______________.')"
            ),
            "opcoes": {
                "a": "raio >= 0 - calcular a circunferência (permite uma esfera de raio zero)",
                "b": "raio > 0 - calcular a circunferência de uma esfera com raio válido",
                "c": "isinstance(raio, (int, float)) - apenas verificar se o raio é um número",
                "d": "raio != 1 - proibir o cálculo para uma esfera de raio unitário"
            },
            "resposta": "b",
            "explicacao": "O raio de uma esfera, sendo uma medida de comprimento, deve ser um valor estritamente positivo para que a esfera tenha uma dimensão real e uma circunferência mensurável. Um raio zero ou negativo não define uma esfera no sentido geométrico usual."
        }
    ]

    # O restante do código que executa o quiz permanece o mesmo...
    pontuacao = 0
    titulo_principal = "--- INÍCIO DO QUIZ DE MATEMÁTICA E LÓGICA ---"
    print("=" * LARGURA_TERMINAL)
    print(titulo_principal.center(LARGURA_TERMINAL))
    print("=" * LARGURA_TERMINAL)

    for i, q in enumerate(perguntas):
        print(f"\n{q['pergunta']}")
        print("_" * LARGURA_TERMINAL)
        
        print("\nQual alternativa preenche a lacuna para a lógica correta?\n")
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
            print(f"💡 Explicação: {q['explicacao']}")
            pontuacao += 1
        else:
            print(f"\n❌ Incorreto! A resposta certa era a letra '{q['resposta']}'.")
            print(f"💡 Explicação: {q['explicacao']}")
        
        time.sleep(3)
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