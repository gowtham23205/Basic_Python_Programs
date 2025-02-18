from breezypythongui import EasyFrame
class LabelDemo(EasyFrame):
    def _init_(self):
        EasyFrame._init_(self)
        self.addLabel(text="Hello World!",row=1,column=0)
def main():
    LabelDemo().mainloop()
if __name__=="__main_":
    main()