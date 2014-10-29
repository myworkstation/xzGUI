#coding:utf-8
#autor:landon connect me by:landonpro@163.com
import urllib
import urllib2
import cookielib
import re
import time
import os
import wx

def getBitmap(w,h,imagename):
	name=imagename
	backImage=wx.Image(name,wx.BITMAP_TYPE_ANY)
	width=w
	height=h
	backImage2=backImage.Scale(w,h)
	backMap=wx.BitmapFromImage(backImage2)

	return backMap

#获取一个保存cookie的对象
cj = cookielib.LWPCookieJar()
#将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
cookie_support = urllib2.HTTPCookieProcessor(cj)
#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
#将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
urllib2.install_opener(opener)

def login(username,password):
	postdata=urllib.urlencode({
	"UserName":username,
    "Password":password,
    "UserType":"stu",
    "btn":"登陆"		
	})

	headers={
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip,deflate",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"202.115.71.131",
    "Origin":"http://202.115.71.131",
    "Referer":"http://202.115.71.131/course/page/widered/index.jsp?c_id=196&c_name=3C0CD8506934059CA20281C5737DA286&c_count=753FA6786E4A2BFF&c_domain=289F67C16B2D311A&c_template=B7564C0FD61B679B",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
	}

	url="http://202.115.71.131/course/servlet/UserLoginDataAction"

	req=urllib2.Request(url,data=postdata)

	for n in headers:
		req.add_header(n,headers[n])
	html=urllib2.urlopen(req).read()
	#print html
	output = re.findall("登录成功，系统2秒后载入...",html)
	if output!=[]:
		return output[0]
	else:
		return "failed!"
#======================================================

def watchvideo(resourceID):
	postdata=urllib.urlencode({
	"resource_id":resourceID
	})

	headers={
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip,deflate,sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Host":"202.115.71.131",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
	}

	url="http://202.115.71.131/course/websys/videoview.jsp?resource_id="+resourceID

	req=urllib2.Request(url,data=postdata)

	for n in headers:
		req.add_header(n,headers[n])
	html=urllib2.urlopen(req).read()
	#return html
	#print html
#=====================================================

def addTime(resourceID):
	now=int(1000*time.time())
	stringnow=str(now)
	postdata=urllib.urlencode({
	"resource_id":resourceID,
    "SetType":"ADD",
    "ranstring":"",
    "sid":"",
    "tt":""
	})

	headers={
	"Accept":"*/*",
    "Accept-Encoding":"gzip,deflate,sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "Host":"202.115.71.131",
    "Referer":"http://202.115.71.131/course/websys/videoview.jsp?resource_id="+resourceID,
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
	}

	url="http://202.115.71.131/course/servlet/UserStudyRecordAction?resource_id="+resourceID+"&SetType=ADD&ranstring=&sid=&tt="+stringnow

	req=urllib2.Request(url,data=postdata)

	for n in headers:
		req.add_header(n,headers[n])
	html=urllib2.urlopen(req).read()
	output = re.findall("(?<=e>)\S+(?=</)",html)
	return output[1].decode('gbk')

#=========================================================

def updateTime(resourceID,sid,ranstring):
	now=int(1000*time.time())
	stringnow=str(now)
	postdata=urllib.urlencode({
	"resource_id":resourceID,
    "SetType":"UPDATE",
    "ranstring":"jywj",
    "sid":sid,
    "tt":stringnow
	})

	headers={
	"Accept":"*/*",
    "Accept-Encoding":"gzip,deflate,sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "Host":"202.115.71.131",
    "Referer":"http://202.115.71.131/course/websys/videoview.jsp?resource_id="+resourceID,
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
	}

	url="http://202.115.71.131/course/servlet/UserStudyRecordAction?resource_id="+resourceID+"&SetType=UPDATE&ranstring="+ranstring+"&sid="+sid+"&tt="+stringnow

	req=urllib2.Request(url,data=postdata)

	for n in headers:
		req.add_header(n,headers[n])
	html=urllib2.urlopen(req).read()
	output = re.findall("(?<=e>)\S+(?=</)",html)
	return output[1].decode('gbk')

