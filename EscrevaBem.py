import random
from tkinter import *
import pygame
import cv2

pygame.init()

# INTRODUÇÃO TOP TRENDS EDUCAÇÃO
intro = cv2.VideoCapture('videos/intro.mp4')

while intro.isOpened():
    ret, janela = intro.read()

    if ret:
        cv2.imshow('ESCREVA BEM', janela)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
intro.release()
cv2.destroyAllWindows()

# JANELA E SUAS VARIÁVEIS

janela = Tk()  # CRIAR JANELA

janela.title("ESCREVA BEM")  # TÍTULO DA JANELA

janela.iconbitmap('imagens/logojogo.ico') # ÍCONE DA JANELA

janela.geometry("800x600+275+50")  # TAMANHO E POSIÇÃO DA JANELA

janela.resizable(width=False, height=False)  # RECONFIGURAR TAMANHO DA JANELA

janela.configure(bg='white')  # COR DA JANELA

# MÚSICA DO JOGO
def musicaJogo():
    pygame.mixer.music.load('sons/musicajogo1.mp3')
    pygame.mixer.music.play(loops=10)

#SAIR DO JOGO
def quit():
    pygame.mixer.music.stop()
    janela.quit()

# BOTÕES DE MUTAR E DESMUTAR
muteimg = PhotoImage(file='imagens/desmute2.png')
label3 = Label(janela, image=muteimg)
label3.pack()
label3.place(x=5, y=6)

desmuteimg = PhotoImage(file='imagens/mute2.png')
label4 = Label(janela, image=desmuteimg)
label4.pack()
label4.place(x=5, y=6)

def mutar():
    pygame.mixer.music.pause()
    desmute = Button(janela, image=desmuteimg, bg='white', command=desmutar)
    desmute.place(x=5, y=6)

def desmutar():
    pygame.mixer.music.unpause()
    mute = Button(janela, image=muteimg, bg='white', command=mutar)
    mute.place(x=5, y=6)

# DEPÓSITO DE PERGUNTAS
questoes = [["IREI AO RESTAURANTE...", "ALMOSSAR", "AUMOÇAR", "AUMOSSAR", "ALMOÇAR"],
            ["IREI CONTATAR MEU...", "ADEVOGADO", "ADIVOGADO", "ADIVOGADU", "ADVOGADO"],
            ["COMPREI 200 GRAMAS DE...", "MORTADELLA", "MORTANDELA", "MOTADELA", "MORTADELA"],
            ["VOU DAR UM PASSEIO DE...", "BICECLETA", "BECICLETA", "BECECLETA", "BICICLETA"],
            ["É SEMPRE UM ... RECEBÊ-LO(A) EM MINHA CASA!", "PRASER", "PRAZÊ", "PRASÊ", "PRAZER"]]

# REMOVER ELEMENTOS DA JANELA
def limparElementos():
    elementos = janela.grid_slaves()
    for e in elementos:
        e.destroy()

