# Sequência de Fibonacci para fins de estudos da linguagem Python
# Exibe a sequêcia de Fibonacci de acordo com a quantidade informada pelo usuário pois sabemos que a sequência é infinita
# Versão 1.0
# Autor: Jean Michel Deschamps
# Data: 05/05/2020

# Variáveis
vr_qtd = 0;
vr_soma = 0;
vr_numAnt = 1;
vr_numRet = 0;
vr_ini = 0;
# Exibe o nome do programa para o usuário
print("--- Fibonacci JMD 1.0 --- ");

# Solicita ao usuário a quantidade de resultados da sequência que serão exibidos
vr_qtd = int(input("Qual a quantidade de resultados que deseja exibir?"));

#Exibi a sequência na tela
for x in range(0, vr_qtd):

  # Soma para calcular o próximo resultado a ser exibido
  vr_soma = vr_numAnt + vr_numRet;

  # Variável para guardar o valor de antes do anterior(-2)
  vr_numRet = vr_numAnt
  # Variável para guardar o valor anterior a soma
  vr_numAnt = vr_soma;

  # Exibi o resultado para o usuário
  print(str(vr_soma));
      
  if x == 0:
    vr_numAnt = 1;

# Pode ser implementado com um laço de repetição WHILE, poderia ser solicitado
# ao usuário se deseja continuar após cada interação;

