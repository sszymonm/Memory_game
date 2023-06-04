import random as r
import tkinter as tk

class MyGUI:

    def __init__(self):

        self.runda=0
        self.tabPamieci = []
        self.licznikPoprawnych=0
        self.rundyDoKonca=1
        self.b = [0,1,2,3]

        self.root=tk.Tk()
        self.root.resizable(width=False, height=False)
        self.root.title("Memory game")
        self.root.configure(background='white')

        self.logo = tk.Label(self.root, text="Memory game!", font=('Arial', 26,"bold"), bg="white")
        self.logo.pack(pady=5)

        self.startButton = tk.Button(self.root, width="40", height="5", bg="lightblue", command=self.start, text="Start", font=('Arial',18,"bold"))
        self.startButton.pack(side="bottom",pady=20)

        for z in range(0,4):
            self.b[z] = tk.Button(self.root, width="20", height="10", command=self.pustka, bg="black")
            self.b[z].pack(side="left", padx=15,pady=10)


        self.root.mainloop()

    def pustka(self):
        pass

    def sprawdz(self,x):

        if(x==self.tabPamieci[self.licznikPoprawnych]):

            for z in range(0,4):
                self.b[z].config(command=self.pustka)

            self.b[x].configure(bg="yellow")
            self.root.update()
        
            self.root.after(1000)

            self.b[x].configure(bg="black")
            self.root.update()

            self.licznikPoprawnych+=1
            self.rundyDoKonca-=1

            for x in range(0,4):
                self.b[x].configure(command=lambda a=x: self.sprawdz(a))
            
            if(self.rundyDoKonca == 0):
                self.root.after(1000,self.pokaz)

        elif(x!=self.tabPamieci[self.licznikPoprawnych]):
            self.startButton.configure(text="Oops! (Click to start a new game)",command=self.start)
            for z in range(0,4):
                self.b[z].configure(command=self.pustka)
        
            self.runda=0
            self.rundyDoKonca=1
            self.licznikPoprawnych=0

    def start(self):

        for x in range(0,1000,1):
            self.tabPamieci.append(r.randint(0,3))

        for z in range(0,4):
            self.b[z].config(command=lambda a=x: self.sprawdz(a))
        
        self.startButton.configure(text="turn: 1", command=self.pustka)
        self.pokaz()

    def pokaz(self):

        for z in range(0,4):
            self.b[z].config(command=self.pustka)
            
        self.startButton.configure(text="Take a look! (turn: " + str(self.runda+1) + ")")
        
        i = 0
        while i <= self.runda:
            
            self.b[self.tabPamieci[i]].configure(bg="yellow")

            self.root.update()
            self.root.after(1000)

            self.b[self.tabPamieci[i]].configure(bg="black")
            self.root.update()
            self.root.after(1000)

            i=i+1

        
        self.runda=self.runda+1
        self.rundyDoKonca=self.runda
        self.licznikPoprawnych=0

        i=0

        self.startButton.configure(text="Your turn! (turn: " + str(self.runda) + ")")

        for x in range(0,4):
            self.b[x].configure(command=lambda a=x: self.sprawdz(a))
        

MyGUI()