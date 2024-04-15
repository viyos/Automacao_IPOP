from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas as pd
import openpyxl
import numpy as np
import os

edge_options = webdriver.EdgeOptions()

ser = Service("C:\\Users\\victory\\OneDrive - HDI SEGUROS SA\\Área de Trabalho\\msedgedriver.exe")    

navegador = webdriver.Edge(service=ser)

navegador.maximize_window()

diretorio_geral = r'C:\Users\victory'
diretorio_relatorio = r'\OneDrive - HDI SEGUROS SA\Área de Trabalho\Relatorio_regras.csv'
diretorio_downloads = r'\Downloads'
diretorio_regras = r'\OneDrive - HDI SEGUROS SA\Área de Trabalho\RoboIPOP.xlsx'
diretorio_conferenciaxls = r'\download.xls'
lista = pd.read_excel(diretorio_geral + diretorio_regras)

df = pd.DataFrame(lista)

navegador.get("https://www.hdi.com.br/rosie/ipop_v4/login")

WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.ID,'usuario_input')))
time.sleep(2)

navegador.find_element(By.ID,'usuario_input').send_keys('victory')

navegador.find_element(By.ID,'senha_input').send_keys('Viyos@123')

time.sleep(1)

navegador.find_element('xpath','//*[@id="entrar_button"]').click()

time.sleep(2)

def Remove_Arquivo():
	if os.path.exists(diretorio_geral+diretorio_downloads+diretorio_conferenciaxls):
		os.remove(diretorio_geral+diretorio_downloads+diretorio_conferenciaxls)

def Variaveis(value,valorrow):
	id = value
	valor = valorrow
	valor = str(valor)
	if pd.isna(valorrow) is False:
		igexcemp = valor[0]
		val = valor[1:]
		valores = val.split(',')
		select.select_by_value(id)
		if valorrow == row.Corretora:
			time.sleep(60)
		else:
			pass
		conect = None
		while conect is None:
			try:
				WebDriverWait(navegador, 30).until(EC.element_to_be_clickable(('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/table/tbody/tr[1]')))
				conect = True
			except:
				pass
		time.sleep(5)
		for i in valores:
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[2]/div/label/input').clear()
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[2]/div/label/input').send_keys(i)
			time.sleep(2)
			WebDriverWait(navegador, 30).until(EC.element_to_be_clickable(('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/table/tbody/tr')))
			conect = None
			while conect is None:
				try:
					navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/button[3]').click()
					conect = True
				except:
					pass
			time.sleep(3)
			if igexcemp == '=':
				navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[1]/div/div/app-bootstrap-treeview/div[2]/button[1]').click()
				operador = '='
			else:
				navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[1]/div/div/app-bootstrap-treeview/div[2]/button[2]').click()
				operador = '<>'
			time.sleep(2)	
			dict_idregra = {"Código da Variável": id,"Descrição Operação" : operador ,"Descrição do Conteúdo" : i, "Range Inicial": '', "Range Final": ''}
			global df_compara
			df_compara = pd.concat([df_compara, pd.DataFrame([dict_idregra])], ignore_index=True)

	else:
		pass

def VariaveisRange(valuerange,valorrowrange):
	id = valuerange
	valor = valorrowrange
	valor = str(valor)
	if pd.isna(valorrowrange) is False:
		igexcemp = valor[0]
		val = valor[1:]
		valores = val.split(',')
		select.select_by_value(id)
		WebDriverWait(navegador, 20).until(EC.element_to_be_clickable(('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/form/div/div/div/input[1]')))
		time.sleep(1)
		for i in valores:
			valoresrange = i.split(':')
			valor1 = valoresrange[0]
			valor2 = valoresrange[1]
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/form/div/div/div/input[1]').clear()
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/form/div/div/div/input[1]').send_keys(valor1)
			time.sleep(1)
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/form/div/div/div/input[2]').clear()
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/form/div/div/div/input[2]').send_keys(valor2)
			WebDriverWait(navegador, 30).until(EC.element_to_be_clickable(('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/form/div/div/div/div/div/button[1]')))
			time.sleep(1)
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/form/div/div/div/div/div/button[1]').click()
			WebDriverWait(navegador, 30).until(EC.element_to_be_clickable(('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr')))
			time.sleep(1)
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr').click()
			time.sleep(3)
			if igexcemp == '=':
				navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[1]/div/div/app-bootstrap-treeview/div[2]/button[1]').click()
				operador = '='
			else:
				navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[1]/div/div/app-bootstrap-treeview/div[2]/button[2]').click()
				operador = '<>'
			time.sleep(1)
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/button[3]').click()
			time.sleep(1)
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/button[5]').click()
			time.sleep(2)
			global df_compara
			dict_idregra = {"Código da Variável": id,"Descrição Operação" : operador ,"Descrição do Conteúdo" : '', "Range Inicial": valor1, "Range Final": valor2}
			df_compara = pd.concat([df_compara, pd.DataFrame([dict_idregra])], ignore_index=True)
	else:
		pass

