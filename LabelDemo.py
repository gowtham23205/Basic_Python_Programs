from breezypythongui import EasyFrame
class LabelDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text="Hello World!",row=20,column=4)
def main():
    LabelDemo().mainloop()
if __name__=="__main__":
    main()