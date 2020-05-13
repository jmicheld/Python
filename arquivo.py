# Programa de manipulação de arquivos para fins de estudos da linguagem Python
# Versão 1.0
# Autor: Jean Michel Deschamps
# Data: 13/05/2020

#Variável de controle para continuar com as ações em arquivos
vr_continue = True;

while vr_continue == True:

    # Cabeçalho do sistema para exibir as informações ao usuário
    print("------------------------------------------------------------");
    print("|                   Manipulação de Arquivo                 |");
    print("|                                                          |");
    print("| - R  - Somente Leitura					                  |");
    print("| - W  - Escrita(Apaga o arquivo já criado)                |");
    print("| - A  - Leitura e Escrita(Add no Final do arquivo)        |");
    print("| - R+ - Leitura e Escrita 				                  |");
    print("| - W+ - Escrita(o modo W+, assim como o W, também         |");
	print("|                apaga o conteúdo anterior do arquivo)     |");
	print("| - A+ - Leitura e escrita(Abre o arquivo para atualização |");
    print("------------------------------------------------------------");

	# Solicita ao usuário qual o tipo de ação deseja efetuar
	vr_tipoAcao = int(input("Qual ação deseja efetuar?"));

	# Condição para verificar qual o valor do veículo informado acima
	if vr_tipoAcao.lower() == "r":
		print("Valor a ser cobrado é: R$ " + vr_listaValores[var_tipoVeiculo]);
		vr_contCarro = vr_contCarro + 1;
	elif vr_tipoAcao.lower() == "w":
		print("Valor a ser cobrado é: R$ " + vr_listaValores[var_tipoVeiculo]);
		vr_contMoto = vr_contMoto + 1;
	elif vr_tipoAcao.lower() == "a":
		print("Ação: A.");
	elif vr_tipoAcao.lower() == "r+":
	elif vr_tipoAcao.lower() == "w+":
	elif vr_tipoAcao.lower() == "a+":
		
	else:
		print("Informe um tipo de veículo válido.");
		continue;
		
	vr_continue = int(input("Deseja continuar?"));
	