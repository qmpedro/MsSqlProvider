import pyodbc

class Conecta:
	bd = str()
	banco = str()
	login = str()
	senha = str()
	query = str()
	
	def __init__(self):
		self.inicio()

	def inicio(self):
		self.bd = input("Servidor: ")
		self.banco = input("Banco: ")
		self.login = input("Login: ")
		self.senha = input("Senha: ")
		self.dados()

	def dados(self):
		global query
		self.query = input("Query ('exit' pra sair): ")
		if self.query == 'exit': return
		print(' ')
		print('Aguarde...')
		self.conecta()

	def conecta(self):	
		try:			
			cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+self.bd+';DATABASE='+self.banco+';UID='+self.login+';PWD='+self.senha)
			cursor = cnxn.cursor()
			cursor.execute(self.query)
			rows = cursor.fetchall()
			print('________________________________________________________')
			for row in rows:
				print(row)			
			print('________________________________________________________')

			self.dados()
			
		except Exception as ex:
			print(' ')
			print('Erro ao conectar. Tente novamente')
			print(' ')
			continua = input('Deseja tentar novamente? (s/n)')
			print(' ')
			if continua == 's':
				self.inicio()
