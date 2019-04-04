# -*- coding: cp1252 -*-
'''
resolução do problema dos canibais e missionários

estado inicial: 3 missionários (me = 3) e 3 canibais (ce = 3) do lado esquerdo do rio
 -> me = ce = 3; md = cd = 0
Ojetivo(estado meta): levar todos os canibais e missionários do lado esquerdo para o lado direito, ou seja:
-> ce = md = 0 ; md = cd = 3
condição: a qtd de missionários de um lado do rio não pode menor do que a de canibais
-> ce < = me e cd < = md

onde:
ce = número de canibais no lado esquerdo do rio
me = número de missionários no lado esquerdo do rio
cd = número de canibais no lado direito do rio
md = representa o número de missionários no lado direito do rio
b = 0 ou 1 indica de qual lado está o barco
    b = 1 o barco está no lado esquerdo, b = 0 lado direito
		
'''

class Estado():
	def __init__(self,ce,me,cd,md,b):
		
		self.ce = ce
		self.me = me
		self.cd = cd
		self.md = md
		self.b = b
		self.pai = None
		self.filhos = []


	def valida_estado(self):

		# não se pode ter um valor negativo para o número de missionários e canibais
		if((self.ce < 0) or (self.me < 0) or (self.cd < 0) or (self.md < 0)):
			return False

		# a qtd de missionários de um lado do rio não pode ser menor do que a qtd de canibais 

		return ((self.me == 0 or self.me >= self.ce) and (self.md == 0 or self.md >= self.cd))


	def verifica_estado_final(self):
		#retorna True caso seja o estado meta e False caso contrário
		return ((self.me == self.ce == 0) and (self.md == self.cd == 3))


	def gera_filhos(self):
		novo_lado_barco = 0 if self.b == 1 else 1

                #o barco sempre tem que ter pelo menos uma pessoa
		
		acoes = [
		{'m': 2, 'c': 0}, # colocar 2 missionários no barco
		{'m': 1, 'c': 0}, # colocar 1 missionário no barco
		{'m': 1, 'c': 1}, # colocar 1 missionário e um 1 canibal no barco
		{'m': 0, 'c': 1}, # colocar 1 canibal no barco 
		{'m': 0, 'c': 2}, # colocar 2 canibais no barco
		]

		for acao in acoes:
			if self.b == 1: #saindo do lado esquerdo para o lado direito
				novo_ce = self.ce - acao['c']
				novo_me = self.me - acao['m']
				novo_cd = self.cd + acao['c']
				novo_md = self.md + acao['m']
			else:    		#saindo do lado direito para o lado esquerdo
				novo_cd = self.cd - acao['c']
				novo_md = self.md - acao['m']
				novo_ce = self.ce + acao['c']
				novo_me = self.me + acao['m']


			filho = Estado(novo_ce, novo_me, novo_cd, novo_md, novo_lado_barco)
			filho.pai = self
			if(filho.valida_estado()):
				self.filhos.append(filho)


	def mostra_estado(self):
		print("Margem Esquerda: Missionários = {}, Canibais = {} ".format(self.me, self.ce))
		print("Margem Direita:  Missionários = {}, Canibais = {} ".format(self.md, self.cd))
 

class Problema():

	def __init__(self):
		estadoInicial = Estado(3,3,0,0,1)
		self.fila = [estadoInicial]
		self.solucao = []

	def gera_solucao(self):
		for e in self.fila:
			if e.verifica_estado_final():
				self.solucao.append(e)
				while e.pai:
					self.solucao.insert(0, e.pai)
					e = e.pai

				return

			e.gera_filhos()
			self.fila.extend(e.filhos)


problema = Problema()
problema.gera_solucao()

print ("Estados do problema dos missionários e canibais\n")
for estado in problema.solucao:
        
    
	
	print("\n")
	estado.mostra_estado()
	print("\n")
	print(50 * '*')
	
