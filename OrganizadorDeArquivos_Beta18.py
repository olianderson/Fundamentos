# DESCRIÇÃO: Este código deve percorrer a pasta Downloads de qualquer PC com SO Windows a procura de arquivos com formatos predefinidos
# e movê-los para subpastas de Organizador de Arquivos conforme extensão.
# Este executável pede um usuário, senha e um cod de verificação.
# Só assim o CÓDIGO para organizar arquivos será executado.
# PROBLEMA 1: Dá erro quando executado pela segunda vez(BETA 16). ---> STATUS: Corrigido
# PROBLEMA 2: Só executa quando localizado na área de trabalho(BETA 17) ---> STATUS: Pendente
# ACRESCENTAR: Informar a quantidade de arquivos nas pastas. ---> STATUS: Feito

import os
import shutil
from tkinter import*
from random import*
from datetime import*

login = Tk() # Cria a 'Jenala principal'
login.title('Janela de Identificação')
login.geometry('300x200+600+100') # LxA+E+T

hoje = date.today()

caracteres = '0123456789ABCDEFGHIJLMNOP1RSTUVXZabcdefghijlmnopqrstuvxz' # Armazena caracters 
senha = ''
for x in range(5):
    senha = senha + choice(caracteres)     # Gera uma senha aleatória que serve como cod de verificação

print('CÓDIGO PARA VERIFICAÇÃO: ', senha) # Mostra a senha no shell
print('')

# Isso cria um objeto de Tk que é a janela principal
# Todo metodo criado dentro de uma classe deve definir como primeiro parametro o self(o nome do objeto a ser invocado na classa pelo metodo)
class janela():
    def __init__(self, login): 
        
        self.textTela = Label(login, text = 'TELA DE IDENTIFICAÇÃO', font = ('Verdana', '10', 'bold'))
        self.textTela.grid(row = 0, column = 1)

        self.textNome = Label(login, text = 'Usuário: ', fg = 'red', font = ('Verdana', '8')) 
        self.textNome.grid(row = 1, column = 0, stick = W)

        self.campNome = Entry(login) 
        self.campNome.grid(row = 1, column = 1, stick = W)

        self.textSenha = Label(login, text = 'Senha: ', fg = 'red', font = ('Verdana', '8'))
        self.textSenha.grid(row = 2, column = 0, stick = W)

        self.campSenha = Entry(login, show = '*')
        self.campSenha.grid(row = 2, column = 1, stick = W)

        self.textVerificar = Label(login, text = 'VERIFICAÇÃO: ', fg = 'red', font = ('Verdana', '8')) 
        self.textVerificar.grid(row = 3, column = 0)

        self.campVerificar = Entry(login) 
        self.campVerificar.grid(row = 3, column = 1, stick = W)

        self.botao = Button(login, text = 'Entrar', font = ('Verdana', '8', 'bold'), fg = 'blue', bg = 'yellow', command = self.confirmar) 
        self.botao.grid(row = 4, column = 1, stick = W)

        self.botao1 = Button(login, text = 'Fechar', font = ('Verdana', '8', 'bold'), fg = 'blue', bg = 'yellow', command = self.sair)
        self.botao1.grid(row = 4, column = 1)

        self.textHora = Label(login, text = (hoje.day,'de',hoje.month,'de', hoje.year), font = ('Verdana', '10', 'bold'))
        self.textHora.grid(row = 5 , column = 1, stick = W)

    def sair(self):
        login.destroy()
    
    def confirmar(self):
        usuario = self.campNome.get()

        senha_user = self.campSenha.get() 
                    
        verifi = self.campVerificar.get() 

        if usuario == 'lima.anderson' and senha_user == '1522' and verifi == senha:
            print('ACESSO PERMITIDO PARA: ', usuario)
            print('')
            
            def main(): 
                cwd = os.getcwd() 
                down = os.path.expanduser('~\Downloads') 
                
                try:
                    
                    os.mkdir('Organizador')
                    os.mkdir('Organizador\Musicas')
                    os.mkdir('Organizador\Documentos')

                    rec_music = os.path.abspath('Organizador\Musicas') 
                    rec_doc = os.path.abspath('Organizador\Documentos')
    
                    for (nome, sub, arqs) in os.walk(os.path.join(down)):
                        for file in arqs:
                            if file.endswith('.mp3'): 
                                print('Foi encontrado o seguinte arquivo de formato MP3: ')
                                print(file)
                                print('')

                                caminho = os.path.join(nome, file) 
                                shutil.move(caminho, rec_music) 
                                
                       
                            if file.endswith('.docx'): 
                                print('Foi encontrado o seguinte arquivo de formato DOCX: ')
                                print(file)
                                print('')


                                caminho = os.path.join(nome, file) 
                                shutil.move(caminho, rec_doc) 

                except:

                    rec_music = os.path.abspath('Organizador\Musicas') 
                    rec_doc = os.path.abspath('Organizador\Documentos') 
    
                    for (nome, sub, arqs) in os.walk(os.path.join(down)): 
                        for file in arqs:
                            if file.endswith('.mp3'): 
                                print('Foi encontrado o seguinte arquivo de formato MP3: ', file)
                                print('')

                                caminho = os.path.join(nome, file) 
                                shutil.move(caminho, rec_music) 
                    
                            if file.endswith('.doc'):
                                print('Foi encontrado o seguinte arquivo de formato DOCX: ', file)
                                print('')
                                
                                caminho = os.path.join(nome, file) 
                                shutil.move(caminho, rec_doc)
                
            main() 
        else:
            print('ACESSO NEGADO!')

janela(login)
login.mainloop() 

try:
    print('')
    print('A pasta Musicas do Organizador de Arquivos possui: ', len(os.listdir('Organizador\Musicas')), 'arquivos.')
    print('A pasta Documentos do Organizador de Arquivos possui: ', len(os.listdir('Organizador\Documentos')),'arquivos.')
    print('Encerrando...')
except:
    print('A pasta Orgazanizador de Arquivos ainda não foi criada. ')
    exit()