#===========================================================
def getRandomPic(resourceID):

	headers={
	"Accept":"image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip,deflate,sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "Host":"202.115.71.131",
    "Referer":"http://202.115.71.131/course/websys/videoview.jsp?resource_id="+resourceID,
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
	}

	url="http://202.115.71.131/course/servlet/GetRandomNumberToJPEG"

	req=urllib2.Request(url)

	for n in headers:
		req.add_header(n,headers[n])
	html=urllib2.urlopen(req).read()

	return html

#=========================================================保存文件操作
def get_file_extension(filename):
	return os.path.splitext(filename)[1]

def save_file(path,filename,data):
	if data ==None:
		return
	if (not os.path.exists(path)):
		print "path does not exists!"
		return
	file=open(path+filename,"wb")
	file.write(data)
	file.flush()
	file.close()


#-------------------------------------------------------
#------------------------图形界面GUI------------------------
class myapp(wx.App):
	def __init__(self):
		super(myapp,self).__init__(False)
		self.frame=mainframe(None,"swjtu xingzheng course video time recoding system")
		self.frame.Show()

class mainframe(wx.Frame):
	def __init__(self,parent,title):
		super(mainframe,self).__init__(parent=parent,title=title,size=(500,350))

		self.loadUI()

	def loadUI(self):
		vbox=wx.BoxSizer(wx.VERTICAL)

		vbox.Add((-1,5))

		logomap=wx.StaticBitmap(self,bitmap=getBitmap(200,69,"swjtu.jpg"),size=(200,69))
		hbox0=wx.BoxSizer(wx.HORIZONTAL)
		hbox0.Add(logomap)
		vbox.Add(hbox0,flag=wx.ALIGN_CENTER)
		vbox.Add((-1,20))

		self.usernamefield=wx.TextCtrl(self)
		self.usernamelabel=wx.StaticText(self,label="username:")
		hbox1=wx.BoxSizer(wx.HORIZONTAL)
		hbox1.Add(self.usernamelabel,flag=wx.RIGHT,border=5)
		hbox1.Add(self.usernamefield)
		vbox.Add(hbox1,flag=wx.ALIGN_CENTER)

		vbox.Add((-1,10))

		self.passwordfield=wx.TextCtrl(self,style=wx.TE_PASSWORD)
		self.passwordlabel=wx.StaticText(self,label="password:")
		hbox2=wx.BoxSizer(wx.HORIZONTAL)
		hbox2.Add(self.passwordlabel,flag=wx.RIGHT,border=5)
		hbox2.Add(self.passwordfield)
		vbox.Add(hbox2,flag=wx.ALIGN_CENTER)

		vbox.Add((-1,15))

		self.confirmbtn=wx.Button(self,label="login")
		hbox3=wx.BoxSizer(wx.HORIZONTAL)
		hbox3.Add(self.confirmbtn)
		vbox.Add(hbox3,flag=wx.ALIGN_CENTER)

		vbox.Add((-1,15))
		self.pic=wx.StaticBitmap(self,bitmap=wx.EmptyBitmap(55,22,-1),size=(55,22))
		self.randpicfield=wx.TextCtrl(self,size=(50,20))
		self.inputstrbtn=wx.Button(self,label="input str")
		self.inputstrbtn.Enable(False)
		hbox4=wx.BoxSizer(wx.HORIZONTAL)
		hbox4.Add(self.pic,flag=wx.RIGHT,border=8)
		hbox4.Add(self.randpicfield)
		hbox4.Add(self.inputstrbtn,flag=wx.LEFT,border=5)
		vbox.Add(hbox4,flag=wx.ALIGN_CENTER)

		vbox.Add((-1,15))

		self.headlabel=wx.StaticText(self,size=(60,22))
		self.infolabel=wx.StaticText(self,size=(120,20))
		self.infolabel.SetLabel("text")
		self.headlabel.SetLabel("log:")
		hbox5=wx.BoxSizer(wx.HORIZONTAL)
		hbox5.Add(self.headlabel,flag=wx.ALIGN_CENTER_VERTICAL)
		hbox5.Add(self.infolabel,flag=wx.ALIGN_CENTER_VERTICAL)
		vbox.Add(hbox5,flag=wx.ALIGN_CENTER)

		vbox.Add((-1,10))

		self.cancelbtn=wx.Button(self,label="cancle")
		hbox6=wx.BoxSizer(wx.HORIZONTAL)
		hbox6.Add(self.cancelbtn)
		vbox.Add(hbox6,flag=wx.ALIGN_CENTER)

		self.SetSizer(vbox)

		self.confirmbtn.Bind(wx.EVT_BUTTON,self.onClickConfirm)
		self.inputstrbtn.Bind(wx.EVT_BUTTON,self.onClickInput)
		self.cancelbtn.Bind(wx.EVT_BUTTON,self.onClickCancel)

	def onClickConfirm(self,event):
		username=self.usernamefield.GetValue()
		password=self.passwordfield.GetValue()
		self.getranpic(username,password)


	def getranpic(self,name,psw):
		self.firstnow=time.time()
		self.now=int(1000*self.firstnow)
		self.stringnow=str(self.now)
		self.looptime=0

		loginhtml=login(name,psw)
		if loginhtml=="登录成功，系统2秒后载入...":
			self.infolabel.SetLabel("login successful!")
			watchvideo(resourceid) #进入收看页面
			self.sid=addTime(resourceid) #开始计时
			pic=getRandomPic(resourceid)
			save_file(savepath,"islogin"+self.stringnow+".png",pic)
			#self.pic.Destroy()
			self.pic.SetBitmap(getBitmap(55,22,savepath+"islogin"+self.stringnow+".png"))
			self.inputstrbtn.Enable(True)
			# self.Hide()
			# self.Show()
			#self.pic=wx.StaticBitmap(self,bitmap=getBitmap(55,22,"islogin"+self.stringnow+".png"),size=(55,22),pos=(122,196))
		else:
			self.infolabel.SetLabel("login failed!")

	def onClickCancel(self,event):
		self.confirmbtn.Enable(True)
		self.randpicfield.Enable(True)
		self.usernamefield.Enable(True)
		self.passwordfield.Enable(True)
		self.inputstrbtn.Enable(False)
		self.usernamefield.SetValue("")
		self.passwordfield.SetValue("")
		self.randpicfield.SetValue("")
		self.pic.SetBitmap(wx.EmptyBitmap(55,22,-1))
		self.infolabel.SetLabel("")

	def onClickInput(self,event):
		randstr=self.randpicfield.GetValue()
		# firststr=updateTime(resourceid,self.sid,randstr)
		# self.infolabel.SetLabel(firststr)
		self.confirmbtn.Enable(False)
		self.randpicfield.Enable(False)
		self.usernamefield.Enable(False)
		self.passwordfield.Enable(False)
		
		if (time.time()-self.firstnow)>360 or self.looptime==0:
			if self.looptime>1:
				self.infolabel.SetLabel("please login again")
				self.confirmbtn.Enable(True)
				self.randpicfield.Enable(True)
				self.usernamefield.Enable(True)
				self.passwordfield.Enable(True)
				self.inputstrbtn.Enable(False)
				self.usernamefield.SetValue("")
				self.passwordfield.SetValue("")
				self.randpicfield.SetValue("")
				self.pic.SetBitmap(wx.EmptyBitmap(55,22,-1))
			else:
				self.looptime=self.looptime+1
				randnumstr=updateTime(resourceid,self.sid,randstr)
				self.firstnow=time.time()
				self.infolabel.SetLabel(str(self.looptime)+": "+randnumstr)
		else:
			self.infolabel.SetLabel("please press later")
		#==========================================================


#================参数===================================
resourceid="CE3E966A68970356"   #视频id
savepath="/Volumes/Macintosh HD 2 1/development/Python/wxpythonapp/"    #验证码保存路径 55 22

if __name__=="__main__":
	app=myapp()
	app.MainLoop()



