#coding=utf-8

import wx
import time
import datetime

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None,title="计时管理系统")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, 
        size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name="my frame"):
        super(MyFrame,self).__init__(parent, id=id, title=title, pos=pos, size=size, style=style, name=name)
        self.timenow = "0:0:0"
        self.infos = self.get_info()
        self.IsStart = 0
        self.time1 = None
        self.time2 = None

        self.timer = wx.Timer(self)
        self.panel = wx.Panel(self)
        # self.panel.SetBackgroundColour
        self.button_start = wx.Button(self.panel,label="开始计时",pos=(50,50))
        self.button_start.SetBackgroundColour("#DB7093")
        self.start_id = self.button_start.GetId()

        self.button_end = wx.Button(self.panel,label="休息一下",pos=(50,150))
        self.button_end.SetBackgroundColour("#9F5F9F")
        self.end_id = self.button_end.GetId()

        self.timetmp = wx.StaticText(self.panel,wx.ID_ANY,label=self.timenow,
        pos=(190,85),size=(130,40),style=wx.ALIGN_CENTER)
        font=wx.Font(40,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.timetmp.SetFont(font)

        self.nownum = wx.StaticText(self.panel,wx.ID_ANY,label=self.infos,
        pos=(75,250),size=(270,150),style=wx.ALIGN_CENTER)
        font=wx.Font(13,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.nownum.SetFont(font)
        self.nownum.SetLabel(self.infos)
        
        # self.label = wx.
        # self.timetmp.Size()
        self.timetmp.SetBackgroundColour("#00FF00")
        # self.nownum.SetBackgroundColour("#00FFFF")
        
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.Bind(wx.EVT_BUTTON,self.OnButtonS,self.button_start)
        self.Bind(wx.EVT_BUTTON,self.OnButtonE,self.button_end)
    
    def OnButtonS(self,event):
        if not self.IsStart:
            self.IsStart = 1
            self.timer.Start(1000)
            self.time1 = datetime.datetime.now()

        # print("start")
        #print(self.time1)
        pass

    def OnButtonE(self,event):
        #print(time.ctime())
        self.IsStart = 0
        file = open("./time.txt","a+")
        self.timer.Stop()
        line = self.timenow+" "+datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
        # print("---------"+line)
        file.writelines(self.timenow+" "+datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S\n"))
        file.close()
        self.infos = self.get_info()
        self.nownum.SetLabel(self.infos)
        #print(self.time2,self.time1)
        # print("end")
        pass
    
    def OnTimer(self,event):
        # self.timenow = time.ctime()[11:19]
        self.time2 = datetime.datetime.now()
        self.timenow = self.subtime(self.time1,self.time2)
        self.timenow = "{}:{}:{} ".format(int(self.timenow.seconds/(60*60)),int(self.timenow.seconds/(60)),int(self.timenow.seconds%60))
        self.timetmp.SetLabel(self.timenow)
        
        pass

    def get_info(self):
        fileinfos = ""
        file=open('./time.txt','r')
        info = file.readlines()
        count = len(info)
       # print(count)
        for index,line in enumerate(info):
            print(index,line)
            if(index >= count-5):
                print("line"+line)
                fileinfos+=line
        file.close()
        #print(fileinfos)
        return fileinfos

    def subtime(self,date1,date2):
        return (date2-date1)


    

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
