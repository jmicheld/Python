# Calculadora feita em Python para fins de estudo da linguagem.
# Somente as principais operações (Soma, Subtração, Multiplicação e Divisão) e com somente dois valores
# Versão 1.0
# Autor: Jean Michel Deschamps
# Data: 05/05/2020

# Exibe ao usuário o título do projeto
print("--- Calculadora JMD 1.0 --- ");

#Inicialização de variáveis, não é necessário.
vr_continue = True;
vr_num1 = 0;
vr_num2 = 0;
vr_opcao = "";

# Laço de repetição para que o usuário continue fazendo suas médias
while vr_continue ==  True:

	# Solicita ao usuário o valor da primeira nota e já efetua a atribuição na variável
	vr_num1 = int(input("Digite o primeiro valor da operação:"));
	
	# Solicita ao usuário qual a operação deseja efetuar
	vr_ope = input("Qual a operação(+-*/)?");
	
	# Solicita ao usuário o valor da primeira nota e já efetua a atribuição na variável
	vr_num2 = int(input("Digite o segundo valor da operação:"));
	
	# Verifica a opção de operação escolhida pelo usuário
	if vr_ope == "+": # Soma
	    print(vr_num1 + vr_num2);
	elif vr_ope == "-": # Subtração
	    print(vr_num1 - vr_num2);
	elif vr_ope == "*": # Multiplicação
	    print(vr_num1 * vr_num2);
	elif vr_ope == "/": # Divisão
	    print(vr_num1 / vr_num2);
	else: # Caso tenha sido informado uma operação inválida o usuário será informado e volta para o início
	   print("Informe um operador válido");
	   continue;

	# Solicita ao usuário se o mesmo deseja continuar com as operações
	vr_opcao = input("Deseja continuar(S/N) ?");
	
	# Caso o usuário informe alguma opção diferente de S/s para permanecer no programa ele irá sair
	if vr_opcao.lower() != "s":
		vr_continue = False; 
