import tkinter as tk
from tkinter import messagebox

class QuizApp:
    """
    Classe que encapsula a lógica e a interface do quiz usando Tkinter.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz de Matemática e Lógica com Python")
        self.root.geometry("900x650") # Aumentando a altura para melhor visualização
        self.root.resizable(False, False)

        # Configuração de estilo
        self.BG_COLOR = "#2c3e50"
        self.TEXT_COLOR = "#ecf0f1"
        self.CORRECT_COLOR = "#27ae60"
        self.INCORRECT_COLOR = "#c0392b"
        self.BUTTON_COLOR = "#3498db"
        self.BUTTON_TEXT_COLOR = "#ffffff"
        self.FONT_NORMAL = ("Helvetica", 12)
        self.FONT_BOLD = ("Helvetica", 14, "bold")
        self.FONT_QUESTION = ("Consolas", 14) # Fonte monoespaçada para código

        self.root.configure(bg=self.BG_COLOR)

        self.perguntas = [
            # ... (sua lista de perguntas vai aqui, sem alterações) ...
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
                    "a": "a != 0 and (b**2 - 4*a*c) >= 0",
                    "b": "a != 0",
                    "c": "(b**2 - 4*a*c) >= 0",
                    "d": "b > 0 and c > 0"
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
                    "    print('Não é possível calcular o logaritmo com argumentos inválidos.')"
                ),
                "opcoes": {
                    "a": "x > 0 and base > 0",
                    "b": "x > 0 and base != 1",
                    "c": "x > 0 and base > 0 and base != 1",
                    "d": "isinstance(x, int) and isinstance(base, int)"
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
                    "a": "ano % 4 == 0 and ano % 100 != 0",
                    "b": "(ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)",
                    "c": "ano % 4 == 0 or ano % 400 == 0",
                    "d": "ano % 4 == 0"
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
                    "    print('Não é possível formar um triângulo válido.')"
                ),
                "opcoes": {
                    "a": "a > 0 and b > 0 and c > 0",
                    "b": "a + b > c and a + c > b and b + c > a",
                    "c": "a != 0 and b != 0",
                    "d": "a**2 + b**2 != c**2"
                },
                "resposta": "b",
                "explicacao": "Para que os lados formem um triângulo, a desigualdade triangular (`a+b > c`, etc.) deve ser satisfeita. Essa condição também garante que o argumento de `acos` estará no intervalo válido de [-1, 1]."
            },
            {
                "pergunta": (
                    "5. O código deve simplificar uma fração 'numerador/denominador' para sua forma irredutível.\n\n"
                    "if ______________:\n"
                    "    divisor_comum = math.gcd(numerador, denominador)\n"
                    "    # ... código de simplificação ...\n"
                    "else:\n"
                    "    print('Não é possível simplificar uma fração inválida.')"
                ),
                "opcoes": {
                    "a": "denominador != 0",
                    "b": "isinstance(numerador, int) and isinstance(denominador, int)",
                    "c": "math.gcd(numerador, denominador) > 1",
                    "d": "isinstance(numerador, int) and isinstance(denominador, int) and denominador != 0"
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
                    "else:\n"
                    "    print('Não é possível calcular a soma e o produto.')"
                 ),
                "opcoes": {
                    "a": "a != 0",
                    "b": "a != 0 and (b**2 - 4*a*c) >= 0",
                    "c": "b != 0 and c != 0",
                    "d": "(b**2 - 4*a*c) >= 0"
                },
                "resposta": "a",
                "explicacao": "As Relações de Girard (Soma = -b/a, Produto = c/a) funcionam até para raízes complexas. A única condição para o cálculo é que `a` seja diferente de zero, para que a divisão seja possível e a equação seja do segundo grau."
            },
            {
                "pergunta": (
                    "7. O código calcula as coordenadas do **vértice** de uma parábola `y = ax² + bx + c`. Qual é a condição fundamental?\n\n"
                    "if ______________:\n"
                    "    xv = -b / (2 * a)\n"
                    "    yv = -(b**2 - 4*a*c) / (4 * a)\n"
                    "else:\n"
                    "    print('Não é uma parábola.')"
                ),
                "opcoes": {
                    "a": "a != 0",
                    "b": "(b**2 - 4*a*c) >= 0",
                    "c": "a > 0",
                    "d": "b != 0 and c != 0"
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
                    "    print('Coordenadas inválidas.')"
                ),
                "opcoes": {
                    "a": "lat >= -90 and lat <= 90",
                    "b": "lon >= -180 and lon <= 180",
                    "c": "(lat >= -90 and lat <= 90) and (lon >= -180 and lon <= 180)",
                    "d": "lat != 0 and lon != 0"
                },
                "resposta": "c",
                "explicacao": "A validação de coordenadas GPS exige a verificação de ambos os valores: a latitude deve estar no intervalo de [-90, 90] graus, e a longitude deve estar no intervalo de [-180, 180] graus."
            },
            {
                "pergunta": (
                    "9. O código calcula a **hipotenusa** de um triângulo retângulo a partir de seus dois catetos. Qual é a condição que garante que os catetos têm comprimentos válidos?\n\n"
                    "if ______________:\n"
                    "    hipotenusa = math.hypot(cateto_a, cateto_b)\n"
                    "else:\n"
                    "    print('Lados inválidos.')"
                ),
                "opcoes": {
                    "a": "cateto_a != 0 and cateto_b != 0",
                    "b": "cateto_a >= 0 and cateto_b >= 0",
                    "c": "cateto_a > 0 and cateto_b > 0",
                    "d": "isinstance(cateto_a, (int, float))"
                },
                "resposta": "c",
                "explicacao": "Para formar um triângulo retângulo válido, os comprimentos dos catetos devem ser valores estritamente positivos. Lados com comprimento zero ou negativo não são geometricamente possíveis."
            },
            {
                "pergunta": (
                    "10. O código calcula o comprimento da **circunferência** de uma esfera. Qual condição garante que o raio da esfera é um valor geometricamente válido?\n\n"
                    "if ______________:\n"
                    "    circunferencia = 2 * math.pi * raio\n"
                    "else:\n"
                    "    print('Raio inválido.')"
                ),
                "opcoes": {
                    "a": "raio >= 0",
                    "b": "raio > 0",
                    "c": "isinstance(raio, (int, float))",
                    "d": "raio != 1"
                },
                "resposta": "b",
                "explicacao": "O raio de uma esfera, sendo uma medida de comprimento, deve ser um valor estritamente positivo para que a esfera tenha uma dimensão real e uma circunferência mensurável."
            }
        ]

        self.pontuacao = 0
        self.indice_pergunta_atual = 0
        self.resposta_selecionada = tk.StringVar()

        self.criar_widgets()
        self.carregar_pergunta()

    def criar_widgets(self):
        """Cria e posiciona todos os widgets na janela."""
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.BG_COLOR, bd=10, padx=10, pady=10)
        main_frame.pack(fill="both", expand=True)
        
        # Rótulo da pergunta
        self.label_pergunta = tk.Label(
            main_frame, text="", wraplength=850, justify="left",
            font=self.FONT_QUESTION, bg=self.BG_COLOR, fg=self.TEXT_COLOR
        )
        self.label_pergunta.pack(pady=(10, 20), anchor="w")

        # Frame para os botões de opção
        self.opcoes_frame = tk.Frame(main_frame, bg=self.BG_COLOR)
        self.opcoes_frame.pack(fill="x", pady=10)

        # Botões de rádio para as opções
        self.botoes_opcoes = []
        for i in range(4):
            key = list("abcd")[i]
            btn = tk.Radiobutton(
                self.opcoes_frame, text="", variable=self.resposta_selecionada, value=key,
                wraplength=800, justify="left", anchor="w",
                font=self.FONT_NORMAL, bg=self.BG_COLOR, fg=self.TEXT_COLOR,
                selectcolor=self.BG_COLOR, activebackground=self.BG_COLOR,
                activeforeground=self.BUTTON_COLOR, highlightthickness=0
            )
            btn.pack(fill="x", pady=5, anchor="w")
            self.botoes_opcoes.append(btn)

        # Frame para feedback
        self.feedback_label = tk.Label(
            main_frame, text="", font=self.FONT_BOLD,
            bg=self.BG_COLOR, wraplength=850, justify="left"
        )
        self.feedback_label.pack(pady=(10, 5))
        
        # Frame para explicação
        self.explicacao_label = tk.Label(
            main_frame, text="", font=self.FONT_NORMAL,
            bg=self.BG_COLOR, fg=self.TEXT_COLOR, wraplength=850, justify="left"
        )
        self.explicacao_label.pack(pady=(5, 20))

        # Botão de próximo/submeter
        self.next_button = tk.Button(
            main_frame, text="Submeter Resposta", command=self.verificar_resposta,
            font=self.FONT_BOLD, bg=self.BUTTON_COLOR, fg=self.BUTTON_TEXT_COLOR,
            relief=tk.FLAT, padx=20, pady=10
        )
        self.next_button.pack(pady=20)
    
    def carregar_pergunta(self):
        """Carrega e exibe a pergunta e as opções atuais."""
        if self.indice_pergunta_atual < len(self.perguntas):
            pergunta_atual = self.perguntas[self.indice_pergunta_atual]
            
            # Limpa estado anterior
            self.feedback_label.config(text="")
            self.explicacao_label.config(text="")
            self.resposta_selecionada.set("")
            
            # Carrega nova pergunta
            self.label_pergunta.config(text=pergunta_atual["pergunta"])
            
            opcoes = pergunta_atual["opcoes"]
            for i, key in enumerate(opcoes):
                self.botoes_opcoes[i].config(
                    text=f"if {opcoes[key]}:", 
                    value=key,
                    state="normal",
                    fg=self.TEXT_COLOR
                )
            
            self.next_button.config(text="Submeter Resposta", command=self.verificar_resposta)
        else:
            self.mostrar_resultado()

    def verificar_resposta(self):
        """Verifica a resposta selecionada, dá feedback e prepara a próxima pergunta."""
        selecionada = self.resposta_selecionada.get()
        if not selecionada:
            messagebox.showwarning("Nenhuma Resposta", "Por favor, selecione uma alternativa.")
            return

        pergunta_atual = self.perguntas[self.indice_pergunta_atual]
        resposta_correta = pergunta_atual["resposta"]
        
        # Desabilita botões para evitar nova seleção
        for btn in self.botoes_opcoes:
            btn.config(state="disabled")

        if selecionada == resposta_correta:
            self.pontuacao += 1
            self.feedback_label.config(text="✅ Correto!", fg=self.CORRECT_COLOR)
        else:
            self.feedback_label.config(text=f"❌ Incorreto! A resposta certa era '{resposta_correta.upper()}'.", fg=self.INCORRECT_COLOR)
        
        self.explicacao_label.config(text=f"💡 Explicação: {pergunta_atual['explicacao']}")
        
        self.indice_pergunta_atual += 1
        self.next_button.config(text="Próxima Pergunta", command=self.carregar_pergunta)

    def mostrar_resultado(self):
        """Exibe o resultado final do quiz."""
        # Limpa a tela para mostrar o resultado
        for widget in self.root.winfo_children():
            widget.destroy()

        resultado_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        resultado_frame.pack(expand=True)

        titulo = "--- FIM DO QUIZ ---"
        label_titulo = tk.Label(resultado_frame, text=titulo, font=("Helvetica", 20, "bold"), bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        label_titulo.pack(pady=20)
        
        resultado_final = f"Sua pontuação final foi: {self.pontuacao} de {len(self.perguntas)}!"
        label_resultado = tk.Label(resultado_frame, text=resultado_final, font=self.FONT_BOLD, bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        label_resultado.pack(pady=30)
        
        # Botão para jogar novamente
        restart_button = tk.Button(
            resultado_frame, text="Jogar Novamente", command=self.reiniciar_quiz,
            font=self.FONT_BOLD, bg=self.BUTTON_COLOR, fg=self.BUTTON_TEXT_COLOR,
            relief=tk.FLAT, padx=20, pady=10
        )
        restart_button.pack(pady=20)

    def reiniciar_quiz(self):
        """Reinicia o quiz para que o usuário possa jogar novamente."""
        # Destrói todos os widgets e recria a interface
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.__init__(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()