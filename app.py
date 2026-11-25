import socket
from flask import Flask, render_template_string

app = Flask(__name__)

# Banco de questões extraído da Revisão AV - ARA0066
QUESTOES = [
    {
        "id": 1,
        "enunciado": "Python é considerada uma linguagem multiparadigma. O que essa característica significa?",
        "codigo": None,
        "alternativas": {
            "A": "Python precisa ser convertida obrigatoriamente para linguagem Assembly antes da execução.",
            "B": "Python permite utilizar diferentes paradigmas de programação, como estruturado, orientado a objetos e funcional.",
            "C": "Python não permite combinar diferentes formas de organização do código.",
            "D": "Python somente permite o desenvolvimento utilizando programação orientada a objetos.",
            "E": "Python executa exclusivamente programas desenvolvidos segundo o paradigma funcional."
        },
        "correta": "B",
        "comentario": "Python é classificada como multiparadigma porque permite desenvolver soluções utilizando diferentes formas de organização da programação, incluindo programação estruturada, orientação a objetos e recursos associados ao paradigma funcional."
    },
    {
        "id": 2,
        "enunciado": "Considere a seguinte expressão: (True + 2) ** 2. Utilizando Python para avaliar a expressão, é correto afirmar que:",
        "codigo": "(True + 2) ** 2",
        "alternativas": {
            "A": "A expressão vale 6.",
            "B": "A expressão vale True.",
            "C": "Não será possível efetuar a operação em virtude da incompatibilidade de tipos.",
            "D": "A expressão vale 9.",
            "E": "A expressão vale 1."
        },
        "correta": "D",
        "comentario": "Em Python, em contexto numérico, True corresponde ao valor inteiro 1. Assim, True + 2 resulta em 3. Em seguida, o operador ** realiza a potenciação: 3² = 9."
    },
    {
        "id": 3,
        "enunciado": "Considere o código abaixo. Qual será a saída apresentada?",
        "codigo": 'idade = 17\nif idade >= 18:\n    print("Maior de idade")\nelse:\n    print("Menor de idade")',
        "alternativas": {
            "A": "Maior de idade",
            "B": "17",
            "C": "Menor de idade",
            "D": "True",
            "E": "O programa apresentará erro."
        },
        "correta": "C",
        "comentario": "A condição idade >= 18 verifica se 17 é maior ou igual a 18. Como a expressão resulta em False, o bloco else será executado, apresentando 'Menor de idade'."
    },
    {
        "id": 4,
        "enunciado": "Como se chama a seguinte característica de uma linguagem de programação: 'um conjunto relativamente pequeno de construções primitivas pode ser combinado em um número, também, pequeno de maneiras para construir as estruturas de controle e de dados de uma linguagem de programação'?",
        "codigo": None,
        "alternativas": {
            "A": "Confiabilidade.",
            "B": "Recursividade.",
            "C": "Expressividade.",
            "D": "Ortogonalidade.",
            "E": "Aliasing."
        },
        "correta": "D",
        "comentario": "A característica descrita corresponde à ortogonalidade, relacionada à possibilidade de combinar um conjunto pequeno de construções primitivas de maneiras consistentes para formar estruturas mais complexas."
    },
    {
        "id": 5,
        "enunciado": "Observe o código abaixo. Qual sequência será apresentada?",
        "codigo": "for numero in range(2, 11, 2):\n    print(numero)",
        "alternativas": {
            "A": "2, 4, 6, 8, 10",
            "B": "2, 4, 6, 8",
            "C": "1, 3, 5, 7, 9",
            "D": "0, 2, 4, 6, 8, 10",
            "E": "2, 3, 4, 5, 6, 7, 8, 9, 10"
        },
        "correta": "A",
        "comentario": "range(2, 11, 2) começa em 2, avança de 2 em 2 e termina antes de 11. Os valores gerados são 2, 4, 6, 8 e 10."
    },
    {
        "id": 6,
        "enunciado": "Analise o trecho de código em Python 3 a seguir. O valor impresso pela função print, na última linha do trecho de código, é: (dica: a função lower retorna todas as letras de uma string em minúsculo)",
        "codigo": "def fc(x, y):\n    s = 0\n    a = x.lower()\n    for i in a:\n        if (i == y):\n            s = s + 1\n    return s\n\na = 'Aracajú/Sergipe'\nx = fc(a, 'a') * 100\ny = fc(a, 'e') * 10\nz = fc(a, 'i')\nprint(x + y + z)",
        "alternativas": {
            "A": "132",
            "B": "321",
            "C": "111",
            "D": "333",
            "E": "123"
        },
        "correta": "B",
        "comentario": "Após lower(), há 3 ocorrências de 'a' (3 * 100 = 300), 2 ocorrências de 'e' (2 * 10 = 20) e 1 ocorrência de 'i' (1). Assim, 300 + 20 + 1 = 321."
    },
    {
        "id": 7,
        "enunciado": "Considere o código abaixo. Qual será a saída?",
        "codigo": "contador = 1\nwhile contador <= 4:\n    print(contador)\n    contador += 1",
        "alternativas": {
            "A": "0, 1, 2, 3",
            "B": "1, 2, 3",
            "C": "1, 2, 3, 4, 5",
            "D": "1, 2, 3, 4",
            "E": "O laço será infinito."
        },
        "correta": "D",
        "comentario": "O contador começa em 1 e o while continua enquanto for menor ou igual a 4. São impressos 1, 2, 3 e 4. Quando passa para 5, a condição se torna falsa."
    },
    {
        "id": 8,
        "enunciado": "A popularidade do Python se deve em grande parte à sua simplicidade. Qual é a definição de um arquivo de script em Python?",
        "codigo": None,
        "alternativas": {
            "A": "É um arquivo de texto que contém sequências de erros para log.",
            "B": "Uma inteligência artificial.",
            "C": "É uma mensagem de erro gerada pelo compilador.",
            "D": "É um arquivo de texto que contém instruções que compõem um programa Python.",
            "E": "É uma mensagem de erro gerada pelos programadores."
        },
        "correta": "D",
        "comentario": "Um script Python é um arquivo de texto contendo instruções escritas na linguagem Python que formam um programa ou parte dele."
    },
    {
        "id": 9,
        "enunciado": "Analise o código abaixo. Qual será a saída?",
        "codigo": 'numero = 7\nif numero % 2 == 0:\n    print("Par")\nelse:\n    print("Ímpar")',
        "alternativas": {
            "A": "Par",
            "B": "0",
            "C": "Ímpar",
            "D": "1",
            "E": "False"
        },
        "correta": "C",
        "comentario": "O operador % calcula o resto da divisão. Como 7 ÷ 2 possui resto 1, 7 % 2 == 0 é falso. Consequentemente, o else é executado e apresenta 'Ímpar'."
    },
    {
        "id": 10,
        "enunciado": "Como um desenvolvedor Python pode comentar um código para facilitar futuras análises?",
        "codigo": None,
        "alternativas": {
            "A": "Usando &",
            "B": "Usando #",
            "C": "Usando !",
            "D": "Usando $",
            "E": "Usando %"
        },
        "correta": "B",
        "comentario": "Em Python, o caractere # inicia um comentário de uma linha. O interpretador desconsidera o conteúdo localizado depois desse símbolo naquela linha."
    },
    {
        "id": 11,
        "enunciado": "Observe o código abaixo. Qual valor será apresentado?",
        "codigo": "def dobro(numero):\n    return numero * 2\n\nresultado = dobro(7)\nprint(resultado)",
        "alternativas": {
            "A": "7",
            "B": "9",
            "C": "14",
            "D": "49",
            "E": "2"
        },
        "correta": "C",
        "comentario": "A função dobro() recebe o valor 7 e retorna 7 * 2 = 14. Esse valor é armazenado em resultado e apresentado pelo print()."
    },
    {
        "id": 12,
        "enunciado": "Dadas as afirmativas acerca das linguagens de programação Java, C++ e Python:\nI - Das três linguagens consideradas, apenas Python não possui suporte nativo a interfaces com sintaxe explícita como em Java e C++, embora permita a criação de interfaces por meio de classes abstratas.\nII - O Python possui nativamente o tipo privado, assim como C e Ruby.\nIII - Na linguagem Python, o decorator @staticmethod somente pode ser utilizado para qualificar métodos, não podendo ser utilizado para qualificar atributos.\nVerifica-se que está(ão) correta(s):",
        "codigo": None,
        "alternativas": {
            "A": "II e III, apenas.",
            "B": "I e II, apenas.",
            "C": "I, II e III.",
            "D": "II, apenas.",
            "E": "I e III, apenas."
        },
        "correta": "E",
        "comentario": "A afirmativa I está correta (Python usa classes abstratas via módulo abc). A afirmativa II está incorreta (Python usa convenções com underscore, não um modificador nativo rígido como private). A afirmativa III está correta quanto à aplicação do decorator a métodos."
    },
    {
        "id": 13,
        "enunciado": "Considere o código abaixo. Qual é a finalidade do bloco except?",
        "codigo": 'try:\n    resultado = 10 / 0\nexcept ZeroDivisionError:\n    print("Não é possível dividir por zero.")',
        "alternativas": {
            "A": "Repetir a divisão até funcionar.",
            "B": "Impedir que qualquer código Python seja executado.",
            "C": "Tratar a exceção provocada pela divisão por zero.",
            "D": "Converter automaticamente zero em um.",
            "E": "Encerrar o interpretador Python."
        },
        "correta": "C",
        "comentario": "A operação 10 / 0 gera uma exceção ZeroDivisionError. O bloco except captura especificamente esse tipo de problema e executa uma resposta controlada, evitando que o programa quebre."
    },
    {
        "id": 14,
        "enunciado": "(FGV/2018) Considere a seguinte definição da função f, declarada na sintaxe Python. Assinale o valor produzido pela execução do código acima.",
        "codigo": "def f(n):\n    if n < 3:\n        return n - 1\n    else:\n        return f(n - 2) + f(n - 1)\n\nprint(f(10))",
        "alternativas": {
            "A": "21",
            "B": "55",
            "C": "13",
            "D": "34",
            "E": "17"
        },
        "correta": "D",
        "comentario": "A função é recursiva (sequência de Fibonacci deslocada): f(1)=0, f(2)=1, f(3)=1, f(4)=2, f(5)=3, f(6)=5, f(7)=8, f(8)=13, f(9)=21 e f(10)=34."
    },
    {
        "id": 15,
        "enunciado": "Considere o código abaixo. Qual será o resultado?",
        "codigo": "import math\nnumero = 81\nresultado = math.sqrt(numero)\nprint(resultado)",
        "alternativas": {
            "A": "8.0",
            "B": "9.0",
            "C": "81.0",
            "D": "40.5",
            "E": "O programa apresentará erro."
        },
        "correta": "B",
        "comentario": "math.sqrt() calcula a raiz quadrada e sempre retorna um número de ponto flutuante (float). Como √81 = 9, a função retorna 9.0."
    },
    {
        "id": 16,
        "enunciado": "Os paradigmas de programação fornecem diferentes formas de estruturar a solução de problemas computacionais. Sobre o paradigma imperativo, assinale a alternativa correta.",
        "codigo": None,
        "alternativas": {
            "A": "É utilizado exclusivamente por linguagens de baixo nível.",
            "B": "Não permite a utilização de funções ou subprogramas.",
            "C": "Organiza a solução por meio de comandos que modificam o estado do programa ao longo da execução.",
            "D": "Descreve apenas o resultado desejado, sem representar operações que modificam o estado do programa.",
            "E": "Proíbe a utilização de variáveis e estruturas de repetição."
        },
        "correta": "C",
        "comentario": "O paradigma imperativo descreve uma sequência de comandos que modificam o estado do programa durante sua execução usando variáveis, atribuições, decisões e repetições."
    },
    {
        "id": 17,
        "enunciado": "Considere o código abaixo. O que a instrução random.randint(1, 10) faz?",
        "codigo": "import random\nnumero = random.randint(1, 10)",
        "alternativas": {
            "A": "Gera somente números pares entre 1 e 10.",
            "B": "Gera um número inteiro aleatório entre 1 e 10, incluindo os limites.",
            "C": "Gera obrigatoriamente o número 10.",
            "D": "Gera um número decimal entre 1 e 10.",
            "E": "Cria uma lista contendo os números de 1 a 10."
        },
        "correta": "B",
        "comentario": "randint(1, 10) seleciona um número inteiro pseudoaleatório no intervalo fechado informado, podendo retornar tanto 1 quanto 10."
    },
    {
        "id": 18,
        "enunciado": "Considere o código Python abaixo. Qual será a saída apresentada?",
        "codigo": 'nota1 = 8.0\nnota2 = 6.0\nmedia = (nota1 + nota2) / 2\nprint(f"Média: {media:.2f}")',
        "alternativas": {
            "A": "Média: 7",
            "B": "Média: 14.00",
            "C": "Média: 6.00",
            "D": "Média: 7.00",
            "E": "Média: 8.00"
        },
        "correta": "D",
        "comentario": "A média é calculada por (8.0 + 6.0) / 2 = 7.0. A formatação :.2f determina duas casas decimais, produzindo 'Média: 7.00'."
    },
    {
        "id": 19,
        "enunciado": "Observe o código abaixo. Desconsiderando o tempo de espera, qual sequência será apresentada?",
        "codigo": "import time\nfor numero in range(3, 0, -1):\n    print(numero)\n    time.sleep(1)",
        "alternativas": {
            "A": "1, 2, 3",
            "B": "3, 2, 1",
            "C": "3, 2, 1, 0",
            "D": "0, 1, 2, 3",
            "E": "3, 3, 3"
        },
        "correta": "B",
        "comentario": "range(3, 0, -1) começa em 3, reduz uma unidade a cada repetição e termina antes de chegar a 0. Assim, são produzidos 3, 2 e 1."
    },
    {
        "id": 20,
        "enunciado": "Observe o código abaixo. Qual sequência será apresentada?",
        "codigo": "for numero in range(1, 6):\n    print(numero)",
        "alternativas": {
            "A": "1, 6",
            "B": "1, 2, 3, 4, 5, 6",
            "C": "0, 1, 2, 3, 4",
            "D": "1, 2, 3, 4, 5",
            "E": "0, 1, 2, 3, 4, 5"
        },
        "correta": "D",
        "comentario": "range(1, 6) começa em 1 e produz valores até imediatamente antes de 6 (limite superior exclusivo). Portanto, a sequência é 1, 2, 3, 4 e 5."
    },
    {
        "id": 21,
        "enunciado": "Considere o código abaixo. Se o usuário digitar 20, quais mensagens serão apresentadas depois da entrada?",
        "codigo": 'try:\n    idade = int(input("Digite sua idade: "))\nexcept ValueError:\n    print("Entrada inválida")\nelse:\n    print("Entrada válida")\nfinally:\n    print("Fim")',
        "alternativas": {
            "A": "Entrada inválida e Fim",
            "B": "Apenas Entrada válida",
            "C": "Entrada válida e Fim",
            "D": "Apenas Fim",
            "E": "O programa apresentará ValueError."
        },
        "correta": "C",
        "comentario": "int('20') é uma conversão válida, portanto nenhuma exceção ocorre. O bloco else apresenta 'Entrada válida'. Independentemente do resultado, finally é sempre executado e apresenta 'Fim'."
    },
    {
        "id": 22,
        "enunciado": "Analise o código abaixo. Qual será a saída?",
        "codigo": "for numero in range(1, 8):\n    if numero == 3:\n        continue\n    if numero == 6:\n        break\n    print(numero)",
        "alternativas": {
            "A": "1, 2, 4, 5, 7",
            "B": "3, 6",
            "C": "1, 2, 3, 4, 5",
            "D": "1, 2, 4, 5",
            "E": "1, 2, 3, 4, 5, 6, 7"
        },
        "correta": "D",
        "comentario": "1 e 2 são impressos. Quando numero vale 3, continue pula o restante daquela iteração. 4 e 5 são impressos. Ao chegar a 6, break encerra o laço antes do print()."
    },
    {
        "id": 23,
        "enunciado": "Considere o código abaixo. Qual será a saída?",
        "codigo": 'class Aluno:\n    def __init__(self, nome):\n        self.nome = nome\n\naluno = Aluno("Carlos")\nprint(aluno.nome)',
        "alternativas": {
            "A": "Aluno",
            "B": "nome",
            "C": "Carlos",
            "D": "self",
            "E": "O programa apresentará erro."
        },
        "correta": "C",
        "comentario": "Ao criar Aluno('Carlos'), o valor 'Carlos' é recebido pelo parâmetro nome e atribuído a self.nome. O comando print(aluno.nome) acessa esse atributo e apresenta 'Carlos'."
    },
    {
        "id": 24,
        "enunciado": "Considere o código abaixo. Qual será o valor apresentado?",
        "codigo": "def calcular_media(n1, n2):\n    return (n1 + n2) / 2\n\nresultado = calcular_media(8, 6)\nprint(resultado)",
        "alternativas": {
            "A": "O programa não produzirá resultado porque uma função não pode retornar valores.",
            "B": "7",
            "C": "6",
            "D": "14",
            "E": "8"
        },
        "correta": "B",
        "comentario": "A função calcula (8 + 6) / 2 = 7.0 (representado como 7 nas alternativas). O comando return devolve esse resultado para a variável resultado."
    },
    {
        "id": 25,
        "enunciado": "Na Programação Orientada a Objetos, qual alternativa define corretamente uma classe?",
        "codigo": None,
        "alternativas": {
            "A": "É obrigatoriamente uma variável do tipo inteiro.",
            "B": "É uma estrutura utilizada como modelo para criação de objetos.",
            "C": "É um erro gerado durante a execução do programa.",
            "D": "É exclusivamente uma função que não recebe parâmetros.",
            "E": "É um laço utilizado para percorrer objetos."
        },
        "correta": "B",
        "comentario": "Uma classe estabelece uma estrutura que define atributos e métodos. A partir dela podem ser criados objetos, também chamados de instâncias."
    },
    {
        "id": 26,
        "enunciado": "Considere o código abaixo. Se o usuário digitar 'Python', o que acontecerá?",
        "codigo": 'try:\n    numero = int(input("Digite um número: "))\nexcept ValueError:\n    print("Valor inválido")\nelse:\n    print("Valor aceito")',
        "alternativas": {
            "A": "O bloco else será executado antes do except.",
            "B": "Será apresentada a mensagem 'Valor inválido'.",
            "C": "O programa converterá automaticamente o texto para zero.",
            "D": "O programa sempre será encerrado sem apresentar mensagens.",
            "E": "Será apresentada a mensagem 'Valor aceito'."
        },
        "correta": "B",
        "comentario": "A tentativa de executar int('Python') gera ValueError, pois o texto não representa um número inteiro válido. O except ValueError captura a exceção e apresenta 'Valor inválido'."
    },
    {
        "id": 27,
        "enunciado": "Observe o código abaixo. Qual será o resultado?",
        "codigo": "class Televisao:\n    def __init__(self):\n        self.volume = 10\n\n    def aumentar_volume(self):\n        if self.volume < 100:\n            self.volume += 1\n\ntv = Televisao()\ntv.aumentar_volume()\ntv.aumentar_volume()\nprint(tv.volume)",
        "alternativas": {
            "A": "10",
            "B": "11",
            "C": "12",
            "D": "20",
            "E": "100"
        },
        "correta": "C",
        "comentario": "O objeto começa com volume = 10. Cada chamada de aumentar_volume() soma uma unidade. Após a primeira chamada, 11; após a segunda, 12."
    },
    {
        "id": 28,
        "enunciado": "Considere o código abaixo. Qual valor será apresentado?",
        "codigo": "class Televisao:\n    def __init__(self):\n        self.volume = 10\n\ntv1 = Televisao()\ntv2 = tv1\ntv2.volume = 50\nprint(tv1.volume)",
        "alternativas": {
            "A": "10",
            "B": "50",
            "C": "60",
            "D": "0",
            "E": "O programa apresentará erro."
        },
        "correta": "B",
        "comentario": "tv2 = tv1 não cria uma nova televisão, mas copia a referência para o mesmo objeto na memória. Ao alterar tv2.volume para 50, tv1.volume reflete o mesmo valor."
    },
    {
        "id": 29,
        "enunciado": "Considere o código abaixo. Qual será a saída?",
        "codigo": 'def saudacao(nome="Aluno"):\n    return f"Olá, {nome}!"\n\nprint(saudacao())',
        "alternativas": {
            "A": "Olá, nome!",
            "B": "Olá, Aluno!",
            "C": "Aluno",
            "D": "Olá!",
            "E": "O programa apresentará erro porque nenhum argumento foi informado."
        },
        "correta": "B",
        "comentario": "O parâmetro nome possui o valor padrão 'Aluno'. Como a função é chamada sem argumento, Python utiliza esse valor padrão, retornando 'Olá, Aluno!'."
    },
    {
        "id": 30,
        "enunciado": "Considere o código abaixo. Qual valor será apresentado?",
        "codigo": 'class Conta:\n    def __init__(self, titular, saldo):\n        self.titular = titular\n        self.saldo = saldo\n\n    def depositar(self, valor):\n        self.saldo += valor\n\nconta = Conta("Ana", 500)\nconta.depositar(200)\nprint(conta.saldo)',
        "alternativas": {
            "A": "200",
            "B": "300",
            "C": "500",
            "D": "700",
            "E": "1000"
        },
        "correta": "D",
        "comentario": "O objeto é criado com saldo inicial de 500. O método depositar(200) executa self.saldo += 200, resultando em 700."
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <meta name="theme-color" content="#090d16">
    <title>Simulado Dark - ARA0066 Python</title>
    <style>
        :root {
            --primary: #3b82f6;
            --primary-hover: #2563eb;
            --bg: #090d16;
            --card: #111827;
            --surface: #1e293b;
            --text: #f1f5f9;
            --muted: #94a3b8;
            --border: #263248;
            --correct-bg: rgba(34, 197, 94, 0.16);
            --correct-border: #22c55e;
            --wrong-bg: rgba(239, 68, 68, 0.16);
            --wrong-border: #ef4444;
        }
        * {
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }
        html {
            scroll-behavior: smooth;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 0;
            line-height: 1.55;
            padding-bottom: 88px;
        }
        header {
            background: linear-gradient(135deg, #0b1120, #172554);
            color: var(--text);
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 16px rgba(0,0,0,0.45);
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        header h1 {
            margin: 0;
            font-size: 1.15rem;
            font-weight: 700;
        }
        header p {
            margin: 0.2rem 0 0.6rem;
            font-size: 0.8rem;
            color: var(--muted);
        }
        .scoreboard {
            display: flex;
            justify-content: space-around;
            align-items: center;
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid var(--border);
            padding: 0.45rem 0.75rem;
            border-radius: 10px;
            font-size: 0.85rem;
            max-width: 600px;
            margin: 0 auto;
        }
        .progress-track {
            width: 100%;
            height: 4px;
            background: rgba(148, 163, 184, 0.18);
            position: absolute;
            bottom: 0;
            left: 0;
        }
        .progress-fill {
            height: 100%;
            width: 0%;
            background: #22c55e;
            transition: width 0.3s ease;
        }
        .container {
            max-width: 760px;
            margin: 1rem auto;
            padding: 0 0.75rem;
        }
        .card {
            background: var(--card);
            border-radius: 14px;
            padding: 1.15rem;
            margin-bottom: 1rem;
            box-shadow: 0 6px 18px rgba(0,0,0,0.3);
            border: 1px solid var(--border);
            scroll-margin-top: 118px;
        }
        .q-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.7rem;
        }
        .q-badge {
            background: rgba(59, 130, 246, 0.16);
            color: #93c5fd;
            border: 1px solid rgba(59, 130, 246, 0.35);
            font-weight: 700;
            padding: 0.25rem 0.7rem;
            border-radius: 8px;
            font-size: 0.85rem;
        }
        .q-points {
            color: var(--muted);
            font-size: 0.8rem;
        }
        .enunciado {
            font-size: 0.98rem;
            font-weight: 500;
            margin-bottom: 0.9rem;
            white-space: pre-line;
            color: var(--text);
        }
        pre {
            background: #050811;
            color: #e2e8f0;
            padding: 0.85rem;
            border-radius: 10px;
            border: 1px solid #1e293b;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            font-family: 'Consolas', 'Menlo', monospace;
            font-size: 0.85rem;
            line-height: 1.45;
            margin: 0 0 1rem 0;
        }
        .options {
            display: flex;
            flex-direction: column;
            gap: 0.65rem;
        }
        .option-btn {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            width: 100%;
            min-height: 52px;
            text-align: left;
            background: var(--surface);
            border: 2px solid var(--border);
            border-radius: 10px;
            padding: 0.75rem 0.9rem;
            cursor: pointer;
            font-size: 0.93rem;
            color: var(--text);
            transition: transform 0.1s ease, background-color 0.15s ease, border-color 0.15s ease;
            touch-action: manipulation;
        }
        .option-btn:active:not(:disabled) {
            transform: scale(0.985);
            background: #24344d;
            border-color: var(--primary);
        }
        .option-btn:disabled {
            cursor: default;
            opacity: 0.92;
        }
        .option-letter {
            font-weight: 700;
            background: #0f172a;
            color: #cbd5e1;
            border: 1px solid #334155;
            min-width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            flex-shrink: 0;
        }
        .option-btn.correct {
            background: var(--correct-bg);
            border-color: var(--correct-border);
            opacity: 1;
        }
        .option-btn.correct .option-letter {
            background: var(--correct-border);
            border-color: var(--correct-border);
            color: #052e16;
        }
        .option-btn.wrong {
            background: var(--wrong-bg);
            border-color: var(--wrong-border);
            opacity: 1;
        }
        .option-btn.wrong .option-letter {
            background: var(--wrong-border);
            border-color: var(--wrong-border);
            color: #ffffff;
        }
        .feedback {
            margin-top: 0.9rem;
            padding: 0.9rem;
            border-radius: 10px;
            font-size: 0.9rem;
            display: none;
        }
        .feedback.show { display: block; }
        .feedback.ok {
            background: rgba(34, 197, 94, 0.12);
            border-left: 4px solid var(--correct-border);
            color: #bbf7d0;
        }
        .feedback.err {
            background: rgba(239, 68, 68, 0.12);
            border-left: 4px solid var(--wrong-border);
            color: #fecaca;
        }
        .mobile-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(8px);
            border-top: 1px solid var(--border);
            padding: 0.65rem 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 0.75rem;
            z-index: 100;
            box-shadow: 0 -4px 16px rgba(0,0,0,0.45);
        }
        .btn-nav {
            flex: 1;
            background: var(--primary);
            color: white;
            border: none;
            padding: 0.75rem 1rem;
            font-size: 0.92rem;
            font-weight: 600;
            border-radius: 10px;
            cursor: pointer;
            touch-action: manipulation;
        }
        .btn-nav:active {
            background: var(--primary-hover);
        }
        .btn-secondary {
            background: var(--surface);
            color: var(--text);
            border: 1px solid var(--border);
            padding: 0.75rem 1rem;
            font-size: 0.92rem;
            font-weight: 600;
            border-radius: 10px;
            cursor: pointer;
        }

        @media (min-width: 768px) {
            header h1 { font-size: 1.4rem; }
            .container { margin: 1.75rem auto; }
            .card { padding: 1.5rem; }
            .option-btn:hover:not(:disabled) {
                border-color: var(--primary);
                background: #24344d;
            }
            .mobile-bar {
                max-width: 760px;
                margin: 0 auto;
                border-radius: 14px 14px 0 0;
                border-left: 1px solid var(--border);
                border-right: 1px solid var(--border);
            }
        }
    </style>
</head>
<body>

<header>
    <h1>Simulado Dark — ARA0066</h1>
    <p>Paradigmas de Linguagens em Python</p>
    <div class="scoreboard">
        <span>Feitas: <strong id="count-total">0</strong>/30</span>
        <span>Acertos: <strong id="count-hits">0</strong></span>
        <span>Nota: <strong id="score-points">0.0</strong>/21</span>
    </div>
    <div class="progress-track">
        <div class="progress-fill" id="progress-bar"></div>
    </div>
</header>

<div class="container">
    {% for q in questoes %}
    <div class="card" id="card-{{ q.id }}" data-answered="false">
        <div class="q-header">
            <span class="q-badge">Questão {{ q.id }} de 30</span>
            <span class="q-points">0.7 pt</span>
        </div>
        <div class="enunciado">{{ q.enunciado }}</div>
        {% if q.codigo %}
        <pre><code>{{ q.codigo }}</code></pre>
        {% endif %}
        <div class="options" id="options-{{ q.id }}">
            {% for letra, texto in q.alternativas.items() %}
            <button class="option-btn" onclick="responder({{ q.id }}, '{{ letra }}', '{{ q.correta }}')">
                <span class="option-letter">{{ letra }}</span>
                <span>{{ texto }}</span>
            </button>
            {% endfor %}
        </div>
        <div class="feedback" id="feedback-{{ q.id }}">
            <strong>Gabarito: Letra {{ q.correta }}</strong><br>
            {{ q.comentario }}
        </div>
    </div>
    {% endfor %}
</div>

<div class="mobile-bar">
    <button class="btn-secondary" onclick="reiniciar()">Reiniciar</button>
    <button class="btn-nav" onclick="proximaPendente()">Próxima pendente ↓</button>
</div>

<script>
    let respondidas = 0;
    let acertos = 0;
    const totalQuestoes = 30;

    function responder(id, escolhida, correta) {
        const card = document.getElementById(`card-${id}`);
        if (card.dataset.answered === "true") return;
        card.dataset.answered = "true";

        const container = document.getElementById(`options-${id}`);
        const botoes = container.querySelectorAll('.option-btn');
        const feedback = document.getElementById(`feedback-${id}`);

        respondidas++;
        const acertou = (escolhida === correta);
        if (acertou) acertos++;

        botoes.forEach(btn => {
            btn.disabled = true;
            const letraBtn = btn.querySelector('.option-letter').innerText.trim();
            if (letraBtn === correta) {
                btn.classList.add('correct');
            } else if (letraBtn === escolhida && !acertou) {
                btn.classList.add('wrong');
            }
        });

        feedback.classList.add('show');
        feedback.classList.add(acertou ? 'ok' : 'err');
        feedback.innerHTML = (acertou ? '✅ <strong>Correto!</strong> ' : '❌ <strong>Incorreto.</strong> ') + feedback.innerHTML;

        document.getElementById('count-total').innerText = respondidas;
        document.getElementById('count-hits').innerText = acertos;
        document.getElementById('score-points').innerText = (acertos * 0.7).toFixed(1);
        document.getElementById('progress-bar').style.width = `${(respondidas / totalQuestoes) * 100}%`;
    }

    function proximaPendente() {
        const pendente = document.querySelector('.card[data-answered="false"]');
        if (pendente) {
            pendente.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
            alert(`Simulado finalizado! Você acertou ${acertos} de ${totalQuestoes} questões (Nota: ${(acertos * 0.7).toFixed(1)}).`);
        }
    }

    function reiniciar() {
        if (confirm("Deseja zerar suas respostas e recomeçar o simulado?")) {
            window.scrollTo(0, 0);
            window.location.reload();
        }
    }
</script>

</body>
</html>"""

def obter_ip_local():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, questoes=QUESTOES)

if __name__ == "__main__":
    ip_local = obter_ip_local()
    print("\n" + "="*50)
    print(f"📱 ACESSE NO CELULAR (mesmo Wi-Fi): http://{ip_local}:5000")
    print("💻 ACESSE NO COMPUTADOR:           http://127.0.0.1:5000")
    print("="*50 + "\n")