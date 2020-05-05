# Calculadora feita em Python para fins de estudo da linguagem.
# Somente as principais operações (Soma, Subtração, Multiplicação e Divisão) e com somente dois valores
# Versão 1.0
# Autor: Jean Michel Deschamps
# Data: 05/05/2020

print("--- Calculadora JMD 1.0 --- ");

#Inicialização de variáveis, não é necessário.
vr_continue = True;
vr_num1 = 0;
vr_num2 = 0;
vr_opcao = "";

while vr_continue ==  True:

	vr_num1 = int(input("Digite o primeiro valor da operação:"));
	vr_num2 = int(input("Digite o segundo valor da operação:"));
	vr_ope = input("Qual a operação(+-*/)?");

	if vr_ope == "+":
	    print(vr_num1 + vr_num2);
	elif vr_ope == "-":
	    print(vr_num1 - vr_num2);
	elif vr_ope == "*":
	    print(vr_num1 * vr_num2);
	elif vr_ope == "/":
	    print(vr_num1 / vr_num2);
	else:
	   print("Informe um operador válido");
	   continue;

	vr_opcao = input("Deseja continuar(S/N) ?");
	if vr_opcao == "N":
		vr_continue = False; 
