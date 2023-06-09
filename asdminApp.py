from kivy.uix.popup import Popup
from kivymd.uix.card import MDCard
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp, sp
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image


class app(MDApp):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.sm = MDScreenManager()
		self.sc1 = MDScreen(name = "main")
		self.sc2 = MDScreen(name = "second")
		self.sm.add_widget(self.sc1)
		self.sm.add_widget(self.sc2)


	def build(self):
			self.fl1 = MDFloatLayout()

			self.gl1 = MDGridLayout(rows = 2, cols = 2)
			self.gl1.size_hint = (.5, .5)
			self.gl1.pos_hint={'center_x':.5,'center_y':.5}
			self.gl1.spacing = dp(10)

			self.gl1.add_widget(MDRaisedButton(text="Просмотр", size_hint=(.2, .2)))
			self.gl1.add_widget(MDRaisedButton(text="Редактирование", size_hint=(.2, .2), on_release=lambda x:self.changeWin(win="second")))

			self.fl1.add_widget(self.gl1)

			self.fl2 = MDFloatLayout()
			
			self.layout2 = MDGridLayout(cols=1, spacing=dp(110), size_hint_y=None, padding=dp(25))
			self.layout2.bind(minimum_height=self.layout2.setter('height'))

			for i in range(4):
				card = MDCard(orientation="vertical", height=Window.height/3,  spacing=dp(15))
				card.add_widget(MDLabel(text=f"Hello world, {i}", size_hint_x=1, halign="center"))
				sl = MDStackLayout(spacing=dp(5))
				sl.height = 90
				card.add_widget(sl)
				for i in range(14):
					sl.add_widget(MDRaisedButton(text=str(i), font_size=dp(30)))
				self.layout2.add_widget(card)
				self.layout2.spacing = card.height
			self.root = MDScrollView(size_hint=(.6, .7), pos_hint={'center_x':.7,'center_y':.5})
			self.root.add_widget(self.layout2)

			self.fl2.add_widget(MDRaisedButton(text="Добавить Комнату", size_hint=(.3, .1), pos_hint={'center_x':.2, 'center_y':.55}, on_release=lambda x:self.popupActivate(type="room")))
			self.fl2.add_widget(MDRaisedButton(text="Добавить Этаж", size_hint=(.3, .1), pos_hint={'center_x':.2, 'center_y':.7}, on_release=lambda x:self.popupActivate(type="layer")))

			self.fl2.add_widget(self.root)

			self.sc1.add_widget(self.fl1)
			self.sc2.add_widget(self.fl2)

			return self.sm


	def popupActivate(self, type):
		popupRoom = Popup(title='Создать комнату',
    content=MDLabel(text='Комната далбаебава'),
    size_hint=(None, None), size=(400, 400))
		popupRoom.open()


	def changeWin(self, win):
		self.sm.current = win	


app().run()

