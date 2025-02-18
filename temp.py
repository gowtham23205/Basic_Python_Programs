from breezypythongui import EasyFrame
class ButtonDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title = "gui")
        self.addLabel(text = "Input",row =0,column = 0)
        self.addLabel(text = "Output",row = 1,column = 0)
        self.input = self.addTextField(text = "",row = 0,column = 1)
        self.output = self.addTextField(text = "",row = 1,column = 1,state= "readonly")
        self.addButton(text = "compute",row =2,column = 0,columnspan = 2,command = self.upper)
    def upper(self):
        text = self.input.getText()
        self.output.setText(text.upper())
        
def main():
    ButtonDemo().mainloop()
if __name__ == "__main__":
    main()
