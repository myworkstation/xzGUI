import wx

app=wx.App(False)
#frame=wx.Frame(None,wx.ID_ANY,"JAT for all")
#frame.Show(True)
class JATFrame(wx.Frame):
	"""docstring for JATFrame"""
	def __init__(self,parent,title):
		#wx.Frame.__init__(self,parent=parent,title=title,size=(500,400))
		super(JATFrame,self).__init__(parent,title=title,size=(500,400))
		self.drawUI()
		self.Show(True)

	def drawUI(self):
		self.btn1=wx.Button(self,label="click1",pos=(20,20),size=(100,20))

		self.checkbox=wx.CheckBox(self,label="choose",pos=(200,20),size=(20,100))

		self.checklist=wx.CheckListBox(self,pos=(200,200),size=(100,100),choices=["1","2","3","4","5","6"])

		self.listbox=wx.ListBox(self,pos=(200,100),size=(100,50),choices=["iiiiiiii","2222222"])

		self.btn1.Bind(wx.EVT_BUTTON,self.onButtonClick)

		self.panel=wx.Panel(self,pos=(300,20),size=(100,100))

		self.panel.SetBackgroundColour(wx.RED)

		self.quote = wx.StaticText(self.panel, label="Your quote: ", pos=(0, 0))

		self.namefield=wx.TextCtrl(self,pos=(20,200),size=(100,40))

		self.choices1=wx.Choice(self,pos=(20,100),size=(100,30),choices=["1","2","3"])

		#self.choicebook=wx.Choicebook(self,wx.ID_ANY,pos=wx.DefaultPosition,size=wx.DefaultSize)

		self.combinebox=wx.ComboBox(self,pos=(20,50),size=(80,30),choices=["11","22","33"])

	def onButtonClick(self,event):
		if self.checkbox.GetValue():
			self.checkbox.SetValue(False)
		else:
			self.checkbox.SetValue(True)


frame=JATFrame(None,"JAT")
app.MainLoop()
