### feito por: Thiago Krügel
'''
Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma da expressão (sintaxe).

A entrada será fornecida por um arquivo de textos que será carregado em linha de comando,
com a seguinte formatação:
1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões lógicas estão no arquivo.
2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.
A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais.

Gramática:
Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.
Constante="T"|"F".
Proposicao=[a−z0−9]+
FormulaUnaria=AbreParen OperadorUnario Formula FechaParen
FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen
AbreParen="("
FechaParen=")"
OperatorUnario="¬"
OperatorBinario="∨"|"∧"|"→"|"↔"

Cada  expressão  lógica  avaliada  pode  ter  qualquer  combinação  das  operações  de  negação, conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações.
Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em qualquer expressão de entrada.'''

import os, glob  ### bibliotecas para abrir os arquivos automaticamente

parenteses = 0

def constante(expressao):
  if expressao == 'T' or expressao == 'F':
    return True
  return False


def validarParenteses(letra):
    if letra == ')':
      return 'fechar'
    elif letra == '(':
      return 'abrir'
    return ''


def contarParenteses(expressao):
  parenteses = 0
  for letra in expressao:
    if validarParenteses(letra) == 'abrir' and parenteses >= 0:
      parenteses += 1
    if validarParenteses(letra) == 'fechar' and parenteses > 0:
      parenteses -= 1
  return parenteses


def proposicao(letra):
  if (letra.isalpha() and letra.islower()) or letra.isnumeric():
    return True
  return False


def espaco(letra):
  if letra == ' ':
    return True
  return False


def contraBarra(expressao):
  for i in range(len(expressao)):
    if expressao[i] == '\\':
      return True
  return False


def operadorLatex(expressao, i):
    operadorLen = 0
    operador = "binario"

    try:
      if expressao[i + 1] == 'n' and expressao[i + 2] == 'e' and expressao[i + 3] == 'g':
        operadorLen = 3
        operador = "unario"
        
      elif expressao[i + 1] == 'l' and expressao[i + 2] == 'o' and expressao[i + 3] == 'r':
        operadorLen = 3

      elif expressao[i + 1] == 'v' and expressao[i + 2] == 'e' and expressao[i + 3] == 'e':
        operadorLen = 3
          
      elif (expressao[i + 1] == 'l' and expressao[i + 2] == 'a' and expressao[i + 3] == 'n' and expressao[i + 4] == 'd'):
        operadorLen = 4

      elif expressao[i + 1] == 'w' and expressao[i + 2] == 'e' and expressao[i + 3] == 'd' and expressao[i + 4] == 'g' and expressao[i + 5] == 'e':
        operadorLen = 5
            
      elif (expressao[i + 1] == 'r' and expressao[i + 2] == 'i' and expressao[i + 3] == 'g' and expressao[i + 4] == 'h' and expressao[i + 5] == 't' and expressao[i + 6] == 'a' and expressao[i + 7] == 'r' and expressao[i + 8] == 'r' and expressao[i + 9] == 'o' and expressao[i + 10] == 'w'):
        operadorLen = 10
            
      elif (expressao[i + 1] == 'l' and expressao[i + 2] == 'e' and expressao[i + 3] == 'f' and expressao[i + 4] == 't' and expressao[i + 5] == 'r' and expressao[i + 6] == 'i' and expressao[i + 7] == 'g' and expressao[i + 8] == 'h' and expressao[i + 9] == 't' and expressao[i + 10] == 'a' and expressao[i + 11] == 'r' and expressao[i + 12] == 'r' and expressao[i + 13] == 'o' and expressao[i + 14] == 'w'):
        operadorLen = 14
            
    except IndexError:
      return 0, ""
    return operadorLen, operador


