import wx

def getBitmap(w,h,imagename):
	name=imagename
	backImage=wx.Image(name,wx.BITMAP_TYPE_ANY)
	width=w
	height=h
	backImage2=backImage.Scale(w,h)
	backMap=wx.BitmapFromImage(backImage2)

	return backMap

class myapp(wx.App):
	def __init__(self):
		super(myapp,self).__init__(False)
		self.frame1=mainframe(None,"JAT")
		self.frame1.Show()

class mainframe(wx.Frame):
	def __init__(self,parent,title):
		super(mainframe,self).__init__(parent,title=title,size=(500,400))
		#wx.Frame.__init__(self,parent=parent,title=title,size=(500,400))
		self.minindex=1
		self.index=1
		self.maxindex=3

		#self.setBackground()
		self.nav=wx.Panel(self)
		self.mainPanel=wx.Panel(self)

		self.updateMainPage(self.index)

		self.SetMaxSize((500,400))
		self.SetMinSize((500,400))
		#self.Show()

	def updateMainPage(self,index):
		self.nav.Destroy()
		self.mainPanel.Destroy()
		self.Show(False)
		vbox=wx.BoxSizer(wx.VERTICAL)

		self.nav=navpanel(self)
		if self.index==1:
			self.mainPanel=panel1(self)
		elif self.index==2:
			self.mainPanel=panel2(self)
		elif self.index==3:
			self.mainPanel=panel3(self)

		vbox.Add(self.nav,flag=wx.ALIGN_CENTER)
		vbox.Add(self.mainPanel,flag=wx.ALIGN_CENTER)
		self.nav.gotoBtn.Bind(wx.EVT_BUTTON,self.onClickGoto)
		self.nav.backBtn.Bind(wx.EVT_BUTTON,self.onClickBack)
		self.SetSizer(vbox)

		#self.setBackground()
		#self.SetBackgroundColour("Blue")
		#self.setBackground()
		self.Update()
		self.Show(True)
		if self.index==self.minindex:
			self.nav.backBtn.Hide()
		elif self.index==self.maxindex:
			self.nav.gotoBtn.Hide()

	def onClickGoto(self,event):
		if self.index<self.maxindex:
			self.index=self.index+1
			self.updateMainPage(self.index)

	def onClickBack(self,event):
		if self.index>self.minindex:
			self.index=self.index-1
			self.updateMainPage(self.index)

	def setBackground(self):
		# size = self.GetClientSize()

		# self.buffer = wx.EmptyBitmap(size.width, size.height)
		# dc = wx.BufferedDC(None, self.buffer)
		# dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
		# dc.Clear()

		# size = self.GetClientSize()
		# self.buffer = wx.EmptyBitmap(size.width, size.height)
		# dc=wx.BufferedDC(None,self.buffer)

		backMap=getBitmap(500,400,"cat.png")
		staticMap=wx.StaticBitmap(self,backMap)

		#dc.SetBackground(wx.Brush(self.GetBackgroundColour()).SetStipple(backMap))
		# self.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
		# self.SetBackgroundColour("Red")



class navpanel(wx.Panel):
	def __init__(self,parent):
		super(navpanel,self).__init__(parent)
		self.loadUI()

	def loadUI(self):
		vbox=wx.BoxSizer(wx.VERTICAL)
		vbox.Add((-1,5))
		# self.backBtn=wx.Button(self,label="<<back")
		# self.gotoBtn=wx.Button(self,label="goto>>")
		backbtnImage=getBitmap(60,60,"1.png")
		gotoBtnImage=getBitmap(60,60,"2.jpg")
		logoImage=getBitmap(120,60,"logo.png")
		self.backBtn=wx.BitmapButton(self,bitmap=backbtnImage,size=(60,60))
		self.gotoBtn=wx.BitmapButton(self,bitmap=gotoBtnImage,size=(120,60))
		self.logo=wx.StaticBitmap(self,bitmap=logoImage,size=(60,60))

		hbox1=wx.BoxSizer(wx.HORIZONTAL)
		hbox1.Add(self.backBtn,0,flag=wx.LEFT,border=10)
		hbox1.Add(self.logo,0,flag=wx.LEFT|wx.RIGHT,border=120)
		hbox1.Add(self.gotoBtn,0,flag=wx.RIGHT,border=10)
		vbox.Add(hbox1)
		vbox.Add((-1,5))
		statcLine=wx.StaticLine(self,size=(500,1))
		vbox.Add(statcLine,flag=wx.ALIGN_CENTER)
		vbox.Add((-1,2))
		self.SetSizer(vbox)