head = 1 

for row in df.itertuples():
	errornot = True
	while errornot == True:
		try:

			df_compara = pd.DataFrame()

			WebDriverWait(navegador, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu_horizontal"]/app-menu-horizontal/nav/a'))) 

			time.sleep(5)

			conect = None
			while conect is None:
				try:
					navegador.find_element('xpath','//*[@id="menu_horizontal"]/app-menu-horizontal/nav/a').click()
					conect = True
				except:
					pass

			WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="menu_vertical"]/app-menu-vertical/nav/app-menu-vertical-item/ul/li[4]/a')))

			#Modulo da Regra
			moduloregra = int(row.Modulo)
			moduloregra = str(moduloregra)
			moduloregra = moduloregra.strip(" ")
			if moduloregra == '1': #Seleciona a opção Subscrição
				navegador.find_element('xpath','//*[@id="menu_vertical"]/app-menu-vertical/nav/app-menu-vertical-item/ul/li[4]/a').click()
			elif moduloregra == '2': #Seleciona a opção Oferta
				navegador.find_element('xpath','//*[@id="menu_vertical"]/app-menu-vertical/nav/app-menu-vertical-item/ul/li[2]/a').click()
			else:
				navegador.find_element('xpath','//*[@id="menu_vertical"]/app-menu-vertical/nav/app-menu-vertical-item/ul/li[3]/a').click()
			
			time.sleep(2)

			WebDriverWait(navegador, 50).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-home/div[3]/app-listar-regras/header[2]/section[1]/button[1]')))	

			time.sleep(4)

			conect = None
			while conect is None:
				try:
					navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/header[2]/section[1]/button[1]').click() #Clicar em nova regra
					conect = True
				except:
					pass

			WebDriverWait(navegador, 20).until(EC.element_to_be_clickable(('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[1]/div/fieldset/div[1]/div[1]/select')))

			time.sleep(2)

			#Tipo Regra
			if moduloregra == '1':
				tpreg = int(row.TipoRegra)
				tpreg = str(tpreg)
				tpreg = tpreg.strip(" ")
				select = Select(navegador.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[4]/div[2]/select'))
				select.select_by_value(tpreg)
			else:
				pass

			#Categoria
			try:
				if moduloregra == '1':
					categ = int(row.Categoria)
					categ = str(categ)
					categ = categ.strip(" ")
					select = Select(navegador.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[4]/div[5]/select'))
					select.select_by_value(categ)
				else:
					pass
			except:
				pass

			#Agravo/Desconto (Ajuste)
			agrdesc = str(row.AgravoDesconto)
			agrdesc = agrdesc.strip(" ")
			if moduloregra == '1' or moduloregra == '3':
				navegador.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[4]/div[1]/div/input").clear()
				navegador.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[4]/div[1]/div/input").send_keys(agrdesc)
			else:
				navegador.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[4]/div[3]/div/input").clear()
				navegador.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[4]/div[3]/div/input").send_keys(agrdesc)
				navegador.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[4]/div[4]/div/input").send_keys('1')

			#Nome da regra
			nomeregra = row.NomeRegra
			navegador.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[1]/div[2]/div/input").clear()
			navegador.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[1]/div[2]/div/input").send_keys(nomeregra)
			
			time.sleep(2)

			#Mensagem
			msgregra = row.Mensagem
			if pd.isna(msgregra) is False:
				try:
					navegador.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[5]/div/textarea").clear()
					navegador.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[5]/div/textarea").send_keys(msgregra)
				except:
					pass
			else:
				pass

			time.sleep(2)

			#Comentario
			comentarioreg = row.Comentario
			if pd.isna(comentarioreg) is False:
				try:
					navegador.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[6]/div/textarea").clear()
					navegador.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[6]/div/textarea").send_keys(comentarioreg)
				except:
					pass
			else:
				pass

			time.sleep(2)

			dtdias = datetime.today() + timedelta(days= 3) 
			dtdias = dtdias.strftime('%d/%m/%Y')
			dtdias = str(dtdias)
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[2]/div[1]/input').send_keys(dtdias)

			dtfinal = '31/12/2070'
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[3]/div[1]/input').send_keys(dtfinal)

			hrinicial = '00:00'
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[2]/div[2]/input').send_keys(hrinicial)

			hrfinal = '23:59'
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/form/fieldset/div[3]/div[2]/input').send_keys(hrfinal)

			select = Select(navegador.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[1]/div/fieldset/div[1]/div[1]/select'))

			select.select_by_value('1')

			time.sleep(4)

			select = Select(navegador.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[2]/div[1]/div/fieldset/div[2]/div[1]/select'))

			select.select_by_value('3')

			time.sleep(5)
			
			valor = "//h5[.='Variáveis']/following-sibling::div/fieldset/div/div[2]//select/option[contains(.,'CPF / CNPJ (agrup')]"

			combobox = "//h5[.='Variáveis']/following-sibling::div/fieldset/div/div[2]//select"

			WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, valor)))

			select = Select(navegador.find_element(By.XPATH, combobox))

			#Empresa
			Variaveis('5',row.Empresa)

			#Filial
			Variaveis('7',row.Filial)

			#Produto
			Variaveis('8',row.Produto)

			#Corretora
			Variaveis('17',row.Corretora)

			#Categoria Tarifaria
			Variaveis('33',row.CatTarifaria)

			#Bonus
			Variaveis('40',row.Bonus)

			#Tipo Operacao
			Variaveis('64',row.TpOperacao)

			#Marca Veiculo
			Variaveis('110',row.MarcaVeic)

			#Forma Contratação
			Variaveis('125',row.FormContrat)

			#Zero KM
			Variaveis('132',row.ZeroKM)

			#Agrupamento Pontuação Serasa
			Variaveis('146',row.AgrupPtoSerasa)

			#Agrupamento RNS Veiculo
			Variaveis('147',row.AgrupRNSVeic)

			#Agrupamento Pontuação Serasa 2
			Variaveis('148',row.AgrupPtoSerasa2)

			#CartaVerde
			Variaveis('190',row.CartaVerde)

			#Tipo Renovação
			Variaveis('191',row.TpRenovacao)

			#Agrupamento CPF CNPJ
			Variaveis('193',row.CpfCnpjAgrup)

			#Tipo Pessoa
			Variaveis('205',row.TpPessoa)

			#Região Circulação Agrupamento
			Variaveis('211',row.RegCirc)

			#Classe Veiculo
			Variaveis('217',row.ClasseVeículo)

			#Utilização Veiculo
			Variaveis('221',row.UtilVeiculo)

			#Tipo Operação Item
			Variaveis('226',row.TpOperacaoItem)

			#Roteiro de Calculo
			Variaveis('228',row.RoteiroCalculo)

			#Código Atividade
			Variaveis('240',row.CodAtividade)

			#Código Alteração Endosso Agrupamento
			Variaveis('295',row.CodAltEndossoAgrup)

			#Fluxo Calculo
			Variaveis('304',row.FluxoCalculo)

			#Codigo Região de Risco
			Variaveis('386',row.CodRegRisco)

			#Tipo Operacao
			Variaveis('394',row.TpOperacao)

			#CEP Circulação
			VariaveisRange('31',row.CEPCirc)

			#Valor Casco IS Merc
			VariaveisRange('47',row.VlCascoISMer)

			#Codigo FIPE
			VariaveisRange('122',row.FIPE)

			#Idade Veiculo
			VariaveisRange('136',row.IdadeVeiculo)

			#Ponto Serasa
			VariaveisRange('138',row.PontoSerasa)

			#Idade Condutor
			VariaveisRange('182',row.IdadeCondutor)

			#Relação Premio Final/ IS %
			VariaveisRange('220',row.RelPremioFinalIS)

			#Fator Aleatorio Controle
			VariaveisRange('234',row.FatorAleatControle)

			#CNAE Principal
			VariaveisRange('272',row.CNAEPrincipal)

			#Fator Aleatorio Controle
			VariaveisRange('279',row.QtMesesRelac)

			#Indice Gini 2010
			VariaveisRange('280',row.Gini2010)

			#IDHM 2010
			VariaveisRange('281',row.IDHM2010)

			#Quantidade de Itens
			VariaveisRange('289',row.QtdItens)

			#Score de Creditos PJ 3
			VariaveisRange('340',row.ScrCrdMerPJ3)

			#Natureza Juridica
			VariaveisRange('347',row.NaturezaJuridica)

			#Score AutoGlass
			VariaveisRange('377',row.ScoreAutoGlass)

			#Score Roubo e Furto
			VariaveisRange('378',row.ScoreRFSerasa)

			#Score Sinistro
			VariaveisRange('379',row.ScoreSinistro)

			time.sleep(4)

			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[3]/div/div/div/div/button[1]').click()

			WebDriverWait(navegador, 20).until(EC.visibility_of_all_elements_located(('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/nav/div/ul[2]/li/button')))

			time.sleep(10)

			#Validação da regra
			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/div[1]/div/div[1]/div/div/app-bootstrap-treeview/button').click() #Baixar Excel com váriaveis

			time.sleep(5)

			valida = pd.read_html(diretorio_geral + diretorio_downloads + diretorio_conferenciaxls, thousands = '.', decimal = ',')

			Remove_Arquivo()

			valida = valida[0]

			valida_ofc = valida[:]

			valida_final =valida_ofc[[0,2,4,5,6]]

			valida_final.rename(columns={0: 'Código da Variável',2: 'Descrição Operação',4: 'Descrição do Conteúdo',5: 'Range Inicial',6: 'Range Final'}, inplace = True)

			valida_final = valida_final.drop(0)

			valida_final = valida_final.fillna('')

			validacao_comand = valida_final.equals(df_compara)

			valida_final = valida_final.sort_values(['Descrição Operação', 'Range Inicial'])

			df_compara = df_compara.sort_values(['Descrição Operação', 'Range Inicial'])

			valida_final["Range Inicial"] = pd.to_numeric(valida_final["Range Inicial"])
			valida_final["Range Final"] = pd.to_numeric(valida_final["Range Final"])

			df_compara["Range Inicial"] = pd.to_numeric(df_compara["Range Inicial"])
			df_compara["Range Final"] = pd.to_numeric(df_compara["Range Final"])

			valida_tabelas = pd.concat([valida_final,df_compara]).drop_duplicates(keep=False)

			if len(valida_tabelas) == 0:
				valid = {"Código da Variável": '',"Descrição Operação" : '' ,"Descrição do Conteúdo" : '', "Range Inicial": '', "Range Final": ''}
				valida_tabelas = pd.DataFrame([valid])
			else:
				pass

			valida_tabelas['Campos Exatamente Iguais'] = validacao_comand

			valida_tabelas['Nome Regra'] = nomeregra

			if head != 1:
				valida_tabelas.to_csv(diretorio_geral + diretorio_relatorio, index=False,mode = 'a',sep=';',header=False)
			else:
				valida_tabelas.to_csv(diretorio_geral + diretorio_relatorio, index=False,mode = 'a',sep=';')

			head = head + 1

			navegador.find_element('xpath','/html/body/app-root/app-home/div[3]/app-listar-regras/div[4]/app-editar-regras/nav/div/ul[2]/li/button').click()
			
			WebDriverWait(navegador, 20).until(EC.element_to_be_clickable(('xpath','/html/body/app-root/app-home/div[2]/app-menu-horizontal/nav/a')))

			errornot = False
		except:
			navegador.get("https://www.hdi.com.br/rosie/ipop_v4/login")

			navegador.refresh()

			WebDriverWait(navegador, 40).until(EC.presence_of_element_located((By.ID,'usuario_input')))

			time.sleep(10)

			navegador.find_element(By.ID,'usuario_input').send_keys('victory')

			navegador.find_element(By.ID,'senha_input').send_keys('Jujubs123')

			time.sleep(1)

			navegador.find_element('xpath','//*[@id="entrar_button"]').click()

			time.sleep(2)