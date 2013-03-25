from Tkinter import *

class App:

    def __init__(self, master):

        self.index = 0
        
        
        self.frame = master
        w = Label(self.frame, text = "Ring-O-Matic 5000", font=("Helvetica",45) , fg = "blue")
        w.place(x=0,y=0)
        w1 = Label(self.frame, text = "Noises-Off", font=("Helvetica",35), fg = "red")
        w1.place(relx=.25,y = 50)

        self.go = False
        
    #Start listbox
        self.listbox = Listbox(selectmode = SINGLE)
        self.listbox.config(activestyle= "dotbox")
        self.listbox.place(x = 25 , y = 200)
        one = "scene one"
        two = "scene two"
        three = "scene three"
        four= "scene four"
        lists = [one, two, three, four]
        for item in lists:
              self.listbox.insert(END, item)
        self.length = self.listbox.size()
    #End listbox
     
        self.sceneup = Button(self.frame, text="Previous Scene", command=self.sceneminus)
        self.sceneup.place(x = 250 , y = 200)

        self.scenedown = Button(self.frame, text="Next Scene", command=self.sceneplus)
        self.scenedown.place(x = 250 , y = 250)

        self.currentLabel = Label(self.frame, text = "Current Selection: ")
        self.currentLabel.place(x=20,y=375)

        self.b_activate = Button(self.frame, text="Start", command=self.activate)
        self.b_activate.place(x = 50 , y = 150)

        self.b_kill = Button(self.frame, text="End", command=self.end)
        self.b_kill.place(x = 110, y = 150)
                
        self.current = StringVar()
        self.current.set(str(self.listbox.get(ACTIVE)))
        self.currentSel = Label(self.frame, textvariable = self.current)
        self.currentSel.place(x = 135 , y = 375)

        self.runLoop()
        self.printCurrent()

    def activate(self):
        self.go = True
        
    def end(self):
        self.go = False
    

    def sceneplus(self):
        self.index = self.index+1
        if self.index > self.length-1:
            self.index = self.length -1
        self.listbox.activate(self.index)
    def sceneminus(self):
        self.index = self.index-1
        if self.index <= 0:
            self.index = 0
        self.listbox.activate(self.index)

    def runLoop(self):
        if self.go:
            currentScene = self.listbox.get(ACTIVE)
            if currentScene == "scene one":
                print "Scene One"
            elif currentScene == "scene two":
                print "Scene Two"
            elif currentScene == "scene three":
                print "Scene Three"
            elif currentScene == "scene four":
                print "Scene Four"
        self.frame.after(1,self.runLoop)
    
    def printCurrent(self):
         try:
            index1 = int(self.listbox.curselection()[0])
            self.listbox.activate(index1)
            self.index=index1
         except Exception:
            self.listbox.activate(self.index)
            #print self.listbox.get(ACTIVE)
         self.current.set(self.listbox.get(ACTIVE))
         self.listbox.selection_clear(self.index)
         self.frame.after(1,self.printCurrent)
         
                
            

root = Tk()
root.wm_title("BCP Noises-Off")
root.minsize(400,400)
root.maxsize(400,400)
app = App(root)
root.mainloop()