# INICIAR JOGO
class IniciarJogo:
    def __init__(self, quest):
        limparElementos()
        pygame.mixer.music.pause()

        # BACKGROUND
        self.fundo = PhotoImage(file='imagens/bg.png')
        Label(janela, image=self.fundo).place(relwidth=1, relheight=1)

        # ACRESCENTAR PERGUNTAS
        self.Perguntar = []
        for n in quest:
            self.Perguntar.append(n)
        self.travar = False

        # CONTADOR DE RESPOSTAS CORRETAS
        self.correta = 0

        # CONTADOR DE RESPOSTAS ERRADAS
        self.errada = 0

        # BOTÃO DE AVANÇAR
        self.avancar = Button(janela, width=7, height=1,
                              text="Próxima",
                              bg='blue',
                              fg='white',
                              font=("BigNoodleTitling", 22),
                              command=self.Questao)

        # TOTAL DE PERGUNTAS
        self.numero = 0
        self.totalPerg = 5
        self.Questao()

    # AVANÇAR QUESTÃO
    def Questao(self):
        self.avancar.place(x=352, y=510)

        # RANDOMIZADOR DE PERGUNTAS
        if len(self.Perguntar) > 0 and self.numero < self.totalPerg:
            self.numero += 1
            self.travar = False
            NumAleatorio = random.randint(0, len(self.Perguntar) - 1)

            # FRASE AUXÍLIO
            PerguntarText = self.Perguntar[NumAleatorio][0]

            self.proxQuest = self.Perguntar[NumAleatorio][-1]
            respostas = []

            for i in range(1, 5):
                respostas.append(self.Perguntar[NumAleatorio][i])

            # ------------------------------ EMBARALHAR RESPOSTAS ------------------------------ #

            random.shuffle(respostas)

            self.alternativa1 = respostas[0]
            self.alternativa2 = respostas[1]
            self.alternativa3 = respostas[2]
            self.alternativa4 = respostas[3]

            # ------------------------ CONFIGURAÇÕES DA FRASE DE AUXÍLIO ----------------------- #

            Questao = Entry(janela,
                            font=('BigNoodleTitling', 30),
                            bg='white',
                            fg='black',
                            width=45,
                            justify='center',
                            highlightbackground="#37d3ff")
            Questao.insert(END, PerguntarText)
            Questao.grid(row=0,
                         column=0,
                         columnspan=4,
                         pady=4)
            Questao.place(x=60, y=90)

            # -------------------------- CONFIGURAÇÕES DOS BOTÕES DE RESPOSTA -------------------------- #
            self.opcao1 = Button(janela,
                                 text=self.alternativa1,
                                 font=("BigNoodleTitling", 26),
                                 width=24,  # BOTÃO 1
                                 height=2,
                                 command=self.fiscalizar1,
                                 bg='#e6ac00', fg='black')
            self.opcao1.place(x=60, y=200)

            # ---------------------------------------------------------------------------------------#

            self.opcao2 = Button(janela,
                                 text=self.alternativa2,
                                 font=("BigNoodleTitling", 26),
                                 width=24,  # BOTÃO 2
                                 height=2,
                                 command=self.fiscalizar2,
                                 bg='#e6ac00', fg='black')
            self.opcao2.place(x=415, y=200)

            # ---------------------------------------------------------------------------------------#

            self.opcao3 = Button(janela,
                                 text=self.alternativa3,
                                 font=("BigNoodleTitling", 26),
                                 width=24,  # BOTÃO 3
                                 height=2,
                                 command=self.fiscalizar3,
                                 bg='#e6ac00', fg='black')
            self.opcao3.place(x=60, y=330)

            # ---------------------------------------------------------------------------------------#

            self.opcao4 = Button(janela,
                                 text=self.alternativa4,
                                 font=("BigNoodleTitling", 26),
                                 width=24,  # BOTÃO 4
                                 height=2,
                                 command=self.fiscalizar4,
                                 bg='#e6ac00', fg='black')
            self.opcao4.place(x=415, y=330)

            # ---------------------------------------------------------------------------------------#

            if self.alternativa1 == self.proxQuest:
                self.BtProxQuestao = self.opcao1
            elif self.alternativa2 == self.proxQuest:
                self.BtProxQuestao = self.opcao2
            elif self.alternativa3 == self.proxQuest:
                self.BtProxQuestao = self.opcao3
            elif self.alternativa4 == self.proxQuest:
                self.BtProxQuestao = self.opcao4
                self.Perguntar.pop(NumAleatorio)
        else:
            limparElementos()

            self.white = PhotoImage(file='imagens/resultado.png')
            Label(janela, image=self.white).place(relwidth=1, relheight=1)

            # ----------------------------------- CONFIGURAÇÕES DO RESULTADO ------------------------------------- #

            lb = Label(janela, bg='white', fg='black',
                       text=f'{str(self.correta)}' + f'\n{str(self.errada)}',
                       font=('BigNoodleTitling', 55),
                       justify='center')
            lb.grid(column=0,
                    row=0,  # CONTADOR DE CORRETAS E INCORRETAS
                    padx=50,
                    pady=(188, 15))

            # --------------------------------------------------------------------------------------------------- #

            btmenu = Button(janela,
                            text="RETORNAR",
                            bg='#bfbfbf',
                            font=('BigNoodleTitling', 25),
                            command=criarMenu)  # BOTÃO DE VOLTAR AO MENU
            btmenu.grid(column=0,
                        row=1,
                        pady=150)
            btmenu.place(x=350, y=500)

            # --------------------------------------------------------------------------------------------------- #

    def fiscalizar1(self):
        if not self.travar:
            if self.proxQuest != self.alternativa1:
                self.opcao1.configure(bg='#b30000', fg='#f2f2f2')
                pygame.mixer.music.load('sons/errado.mp3')
                pygame.mixer.music.play()
                self.errada += 1
            else:
                self.opcao1.configure(bg='#006622', fg='#f2f2f2')
                pygame.mixer.music.load('sons/correto.mp3')
                pygame.mixer.music.play()
                self.correta += 1
            self.BtProxQuestao.configure(bg='#006622')
            self.travar = True

    def fiscalizar2(self):
        if not self.travar:
            if self.proxQuest != self.alternativa2:
                self.opcao2.configure(bg='#b30000', fg='#f2f2f2')
                pygame.mixer.music.load('sons/errado.mp3')
                pygame.mixer.music.play()
                self.errada += 1
            else:
                self.opcao2.configure(bg='#006622', fg='#f2f2f2')
                pygame.mixer.music.load('sons/correto.mp3')
                pygame.mixer.music.play()
                self.correta += 1
            self.BtProxQuestao.configure(bg='#006622')
            self.travar = True

    def fiscalizar3(self):
        if not self.travar:
            if self.proxQuest != self.alternativa3:
                self.opcao3.configure(bg='#b30000', fg='#f2f2f2')
                pygame.mixer.music.load('sons/errado.mp3')
                pygame.mixer.music.play()
                self.errada += 1
            else:
                self.opcao3.configure(bg='#006622', fg='#f2f2f2')
                pygame.mixer.music.load('sons/correto.mp3')
                pygame.mixer.music.play()
                self.correta += 1
            self.BtProxQuestao.configure(bg='#006622')
            self.travar = True

    def fiscalizar4(self):
        if not self.travar:
            if self.proxQuest != self.alternativa4:
                self.opcao4.configure(bg='#b30000', fg='#f2f2f2')
                pygame.mixer.music.load('sons/errado.mp3')
                pygame.mixer.music.play()
                self.errada += 1
            else:
                self.opcao4.configure(bg='#006622', fg='#f2f2f2')
                pygame.mixer.music.load('sons/correto.mp3')
                pygame.mixer.music.play()
                self.correta += 1
            self.BtProxQuestao.configure(bg='#006622')
            self.travar = True

