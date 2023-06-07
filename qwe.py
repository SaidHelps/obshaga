from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.metrics import sp, dp
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.image import Image
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from threading import Thread
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivy.animation import Animation
from requests import get
from time import sleep


Window.size = (450, 700)


class second(Thread):
	def __init__(self, main):
		super().__init__()
		self.main = main
		self.qw = None


	def run(self):
		while True:
			try:
				q = get("http://127.0.0.1:5000").json()
				self.qw = q
				break
			except:
				sleep(1)


class app(MDApp):
	def __init__(self):
		super().__init__()
		self.th = second(main=self)
		self.th.daemon = True
		self.th.start()

	def build(self):
		self.fl = MDFloatLayout()
		
		self.layout = MDGridLayout(cols=1, spacing=dp(130), padding=dp(35))
		self.layout.height = dp(500)
		self.layout.size_hint= (1 ,.2)
		self.layout.bind(minimum_height=self.layout.setter('height'))
		self.root = MDScrollView(size_hint=(1, 1), pos_hint={"center_x":.5,'center_y':.4})
		self.root.size = (Window.width, Window.height)
		self.root.add_widget(self.layout)

		self.fl.add_widget(self.root)

		self.animRestarter()

		return self.fl
	

	def animRestarter(self):
		def low(q):
			if self.th.qw == None:
				print(self.th.qw)
				self.animRestarter()
			else:
				w = False
				for i in self.th.qw:
					card = MDCard(orientation="vertical", spacing=dp(10))
					sl = MDStackLayout(spacing=dp(5))
					sl.padding = 0
					sl.size_hint = (1, None)
					sl.height = dp(90)
					w = False
					for q in i:
						if w == False:
							card.add_widget(MDLabel(text=str(q[0]) + " Этаж", halign="center"))
							w = True
						else: 
							sl.add_widget(MDRaisedButton(text=q, font_size=sp(15)))
					card.add_widget(sl)
					self.layout.add_widget(card)

				
				            
		anim = Animation(
			d=.01
		)
		anim.on_complete=low
		anim.start(self.fl)



app().run()