#==============================================
class panel1(wx.Panel):
	def __init__(self,parent):
		super(panel1,self).__init__(parent)
		self.loadUI()

	def loadUI(self):
		vbox=wx.BoxSizer(wx.VERTICAL)

		vbox.Add((-1,50))
		namefield=wx.TextCtrl(self)
		namelabel=wx.StaticText(self,label="name:")

		hbox1=wx.BoxSizer(wx.HORIZONTAL)
		hbox1.Add(namelabel,flag=wx.RIGHT,border=5)
		hbox1.Add(namefield,proportion=1)
		vbox.Add(hbox1,flag=wx.ALIGN_CENTER)

		vbox.Add((-1,10))
		passwordlabel=wx.StaticText(self,label="password:")
		passwordfield=wx.TextCtrl(self)

		hbox2=wx.BoxSizer(wx.HORIZONTAL)
		hbox2.Add(passwordlabel,flag=wx.RIGHT,border=5)
		hbox2.Add(passwordfield,proportion=1)
		vbox.Add(hbox2,flag=wx.ALIGN_CENTER)

		vbox.Add((-1,40))
		confirmbtn=wx.Button(self,label="login")
		dismissbtn=wx.Button(self,label="cancle")

		hbox3=wx.BoxSizer(wx.HORIZONTAL)
		hbox3.Add(dismissbtn,flag=wx.RIGHT,border=10)
		hbox3.Add(confirmbtn)
		vbox.Add(hbox3,flag=wx.ALIGN_CENTER)
		vbox.Add((-1,2))

		self.SetSizer(vbox)
		

#----------------------------------------------

class panel2(wx.Panel):
	def __init__(self,parent):
		super(panel2,self).__init__(parent)
		self.loadUI()

	def loadUI(self):
		vbox=wx.BoxSizer(wx.VERTICAL)

		vbox.Add((-1,50))
		# namefield=wx.TextCtrl(self)
		namelabel=wx.StaticText(self,label="Select project:")
		choiceList=["mall_1.84","mall_1.85","mall_1.86","iPhone_2.69","iPhone_2.70"]
		choiceBox=wx.ComboBox(self,value=choiceList[0],choices=choiceList)

		hbox1=wx.BoxSizer(wx.HORIZONTAL)
		hbox1.Add(namelabel,flag=wx.RIGHT|wx.ALIGN_LEFT|wx.EXPAND,border=5)
		hbox1.Add(choiceBox,proportion=1)
		vbox.Add(hbox1,flag=wx.ALIGN_CENTER)
		vbox.Add((-1,10))
		# passwordlabel=wx.StaticText(self,label="Select device:")
		# hbox2=wx.BoxSizer(wx.HORIZONTAL)
		# hbox2.Add(passwordlabel,flag=wx.LEFT,border=20)
		# vbox.Add(hbox2)

		hbox2=wx.BoxSizer(wx.HORIZONTAL)
		self.deviceBox=wx.RadioBox(self,label="Select device:",choices=["simulaor","device"],majorDimension=1)
		self.uidilabel=wx.StaticText(self,label="UDID:")
		self.udidfield=wx.TextCtrl(self,size=(150,20))
		self.udidfield.SetEditable(False)
		self.udidfield.SetValue("NONE")
		hbox2.Add(self.deviceBox,flag=wx.ALIGN_CENTER)
		hbox2.Add(self.uidilabel,flag=wx.RIGHT|wx.LEFT|wx.ALIGN_CENTRE_VERTICAL,border=5)
		hbox2.Add(self.udidfield,flag=wx.ALIGN_CENTRE_VERTICAL)
		vbox.Add(hbox2,flag=wx.ALIGN_BOTTOM)
		self.deviceBox.Bind(wx.EVT_RADIOBOX,self.onChoiceDevice)
		vbox.Add((-1,5))

		
		vbox.Add((-1,30))
		confirmbtn=wx.Button(self,label="begin test")
		dismissbtn=wx.Button(self,label="cancle")
		hbox4=wx.BoxSizer(wx.HORIZONTAL)
		hbox4.Add(dismissbtn,flag=wx.RIGHT,border=10)
		hbox4.Add(confirmbtn)
		vbox.Add(hbox4,flag=wx.ALIGN_CENTER)
		vbox.Add((-1,2))

		self.SetSizer(vbox)
		# self.uidilabel.Hide()
		# self.udidfield.Hide()

	def onChoiceDevice(self,event):
		if self.deviceBox.GetSelection()==0:
			# self.uidilabel.Hide()
			# self.udidfield.Hide()
			self.udidfield.SetEditable(False)
			self.udidfield.SetValue("NONE")
		else:
			# self.uidilabel.Show()
			# self.udidfield.Show()
			self.udidfield.SetEditable(True)
			self.udidfield.SetValue("UDID here")

