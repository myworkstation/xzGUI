import wx

class myapp(wx.App):
	def __init__(self):
		super(myapp,self).__init__(False)
		self.frame1=mainframe(None,"JAT")
		#self.frame2=testframe(None,"JAT")
		self.frame1.Show()

class mainframe(wx.Frame):
	def __init__(self,parent,title):
		super(mainframe,self).__init__(parent,title=title,size=(500,400))
		#wx.Frame.__init__(self,parent=parent,title=title,size=(500,400))
		self.mainPage()
		self.SetMaxSize((500,400))
		self.SetMinSize((500,400))
		#self.Show()

	def mainPage(self):
		panel=wx.Panel(self)

		vbox=wx.BoxSizer(wx.VERTICAL)

		vbox.Add((-1,50))
		namefield=wx.TextCtrl(panel)
		namelabel=wx.StaticText(panel,label="name:")

		hbox1=wx.BoxSizer(wx.HORIZONTAL)
		hbox1.Add(namelabel,flag=wx.RIGHT,border=5)
		hbox1.Add(namefield,proportion=1)
		vbox.Add(hbox1,flag=wx.ALIGN_CENTER)

		vbox.Add((-1,10))
		passwordlabel=wx.StaticText(panel,label="password:")
		passwordfield=wx.TextCtrl(panel)

		hbox2=wx.BoxSizer(wx.HORIZONTAL)
		hbox2.Add(passwordlabel,flag=wx.RIGHT,border=5)
		hbox2.Add(passwordfield,proportion=1)
		vbox.Add(hbox2,flag=wx.ALIGN_CENTER)

		vbox.Add((-1,40))
		confirmbtn=wx.Button(panel,label="login")
		dismissbtn=wx.Button(panel,label="cancle")

		hbox3=wx.BoxSizer(wx.HORIZONTAL)
		hbox3.Add(dismissbtn,flag=wx.RIGHT,border=10)
		hbox3.Add(confirmbtn)
		vbox.Add(hbox3,flag=wx.ALIGN_CENTER)

		confirmbtn.Bind(wx.EVT_BUTTON,self.onBtnClick)

		#panel.SetSizer(self.hbox1)
		panel.SetSizer(vbox)

	def onBtnClick(self,event):
		self.Hide()


#--------------------------------------------------------		
class testframe(wx.Frame):
	def __init__(self,parent,title):
		super(testframe,self).__init__(parent,title=title,size=(500,400))
		self.testPage()
		self.SetMinSize((500,400))
		self.SetMaxSize((500,400))
		#self.Show(True)

	def testPage(self):
		panel=wx.Panel(self)

		vbox=wx.BoxSizer(wx.VERTICAL)

		vbox.Add((-1,50))
		namefield=wx.TextCtrl(panel)
		namelabel=wx.StaticText(panel,label="ssss")

		hbox1=wx.BoxSizer(wx.HORIZONTAL)
		hbox1.Add(namelabel,flag=wx.RIGHT,border=5)
		hbox1.Add(namefield,proportion=1)
		vbox.Add(hbox1,flag=wx.ALIGN_CENTER)

		vbox.Add((-1,10))
		passwordlabel=wx.StaticText(panel,label="sssssss")
		passwordfield=wx.TextCtrl(panel)

		hbox2=wx.BoxSizer(wx.HORIZONTAL)
		hbox2.Add(passwordlabel,flag=wx.RIGHT,border=5)
		hbox2.Add(passwordfield,proportion=1)
		vbox.Add(hbox2,flag=wx.ALIGN_CENTER)

		vbox.Add((-1,40))
		confirmbtn=wx.Button(panel,label="login")
		dismissbtn=wx.Button(panel,label="cancle")

		hbox3=wx.BoxSizer(wx.HORIZONTAL)
		hbox3.Add(dismissbtn,flag=wx.RIGHT,border=10)
		hbox3.Add(confirmbtn)
		vbox.Add(hbox3,flag=wx.ALIGN_CENTER)

		confirmbtn.Bind(wx.EVT_BUTTON,self.onBtnClick)

		#panel.SetSizer(self.hbox1)
		panel.SetSizer(vbox)

	def onBtnClick(self,event):
		self.Hide()

		

if __name__=="__main__":
	app=myapp()
	app.MainLoop()