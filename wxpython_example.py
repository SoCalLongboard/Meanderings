import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "wxPython Example", size=(280, 80))
panel = wx.Panel(frame, wx.ID_ANY)
label = wx.StaticText(panel, label="Hello, wxPython!", pos=(80, 30))
frame.Show(True)
app.MainLoop()
