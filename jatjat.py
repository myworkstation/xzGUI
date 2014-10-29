import wx

class myapp(wx.App):
	def __init__(self):
		super(myapp,self).__init__(False)
		self.frame1=mainframe(None,"JAT")
		self.frame1.Show()

class mainframe(wx.Frame):
	def __init__(self,parent,title):
		super(mainframe,self).__init__(parent,title=title,size=(500,400))
		self.SetMaxSize((500,400))
		self.SetMinSize((300,300))
		#wx.Frame.__init__(self,parent=parent,title=title,size=(500,400))
		self.panel=wx.Panel(self)
		self.minindex=1
		self.maxindex=2
		self.index=1
		self.updateUI()

	def updateUI(self):
		self.panel.Destroy()
		self.panel=self.loadUI(self.index)
		self.Show(False)
		self.Show(True)
		#self.panel.Update()

	def loadUI(self,index):
		panel=wx.Panel(self)
		vbox=wx.BoxSizer(wx.VERTICAL)
		if index==1:
			vbox.Add((-1,10))
			self.backBtn=wx.Button(panel,label="<<Back",size=(70,20))
			self.gotoBtn=wx.Button(panel,label="Goto>>",size=(70,20))
			hbox0=wx.BoxSizer(wx.HORIZONTAL)
			hbox0.Add(self.backBtn,flag=wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT,border=10)
			hbox0.Add(self.gotoBtn,flag=wx.ALIGN_RIGHT)
			self.backBtn.Bind(wx.EVT_BUTTON,self.onClickBack)
			self.gotoBtn.Bind(wx.EVT_BUTTON,self.onClickGoto)
			vbox.Add(hbox0)

			vbox.Add((-1,20))
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
			vbox.Add((-1,2))

		elif index==2:
			vbox.Add((-1,10))
			self.backBtn=wx.Button(panel,label="<<Back",size=(70,20))
			self.gotoBtn=wx.Button(panel,label="Goto>>",size=(70,20))

			hbox0=wx.BoxSizer(wx.HORIZONTAL)
			hbox0.Add(self.backBtn,flag=wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT,border=10)
			hbox0.Add(self.gotoBtn,flag=wx.ALIGN_RIGHT)
			self.backBtn.Bind(wx.EVT_BUTTON,self.onClickBack)
			self.gotoBtn.Bind(wx.EVT_BUTTON,self.onClickGoto)
			vbox.Add(hbox0)

			vbox.Add((-1,20))
			namefield=wx.TextCtrl(panel)
			namelabel=wx.StaticText(panel,label="haha:")

			hbox1=wx.BoxSizer(wx.HORIZONTAL)
			hbox1.Add(namelabel,flag=wx.RIGHT,border=5)
			hbox1.Add(namefield,proportion=1)
			vbox.Add(hbox1,flag=wx.ALIGN_CENTER)

			vbox.Add((-1,10))
			passwordlabel=wx.StaticText(panel,label="pass:")
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
			vbox.Add((-1,2))

		panel.SetSizer(vbox)
		return panel

	def onClickGoto(self,event):
		if self.index<self.maxindex:
			self.index=self.index+1
			self.updateUI()

	def onClickBack(self,event):
		if self.index>self.minindex:
			self.index=self.index-1
			self.updateUI()

if __name__=="__main__":
	app=myapp()
	app.MainLoop()