def expressaoValidar(expressao, i, operador):
  expressaoLen = -1
  temp = ""
  parentesesTotal = 0
  
  if operador == "unario":
    if constante(expressao[i]):
      letra = expressao[i + 1]
      if validarParenteses(letra) == 'fechar':    
        expressaoLen += 1
        return True, expressaoLen
      else:
        return False, -1
      
    for j in range(i, len(expressao) - 1):
      if validarParenteses(expressao[i]) == 'abrir':
        if validarParenteses(expressao[j]) == 'abrir' and parentesesTotal >= 0:
          parentesesTotal += 1
        elif validarParenteses(expressao[j]) == 'fechar' and parentesesTotal > 0:
          parentesesTotal -= 1
          if parentesesTotal == 0:
            break
      else:
        if validarParenteses(expressao[j]) == 'fechar' and not espaco(expressao[j + 1]):
          break

      temp += expressao[j]
      expressaoLen += 1

  elif operador == "binario":
    for j in range(i, len(expressao)):
      if validarParenteses(expressao[i]) == 'abrir':
        if validarParenteses(expressao[j]) == 'fechar':
          parentesesTotal += 1
        elif validarParenteses(expressao[j]) == 'fechar':
          parentesesTotal -= 1
          if parentesesTotal == 0:
            break          
      else:
        if validarParenteses(expressao[j]) == 'fechar' or espaco(expressao[j]):
          break

      temp += expressao[j]
      expressaoLen += 1


  if validarParenteses(expressao[i]) == 'abrir':
    expressaoFull = temp + ")"
    expressaoLen += 1
  else:
    expressaoFull = temp

  resultadoExpressao = stringValidar(expressaoFull)

  return resultadoExpressao, expressaoLen


def stringValidar(expressao):
    resultado = True
    operador = ""
    estadoExpressao = 1

    if contarParenteses(expressao) != 0:
      return False
      
    if contraBarra(expressao):
      i = 0
      while i < len(expressao):
        letra = expressao[i]
        if estadoExpressao == 1:
          if validarParenteses(letra) != 'abrir':
            return False
          estadoExpressao += 1
              
        elif estadoExpressao == 2:
          operadorLen, operador = operadorLatex(expressao, i)
          if operadorLen == 0:
            return False
          i += operadorLen
          estadoExpressao += 1

        elif estadoExpressao == 3:
          if not espaco(letra):
            return False
          estadoExpressao += 1             

        elif estadoExpressao == 4:
          resultadoExpressao, expressaoLen = expressaoValidar(expressao, i, operador)
          i += expressaoLen
              
          if resultadoExpressao:
            if operador == "binario":
              estadoExpressao += 1
            elif operador == "unario":
              return True
          else:
            return False

        elif estadoExpressao == 5:
          if espaco(letra):
            estadoExpressao += 1
          else:
            return False

        elif estadoExpressao == 6:
          resultadoExpressao, expressaoLen = expressaoValidar(expressao, i, operador)
          i += expressaoLen

          if not resultadoExpressao:
            return False
          return True

        i += 1
    else:
      for i in range(len(expressao)):
        Constante = constante(expressao)
        Proposicao = proposicao(expressao[i])

        if not Constante and not Proposicao:
          return False

    return resultado



def parserLogica():

    quantidade = 0
    palavrasChecadas = 0
    inicioArquivo = False
    path = "./textos"  ### pasta onde estão os arquivos de texto

    for nomeArquivo in glob.glob(os.path.join(path,'*.txt')):  ### verificação do tipo do arquivo (somente lerá.txt)
        inicioArquivo = False
        quantidade = 0
        palavrasChecadas = 0
        arq = open(os.path.join(os.getcwd(), nomeArquivo), 'r')
        ### print("Arquivo: " + nomeArquivo)

        for i in arq:
            if inicioArquivo == False:
                quantidade = int(i[0])
                inicioArquivo = True
            else:
                word = str(i)
                dividir = word.split("\n")
                palavra = str(dividir[0])
                validado = stringValidar(palavra)
              
                if validado:
                  print("válida")
                  palavrasChecadas += 1
                  if palavrasChecadas >= quantidade:
                    break
                else:
                  print("inválida")
                  palavrasChecadas += 1
                  if palavrasChecadas >= quantidade:
                    break

parserLogica()