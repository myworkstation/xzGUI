import wx
class ExampleFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.RED)
        self.quote = wx.StaticText(self.panel, label="Your quote: ", pos=(20, 30))
        self.Show()

app = wx.App(False)
ExampleFrame(None)
app.MainLoop()