# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import urllib
from urllib import parse

###########################################################################
## Class WindowsBox
###########################################################################

class WindowsBox ( wx.Frame ):
	char_urlcode = {'A':'%41','B':'%42','C':'%43','D':'%44','E':'%45','F':'%46','G':'%47','H':'%48','I':'%49','J':'%4a','K':'%4b','L':'%4c','M':'%4d','N':'%4e','O':'%4f','P':'%50','Q':'%51','R':'%52','S':'%53','T':'%54','U':'%55','V':'%56','W':'%57','X':'%58','Y':'%59','a':'%61','b':'%62','c':'%63','d':'%64','e':'%65','f':'%66','g':'%67','h':'%68','i':'%69','j':'%6a','k':'%6b','l':'%6c','m':'%6d','n':'%6e','o':'%6f','p':'%70','q':'%71','r':'%72','s':'%73','t':'%74','u':'%75','v':'%76','w':'%77','x':'%78','y':'%79'}
	number_urlcode = {'1':'%31','2':'%32','3':'%33','4':'%34','5':'%35','6':'%36','7':'%37','8':'%38','9':'%39'}
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"URL编解码小程序", pos = wx.DefaultPosition, size = wx.Size( 499,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"输入", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.input_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.input_box, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"输出", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.output_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.output_box, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.char_code = wx.CheckBox( self, wx.ID_ANY, u"字母编码", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.char_code, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.number_code = wx.CheckBox( self, wx.ID_ANY, u"数字编码", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.number_code, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.encode = wx.Button( self, wx.ID_ANY, u"编码", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.encode, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.uncode = wx.Button( self, wx.ID_ANY, u"解码", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.uncode, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.encode.Bind( wx.EVT_BUTTON, self.encode_click )
		self.uncode.Bind( wx.EVT_BUTTON, self.uncode_click )
	
	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def encode_click( self, event ):
		encode_str = self.input_box.GetValue()
		temp_for_encode_str = []	#临时编码专用变量
		temp_for_encode_str_counter = 0 #临时编码定位专用变量
		for i in encode_str:
			temp_for_encode_str.append(i)	#将字符串列表化
		for i in temp_for_encode_str:
			temp_for_encode_str[temp_for_encode_str_counter] = parse.quote(i)
			for j in self.char_urlcode:
				if i == j:
					if self.char_code.GetValue() == True:
						temp_for_encode_str[temp_for_encode_str_counter] = self.char_urlcode[j]       
			for j in self.number_urlcode:
				if i == j:
					if self.number_code.GetValue() == True:
						temp_for_encode_str[temp_for_encode_str_counter] = self.number_urlcode[j]
			temp_for_encode_str_counter += 1
		encode_str = ''
		for i in temp_for_encode_str:
			encode_str += str(i)
		self.output_box.SetValue(encode_str)
		
	def uncode_click( self, event ):
		uncode_str = parse.unquote(self.input_box.GetValue())
		self.output_box.SetValue(uncode_str)
#running	
app =wx.App()
fram = WindowsBox(None)
fram.Show(True)
app.MainLoop()