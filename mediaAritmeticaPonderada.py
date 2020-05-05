# Calculadora de médias (Aritmética e Ponderada) feita em Python para fins de estudo da linguagem.
# Versão 1.0
# Autor: Jean Michel Deschamps
# Data: 05/05/2020

print("--- Calculadora de Média Aritmética e Ponderada - JMD 1.0 --- ");

#Inicialização de variáveis, não é necessário.
vr_continue = True;
vr_num1 = 0;
vr_num2 = 0;
vr_opcao = "";
vr_qtdNotas = 0;
vr_contador = 0;
vr_listaNota = [];
vr_listaPeso = [];
vr_soma = 0;
vr_nota = 0;
vr_peso = 0;
vr_media = 0;
vr_somaPeso = 0;

while vr_continue ==  True:

        vr_media = input("Qual o tipo de média deseja executar((A)ritmética / (P)onderada)?");

        # Operação Aritmética
        if vr_media.lower() == "a":

                # Zerar variáveis
                vr_qtdNotas = 0;
                vr_media = 0;
                vr_contador = 0;
                vr_soma = 0;

                #Solicita ao usuário a quantidade de notas que será informada
                vr_qtdNotas = int(input("Quantas notas você irá informar?"));

                #Laço de repetição para que o usuário informe as notas conforme quantidade informada anteriormente
                while vr_contador < vr_qtdNotas:
                        #Nota informada pelo usuário
                        vr_nota = float(input("Informe a nota:"));
                        #Efetua a soma dos valores
                        vr_soma = vr_soma + vr_nota;
                        #Incrementa contador para controle do loop
                        vr_contador = vr_contador + 1;

                #Cálculo da média        
                vr_media = vr_soma / vr_qtdNotas;

                #Exibição da média para o usuário
                print("A média aritmética das notas informadas é: " + str(vr_media));     

        # Operação Ponderada
        elif vr_media.lower() == "p":

                # Zerar variáveis        
                vr_qtdNotas = 0;
                vr_nota = 0;
                vr_peso = 0;
                vr_soma = 0;
                vr_somaPeso = 0;
                vr_contador = 0;

                #Solicita ao usuário a quantidade de notas que será informada
                vr_qtdNotas = int(input("Quantas notas você irá informar?"));

                #Laço de repetição para que o usuário informe as notas e os respectivos pesos conforme quantidade informada anteriormente
                while vr_contador < vr_qtdNotas:
                        #Nota informada pelo usuário
                        vr_nota = float(input("Informe a nota:"));
                        #Atribui o valor da nota informada em uma lista para uso posterior
                        vr_listaNota.append(vr_nota);

                        #Peso da nota acima informada pelo usuário
                        vr_peso = float(input("Informe o peso da nota:"));
                        #Atribui o valor do peso da nota informada em uma lista para uso posterior
                        vr_listaPeso.append(vr_peso);

                        #Efetua a soma dos pesos para cálculo da média. Obs.: Isto poderia ser feito adiante.
                        vr_somaPeso = vr_somaPeso + vr_peso;

                        #Incrementa contador para controle do loop
                        vr_contador = vr_contador + 1;

                #Zerar contador para efetuar o cálcula da média, este trecho poderia ter sido feito acima dentro do while
                # Porém preferi separar para que o entendimento seja mais claro
                vr_contador = 0;

                #Laço de repetição para percorrer as informações inseridas pelo usuário
                while vr_contador < vr_qtdNotas:
                        #Soma e cálculo das notas e seus respectivos pesos
                        vr_soma = vr_soma + (vr_listaPeso[vr_contador] * vr_listaNota[vr_contador]);

                        #Incrementa contador para controle do loop
                        vr_contador = vr_contador + 1;

                #Cálculo final da média
                vr_media = vr_soma / vr_somaPeso;

                #Exibição da média para o usuário
                print("A média ponderada é: " + str(vr_media));

        # Operação Inválida               
        else:

                print("Informe um tipo de média válido.");
                continue;

        #Solicita ao usuário se deseja continuar com as operações                       
        vr_opcao = input("Deseja efetuar outra média(S/N) ?");
                                                
        if vr_opcao.lower() != "s":
                vr_continue = False; 