class panel3(wx.Panel):
	def __init__(self,parent):
		super(panel3,self).__init__(parent)
		self.loadUI()

	def loadUI(self):
		vbox=wx.BoxSizer(wx.VERTICAL)

		vbox.Add((-1,50))
		# namefield=wx.TextCtrl(self)
		namelabel=wx.StaticText(self,label="Select project:")
		choiceList=["mall_1.84","mall_1.85","mall_1.86","iPhone_2.69","iPhone_2.70"]
		choiceBox=wx.ComboBox(self,value=choiceList[0],choices=choiceList)

		hbox1=wx.BoxSizer(wx.HORIZONTAL)
		hbox1.Add(namelabel,flag=wx.RIGHT|wx.ALIGN_LEFT|wx.EXPAND,border=5)
		hbox1.Add(choiceBox,proportion=1)
		vbox.Add(hbox1,flag=wx.ALIGN_CENTER)
		vbox.Add((-1,10))
		# passwordlabel=wx.StaticText(self,label="Select device:")
		# hbox2=wx.BoxSizer(wx.HORIZONTAL)
		# hbox2.Add(passwordlabel,flag=wx.LEFT,border=20)
		# vbox.Add(hbox2)

		hbox2=wx.BoxSizer(wx.HORIZONTAL)
		self.deviceBox=wx.RadioBox(self,label="Select device:",choices=["simulaor","device"],majorDimension=1)
		self.uidilabel=wx.StaticText(self,label="UDID:")
		self.udidfield=wx.TextCtrl(self,size=(150,20))
		self.udidfield.SetEditable(False)
		self.udidfield.SetValue("NONE")
		hbox2.Add(self.deviceBox,flag=wx.ALIGN_CENTER)
		hbox2.Add(self.uidilabel,flag=wx.RIGHT|wx.LEFT|wx.ALIGN_CENTRE_VERTICAL,border=5)
		hbox2.Add(self.udidfield,flag=wx.ALIGN_CENTRE_VERTICAL)
		vbox.Add(hbox2,flag=wx.ALIGN_BOTTOM)
		self.deviceBox.Bind(wx.EVT_RADIOBOX,self.onChoiceDevice)
		vbox.Add((-1,5))

		
		vbox.Add((-1,30))
		confirmbtn=wx.Button(self,label="begin test")
		dismissbtn=wx.Button(self,label="cancle")
		hbox4=wx.BoxSizer(wx.HORIZONTAL)
		hbox4.Add(dismissbtn,flag=wx.RIGHT,border=10)
		hbox4.Add(confirmbtn)
		vbox.Add(hbox4,flag=wx.ALIGN_CENTER)
		vbox.Add((-1,2))

		self.SetSizer(vbox)
		# self.uidilabel.Hide()
		# self.udidfield.Hide()

	def onChoiceDevice(self,event):
		if self.deviceBox.GetSelection()==0:
			# self.uidilabel.Hide()
			# self.udidfield.Hide()
			self.udidfield.SetEditable(False)
			self.udidfield.SetValue("NONE")
		else:
			# self.uidilabel.Show()
			# self.udidfield.Show()
			self.udidfield.SetEditable(True)
			self.udidfield.SetValue("UDID here")

	

if __name__=="__main__":
	app=myapp()
	app.MainLoop()