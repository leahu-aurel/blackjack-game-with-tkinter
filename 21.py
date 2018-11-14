from tkinter import *
import sys, random,PIL.Image, PIL.ImageTk, time, tkinter.messagebox
import vars as var
import cards as deck
from collections import defaultdict

class Window(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry(("800x600"))
        self.root.title("Blackjack by Aurel")
        try:
            self.root.wm_iconbitmap("playing_cards/icon.ico")
        except:
            pass

        self.root.bind("<Escape>", sys.exit)

        #Creating the main menu
        mainMenu = Menu(self.root)
        self.root.config(menu = mainMenu)

        subMenu = Menu(mainMenu, tearoff = 0)
        mainMenu.add_cascade(label = "Rules", command = self.gameRules)
        mainMenu.add_cascade(label = "Help", menu = subMenu)

        subMenu.add_command(label = "Known bugs", command = self.knownBugs)
        subMenu.add_command(label = "Report a bug", command = self.reportBug)
        subMenu.add_separator
        subMenu.add_command(label = "How to play", command = self.howToPlay)

        self.root.resizable(False,False)
        self.root['bg'] = var.BACKGROUND

        #Starting the game rules gameScreen

        self.gameRulesScreen()

        self.root.mainloop()

    #Menu functions

    def knownBugs(self):

        newWindow = Toplevel()

        newWindow.wm_title("Known bugs")
        text = Label(newWindow, text = """You can see below the knownBugs:
                                          1.................................
                                          2................................
                                          3...........................................
                                          P.S.In process""")
        text.pack(side="top", fill="both", expand=True, padx=10,pady=10)
      #may add some functionality, like, if it already is in the file, make it not add

    def reportBug(self):
        newWindow = Toplevel()
        newWindow.wm_title("Report a bug")

        text = Label(newWindow, text = "Reporting bugs helps the developers make the game better")
        self.reportEntry = Entry(newWindow)
        ok = Button(newWindow, text = "Send", command = self.getReport)


        text.pack()
        self.reportEntry.pack()
        ok.pack()

    def getReport(self):

        print(">>>", self.reportEntry.get())
        file = open("reportbugs.txt","a")
        file.write('\n'+self.reportEntry.get())

        file.close()

    def howToPlay(self):
        print("Have to do")

    def gameRules(self):
        print("Have to do this too")

    def mainMenu(self):
        self.frameRules.destroy()
        self.p = 0
        self.points = {}
        self.namePlayer = 0
        self.wins = {}
        self.wins = defaultdict(lambda: 0, self.wins)


        self.frameTitle = Frame(self.root, bg = var.BACKGROUND)
        self.frameTitle.pack()

        self.start_but = Button(self.frameTitle, text="Start 21",
        pady=10,command=self.entryNames,padx=15,fg="darkblue",
        bg="ghostwhite",relief=GROOVE)

        self.options_but = Button(self.frameTitle, text="Options",
        command = self.options, pady=10, padx=21,
        fg='darkblue',bg="ghostwhite",relief=GROOVE)

        self.exit_but = Button(self.frameTitle, text="Exit 21",
        command=self.exit, pady=10,padx=17,
        fg='darkblue',bg="ghostwhite",relief=GROOVE)
        #I can make a page with my photo and my info and a "back" button

        self.developer = Label(self.frameTitle, text="Made by Aurel")

        self.start_but.pack()
        self.options_but.pack()
        self.exit_but.pack()
        self.developer.pack(side=BOTTOM)

    def entryNames(self):
        self.frameTitle.destroy()
        self.frameNames = Frame(self.root, bg = var.BACKGROUND)
        self.frameNames.pack()

        self.v = IntVar()

        Label(self.frameNames,
                 text="""How many players?""",
                 justify = LEFT,
                 padx = 20).pack()
        Radiobutton(self.frameNames,
                      text="1",
                      padx = 20,
                      variable=self.v,
                      value=1).pack(anchor=N)
        Radiobutton(self.frameNames,
                      text="2",
                      padx = 20,
                      variable=self.v,
                      value=2).pack(anchor=N)
        Radiobutton(self.frameNames,
                      text="3",
                      padx = 20,
                      variable=self.v,
                      value=3).pack(anchor=N)
        Radiobutton(self.frameNames,
                      text="4",
                      padx = 20,
                      variable=self.v,
                      value=4).pack(anchor=N)


        Button(self.frameNames, text="Show", command=self.names).pack()

    def names(self):
        self.g=self.v.get()
        if self.g==4:
            Label(self.frameNames, text="      Name of first player:").pack()
            e1 = Entry(self.frameNames)
            e1.pack()
            Label(self.frameNames, text="Name of second player:").pack()
            e2 = Entry(self.frameNames)
            e2.pack()
            Label(self.frameNames, text="     Name of third player:").pack()
            e3 = Entry(self.frameNames)
            e3.pack()
            Label(self.frameNames, text="  Name of fourth player:").pack()
            e4 = Entry(self.frameNames)
            e4.pack()
        elif self.g==3:
            Label(self.frameNames, text="      Name of first player:").pack()
            e1 = Entry(self.frameNames)
            e1.pack()
            Label(self.frameNames, text="Name of second player:").pack()
            e2 = Entry(self.frameNames)
            e2.pack()
            Label(self.frameNames, text="     Name of third player:").pack()
            e3 = Entry(self.frameNames)
            e3.pack()
        elif self.g==2:
            Label(self.frameNames, text="      Name of first player:").pack()
            e1 = Entry(self.frameNames)
            e1.pack()
            Label(self.frameNames, text="Name of second player:").pack()
            e2 = Entry(self.frameNames)
            e2.pack()
        else:
            Label(self.frameNames, text="      Name of first player:").pack()
            e1 = Entry(self.frameNames)
            e1.pack()


        globals().update(locals())

        Button(self.frameNames, text="Start", command=self.saveEntries).pack()

    def saveEntries(self):
        if self.g==4:
            self.s1= e1.get()
            self.s2= e2.get()
            self.s3= e3.get()
            self.s4= e4.get()
            e1.delete(0,END)
            e1.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
        elif self.g==3:
            self.s1= e1.get()
            self.s2= e2.get()
            self.s3= e3.get()
            e1.delete(0,END)
            e1.delete(0,END)
            e3.delete(0,END)
        elif self.g==2:
            self.s1= e1.get()
            self.s2= e2.get()
            e1.delete(0,END)
            e1.delete(0,END)
        else:
            self.s1= e1.get()
            e1.delete(0,END)
        self.play()

    def options(self):
        self.frameTitle.destroy()

        self.frameOptions = Frame(self.root,bg= var.BACKGROUND)
        self.frameOptions.pack()

        self.bg_var = False

        self.bg_but = Button(self.frameOptions,
        text="Night Mode",command = self.nightMode)

        self.mainmenu_but = Button(self.frameOptions,
        text="Return to main menu", command=self.changeMenu,
        fg="white",bg="darkgrey",font=("Verdana","15","bold"))

        self.bg_but.pack()
        self.mainmenu_but.pack(side=BOTTOM)

    def changeMenu(self):
        self.frameOptions.destroy()
        self.mainMenu()

    def nightMode(self):
        self.bg_var = not self.bg_var

        if self.bg_var:
            self.root['bg'] = 'black'
            self.frameOptions['bg'] = 'black'

            var.BACKGROUND = 'black'
        else:
            self.root['bg'] = 'lightgrey'
            self.frameOptions['bg'] = 'lightgrey'

            var.BACKGROUND = 'lightgrey'

    def exit(self):
        quit()

    def play(self):
        deck.makeDeck()
        self.p += 1
        #Preloaded FRAMES
        self.frameGame = Frame(self.root)
        #canvas for the game
        self.gameScreen = Canvas(self.frameGame,
        width=800,height=600)
        width=int("125")
        height=int("181")
        self.image1 = PIL.Image.open("playing_cards/background.jpg")
        self.image1 = self.image1.resize((800, 600), PIL.Image.ANTIALIAS)
        self.image1 = PIL.ImageTk.PhotoImage(self.image1)
        self.image2 = PIL.Image.open("playing_cards/playing-card-back.jpg")
        self.image2 = self.image2.resize((width, height), PIL.Image.ANTIALIAS)
        self.image2 = PIL.ImageTk.PhotoImage(self.image2)
        self.gameScreen.create_image(0,0, image=self.image1, anchor=NW)

        self.frameNames.destroy()
        self.frameGame.pack()
        self.gameScreen.pack()

        for i in range(5):
            self.gameScreen.create_image(int(eval("10+({}*4)".format(i))),int(eval("30-({}*4)".format(i))), image=self.image2, anchor=NW)

        if self.p == self.g+1:
            self.t = max(self.points, key=self.points.get)
            if "1" in self.t:
                self.namePlayer = self.s1
            elif "2" in self.t:
                self.namePlayer = self.s2
            elif "3" in self.t:
                self.namePlayer = self.s3
            elif "4" in self.t:
                self.namePlayer = self.s4
            self.wins["{}".format(self.namePlayer)]+=1

            tkinter.messagebox.showinfo('End of the game',"{} won this game. He now has {} win/(s)".format(self.namePlayer,self.wins["{}".format(self.namePlayer)]))
            answer = tkinter.messagebox.askquestion("End of the game","Do you want to play again?")
            if answer == "yes":
                self.p = 0
                self.frameGame.destroy()
                self.play()
                self.points={}
            if answer == "no":
                self.frameGame.destroy()
                self.mainMenu()


        #creating the scenario
        self.startTheGame(self.root)

    def startTheGame(self,root):
        self.d={}
        self.tp={}
        self.width1=int(500/4)
        self.height1=int(726/4)
        self.i ={}

        self.r=1
        self.bust = False
        for s in range(2):
            self.i["{}".format(s)] = deck.randomChoice()
            self.tp["tp{}{}".format(s,self.p)] = 0
            self.tp["tp{}{}".format(s,self.p)] += var.calculateValue(self.i["{}".format(s)],self.tp["tp{}{}".format(s,self.p)], sum(self.tp.values()), self.tp.values())

            self.d["im{}{}".format(s,self.p)] = PIL.Image.open("playing_cards/"+self.i["{}".format(s)]+".png")
            self.d["im{}{}".format(s,self.p)] = self.d["im{}{}".format(s,self.p)].resize((self.width1, self.height1), PIL.Image.ANTIALIAS)
            self.d["im{}{}".format(s,self.p)] = PIL.ImageTk.PhotoImage(self.d["im{}{}".format(s,self.p)])
            self.d["im1{}{}".format(s,self.p)] = self.gameScreen.create_image(30, 10, anchor=NW,image=self.d["im{}{}".format(s,self.p)])

            for x in range(0,30):
                self.gameScreen.move(self.d["im1{}{}".format(s,self.p)], int(eval("6+{}".format(s))),12)
                self.gameScreen.update()
                time.sleep(0.01)
        self.creatingChoices()

    def creatingChoices(self):

        self.gameScreen.create_text(650,400,text="Click your choice below:", font=26, fill="white")
        self.gameScreen.create_text(650,450,text="Hit", font =20, fill="white")
        self.gameScreen.create_text(650,500,text="Stand", font =20, fill="white")
        self.gameScreen.bind("<ButtonRelease-1>", self.hit)

    def gameRulesScreen(self):
        self.frameRules = Frame(self.root, bg="black")
        self.frameRules.pack()

        self.ok_but = Button(self.frameRules, text="Ok!",
        command = self.mainMenu, pady=40,padx=190,fg="darkblue",
        bg="ghostwhite", relief=GROOVE)
        self.quit_but = Button(self.frameRules, text="Quit!",
        command = self.root.quit, pady=40,padx=190,fg="darkblue",
        bg="ghostwhite", relief=GROOVE)

        self.rules= Label(self.frameRules, bd=1, relief = SUNKEN,
         pady=260, padx=350, text="Blackjack Rules",
        fg="ghostwhite",bg="black",font=('Verdana',20))

        self.rules.pack()
        self.ok_but.pack(side=LEFT)
        self.quit_but.pack(side=LEFT)

    def hit(self, event):
        self.coords = self.gameScreen.coords(self.d["im1{}{}".format(self.r,self.p)])
        self.points["{}".format(self.p)] = sum(self.tp.values())
        if self.coords[1]>360:
            if sum(self.tp.values()) > 21:
                if 11 in self.tp.values():
                    self.reversedtp = {val:key for (key, val) in self.tp.items()}
                    self.reversedtp[1] = self.reversedtp[11]
                    del self.reversedtp[11]
                    self.tp = {val:key for (key, val) in self.reversedtp.items()}
                    print(self.tp)
                    print(self.tp.values())

                else:
                    self.bust = True
                    self.gameScreen.create_text(450,100,text="""You busted, after 3 seconds,
                     the cards will be given to the next player:""", font=20, fill="white")
                    self.gameScreen.update()
                    time.sleep(3)
                    self.frameGame.destroy()
                    self.points["Player{}".format(self.p)] = 0
                    self.play()

            if self.bust == False:
                if 610<event.x<700 and 430<event.y<470:
                    self.r+=1
                    self.i["{}".format(self.r)] = deck.randomChoice()
                    self.tp["tp{}{}".format(self.r,self.p)] = 0
                    self.tp["tp{}{}".format(self.r,self.p)] += var.calculateValue(self.i["{}".format(self.r)],self.tp["tp{}{}".format(self.r,self.p)], sum(self.tp.values()), self.tp.values())
                    self.d["im{}{}".format(self.r,self.p)] = PIL.Image.open("playing_cards/"+self.i["{}".format(self.r)]+".png")
                    self.d["im{}{}".format(self.r,self.p)] = self.d["im{}{}".format(self.r,self.p)].resize((self.width1, self.height1), PIL.Image.ANTIALIAS)
                    self.d["im{}{}".format(self.r,self.p)] = PIL.ImageTk.PhotoImage(self.d["im{}{}".format(self.r,self.p)])
                    self.d["im1{}{}".format(self.r,self.p)] = self.gameScreen.create_image(30, 10, anchor=NW,image=self.d["im{}{}".format(self.r,self.p)])

                    for x in range(0,30):
                        self.gameScreen.move(self.d["im1{}{}".format(self.r,self.p)], int(eval("6+{}".format(self.r))),12)
                        self.gameScreen.update()
                        time.sleep(0.01)

                elif 600<event.x<700 and 480<event.y<520:
                    self.frameGame.destroy()
                    self.play()





if __name__ == "__main__":

    Window()
