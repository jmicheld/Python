# Programa de pedágio para fins de estudos da linguagem Python
# Efetua a cobrança de pedágio em rodovias e exibe a quantidade de veículos ao final
# Versão 1.0
# Autor: Jean Michel Deschamps
# Data: 06/05/2020

# Aconselho a quem estiver estudando a linguagem que implemente neste código a parte de troco que o usuário do pedágio deve dar ao motorista do veículo
# Seria legal tbm elaborar um controle da abertura da cancela após o pagamento

# Variáveis
var_tipoVeiculo = 0; # 0 - Carro / 1 - Moto / 2 - Vans, Trator e Caminhões Pequenos / 3 - Carretas(4 Eixos) / 4 - Eixo Extra
vr_continue = True;
vr_eixoExtra = "N";
vr_qtdEixoExtra = 0;

# Variáveis contadores de veículos
vr_contCarro = 0;
vr_contMoto = 0;
vr_contVan = 0;
vr_contCarreta = 0;
vr_contEixoExtra = 0;

# Array que contém os valores do pedágio, o valor de cada veículo está de acordo com os códigos de veículos informados acima
# Como este "sistema" não tem conexão com banco de dados, caso queira alterar algum valor o faça nesta lista declarada abaixo
vr_listaValores = ["2,70", "1,50", "3,50", "6,78", "1,53"];

while vr_continue == True:

	# Cabeçalho do sistema para exibir as informações ao usuário
	print("---------------------------------------------");
	print("|             SISTEMA DE PEDÁGIO             |");
	print("|                                            |");
	print("| - 0 - Carro                     - R$ " + vr_listaValores[0] +"  |");
	print("| - 1 - Moto                      - R$ " + vr_listaValores[1] +"  |");
	print("| - 2 - Vans e Caminhões Pequenos - R$ " + vr_listaValores[2] +"  |");
	print("| - 3 - Carretas(4 Eixos)         - R$ " + vr_listaValores[3] +"  |");
	print("| - EIXO EXTRA                    - R$ " + vr_listaValores[4] +"  |");
	print("---------------------------------------");

	# Solicita ao usuário qual o tipo de veículo será cobrado
	var_tipoVeiculo = int(input("Qual o tipo de veículo?"));

	# Condição para verificar qual o valor do veículo informado acima
	if var_tipoVeiculo == 0:
		print("Valor a ser cobrado é: R$ " + vr_listaValores[var_tipoVeiculo]);
		vr_contCarro = vr_contCarro + 1;
	elif var_tipoVeiculo == 1:
		print("Valor a ser cobrado é: R$ " + vr_listaValores[var_tipoVeiculo]);
		vr_contMoto = vr_contMoto + 1;
	elif var_tipoVeiculo == 2:
		print("Valor a ser cobrado é: R$ " + vr_listaValores[var_tipoVeiculo]);
		vr_contVan = vr_contVan + 1;
	elif var_tipoVeiculo == 3:
		print("Carretas(4 Eixos)");
		vr_contCarreta = vr_contCarreta + 1;
		vr_eixoExtra = input("Veículo possui mais de 4 eixos(S/N)?");
		if vr_eixoExtra.lower() == "s" :
			vr_qtdEixoExtra = float(input("Qual a quantidade de EIXOS extras?"));
			print("Valor a ser cobrado é: R$ " + vr_listaValores[var_tipoVeiculo] + (vr_qtdEixoExtra * vr_listaValores[4]));
		else:
			print("Valor a ser cobrado é: R$ " + vr_listaValores[var_tipoVeiculo]);
	else:
		print("Informe um tipo de veículo válido.");
		continue;