# ADICIONAR PERGUNTAS
class Adicionar:
    def __init__(self):
        limparElementos()
        questoes = []
        for add in range():
            questoes1.append(input('Adicione uma pergunta: '))

# MENU
class Menu:
    def __init__(self):
        limparElementos()
        self.fundo = PhotoImage(file='imagens/bg.png')
        Label(janela, image=self.fundo).place(relwidth=1, relheight=1)

        mutar()
        desmutar()

        # ------------------------------------ BOTÃO DE INICIAR ------------------------------------ #

        self.Iniciar = Button(janela, text="INICIAR",
                              padx=17, pady=19, width=20,
                              font=('BigNoodleTitling', 26),
                              bg='#e6ac00', fg='black',
                              activebackground='#006622',
                              activeforeground='white', command=self.criarQuiz)
        self.Iniciar.grid(column=0, row=0, padx=250, pady=350)

        # ------------------------------------- BOTÃO DE SAIR ------------------------------------- #

        self.Sair = Button(janela, text='SAIR', width=20,
                           padx=17, pady=19,
                           font=('BigNoodleTitling', 26),
                           bg='#e6ac00', fg='black',
                           activebackground='#b30000',
                           activeforeground='white',
                           command=quit)
        self.Sair.place(x=250, y=465)

        self.logo = PhotoImage(file='imagens/logojogo.png')
        self.label2 = Label(janela, image=self.logo)
        self.label2.place(x=250, y=30)

        # -------------------------------------- BOTÃO MENU -----------------------------------------#
        menuu = Button(janela, text='Menu', bg='white', command=self.criarQuiz2)
        menuu.place(x=755, y=6)

    def criarQuiz(self):
        self.label2.destroy()
        self.Sair.destroy()
        q = IniciarJogo(questoes)

    def criarQuiz2(self):
        self.label2.destroy()
        self.Sair.destroy()
        m = Adicionar(questoes1)

# FUNÇÃO PARA CRIAR O MENU
def criarMenu():
    musicaJogo()

    m = Menu()
