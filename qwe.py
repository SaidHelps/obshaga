from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from typing import Any
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
				#self.qw  = q['102']
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
		
		self.layout = MDGridLayout(cols=1, spacing=100, size_hint_y=None, padding=100)
		self.layout.height = 100
# Make sure the height is such that there is something to scroll.
		self.layout.bind(minimum_height=self.layout.setter('height'))
		self.root = MDScrollView(size_hint=(1, None), pos_hint={"center_x":.5,'center_y':.5})
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
				for i in range(10):
					card = MDCard()
					rl = MDRelativeLayout()
					sl = MDStackLayout()
					sl.padding = 40
					sl.size_hint = (1, None)
					sl.height = 90
					#sl.spacing = 60
					for i, q in self.th.qw.items():
						sl.add_widget(MDRaisedButton(text=f"{i} комната, для {q} курса"))
					#rl.add_widget(sl)
					card.add_widget(sl)

					self.layout.add_widget(card)
		anim = Animation(
			d=.01
		)
		anim.on_complete=low
		anim.start(self.fl)
	


app().run()
