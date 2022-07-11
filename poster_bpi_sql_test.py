from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import pymysql.cursors  
from python_anticaptcha import AnticaptchaClient, ImageToTextTask
import requests


def get_html(url):
	r = requests.get(url)
	return r.text




class Bot:
	def __init__(self, row):
		profile = FirefoxProfile("C:\\Users\\Дмитрий\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\kl5gzaww.default-release")
		self.driver = webdriver.Firefox(firefox_profile=profile) 
		self.driver.set_page_load_timeout(10)
		self.data = row
		self.navigate()
		# options = webdriver.ChromeOptions()
		# options.add_argument("user-data-dir=C:\\Users\\Дмитрий\\AppData\\Local\\Google\\Chrome\\User Data")
		# self.driver = webdriver.Chrome(chrome_options=options) 
		# self.driver.set_page_load_timeout(10)
		# self.data = row
		# self.navigate()
	
	def navigate(self):
		
		global timeout
		try:
			ids = self.data['ids'] # id in bpi
			jk = self.data['jk'] # название жилого комплекса
			och = self.data['och'] # очередь
			sec = self.data['sec'] # секция
			deadline = self.data['deadline'] # срок сдачи
			room = self.data['room'] # тип квартиры
			area = self.data['area'] # общая площадь
			floor = self.data['floor'] # этаж
			t_floor = self.data['t_floor'] # этажность
			decor = self.data['decor'] # отделка
			price = self.data['price'] # цена
			dop = self.data['dop'] # дополнительные расходы
			ipoteka = self.data['ipoteka'] # ипотека
			of_price = self.data['of_price'] # цена в договоре
			dogovor = self.data['dogovor'] # тип договора



			self.driver.get('https://realty.yandex.ru/management-new/') #ЗАХОДИМ НА СТРАНИЦУ ЯНДЕКС НЕДВИЖИМОСТИ
			sleep(2)
			self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div[1]/div/div[3]/div/a/span').click() #Новое объявление
			sleep(0.5)
			self.driver.find_element_by_xpath('//*[@id="form-group-type"]/div/span/div[1]/label').click() #Продать
			sleep(0.5)
			self.driver.find_element_by_xpath('//*[@id="category-APARTMENT"]').click() #Квартира
			sleep(1)


			#адрес
			inputJk = self.driver.find_element_by_xpath('//*[@id="search-input"]')
			inputJk.send_keys(jk)
			sleep(0.5)
			inputJk.send_keys(Keys.ENTER)
			sleep(1)
			if room == '1 к':
				#тип квартиры - 1 комнатная
				self.driver.find_element_by_xpath('//*[@id="roomsTotalApartment-1"]').click()
				sleep(0.5)
			elif room == 'Ст.':
				#тип квартиры - студия
				self.driver.find_element_by_xpath('//*[@id="roomsTotalApartment-studio"]').click()
				sleep(0.5)
			elif room == '1Е':
				#тип квартиры - студия
				self.driver.find_element_by_xpath('//*[@id="roomsTotalApartment-studio"]').click()
				sleep(0.5)
			elif room == '2 к':
				#тип квартиры - 2 комнатная
				self.driver.find_element_by_xpath('//*[@id="roomsTotalApartment-2"]').click()
				sleep(0.5)	
			elif room == '2Е':
				#тип квартиры - 2 комнатная
				self.driver.find_element_by_xpath('//*[@id="roomsTotalApartment-2"]').click()
				sleep(0.5)
			elif room == '3 к':
				#тип квартиры - 3 комнатная
				self.driver.find_element_by_xpath('//*[@id="roomsTotalApartment-3"]').click()
				sleep(0.5)				
			elif room == '3Е':
				#тип квартиры - 3 комнатная
				self.driver.find_element_by_xpath('//*[@id="roomsTotalApartment-3"]').click()
				sleep(0.5)
			elif room == '4 к':
				#тип квартиры - 4 комнатная
				self.driver.find_element_by_xpath('//*[@id="roomsTotalApartment-4"]').click()
				sleep(0.5)
			elif room == '4Е':
				#тип квартиры - 4 комнатная
				self.driver.find_element_by_xpath('//*[@id="roomsTotalApartment-4"]').click()
				sleep(0.5)
			elif room == '5 к':
				#тип квартиры - 5 комнатная
				self.driver.find_element_by_xpath('//*[@id="roomsTotalApartment-5"]').click()
				sleep(0.5)	

			# общая площадь
			inputArea = self.driver.find_element_by_xpath('//*[@id="input-area"]')
			inputArea.send_keys(area)
			#этаж
			inputFloor = self.driver.find_element_by_xpath('//*[@id="input-floor"]')
			inputFloor.send_keys(floor)
			#этажность
			inputTotalf = self.driver.find_element_by_xpath('//*[@id="input-floorsTotal"]')
			inputTotalf.clear()
			# inputTotalf.send_keys('\b\b\b')
			inputTotalf.send_keys(t_floor)
			#ремонт
			if decor == 'без отделки':
				self.driver.find_element_by_xpath('//*[@id="renovation-NEEDS_RENOVATION"]').click()
			elif decor == 'предчистовая':
				self.driver.find_element_by_xpath('//*[@id="renovation-NEEDS_RENOVATION"]').click()
			else:
				self.driver.find_element_by_xpath('//*[@id="renovation-EURO"]').click()				
			
			#загрузка фото
			list = os.listdir('c:\\Python37\\BPI\\'+str(ids)) 
			number_files = len(list)
			photo = "C:\\Python37\\BPI\\"+str(ids)+"\\"+str(1)+".jpg"
			# print(photo)
			# self.driver.find_element_by_xpath('//*[@id="form-group-photo"]/div/div/div[4]/div/input').send_keys("C:\\Python37\\"+str(t)+"\\"+str(1)+".jpg")
			for i in range(number_files-1):
				photo = photo + "\n"+ "C:\\Python37\\BPI\\"+str(ids)+"\\"+str(i+2)+".jpg"
			# print(photo)
			try:
				self.driver.find_element_by_xpath('//*[@id="form-group-photo"]/div/div/div[4]/div/input').send_keys(photo)
				sleep(1)
			except:
				try:
					self.driver.find_element_by_xpath('//*[@id="form-group-photo"]/div/div/div[4]/div/input').send_keys(photo)
					sleep(1)
				except:
					print('Фото не загрузились')




			if room == '1 к':
				d_room = 'однокомнатная квартира. '

			elif room == 'Ст.':
				d_room = 'квартира-студия. '

			elif room == '1Е':
				d_room = 'еврооднушка. '

			elif room == '2 к':
				d_room = 'двухкомнатная квартира. '
		
			elif room == '2Е':
				d_room = 'евродвушка. '

			elif room == '3 к':
				d_room = 'трехкомнатная квартира. '

			elif room == '3Е':
				d_room = 'евротрешка квартира. '

			elif room == '4 к':
				d_room = 'четырехкомнатная квартира. '

			elif room == '4Е':
				d_room = 'трехкомнатная квартира с большой кухней-гостиной. '

			elif room == '5 к':
				d_room = 'пятикомнатная квартира. '
			
			if deadline == 'Госкомиссия':
				d_deadline = 'Дом полностью достроен. В настоящее время на госкомиссии. '
			elif deadline == 'Дом сдан':
				d_deadline = 'Дом сдан. '
			elif deadline == 'Заселен':
				d_deadline = 'Дом сдан и заселен. Можно въезжать. '
			elif deadline == 'Собственность':
				d_deadline = 'Дом сдан и заселен. Получена собственность. '
			else:
				d_deadline = 'Срок сдачи дома - ' + deadline + '. '

			if decor == 'без отделки':
				d_decor = 'Без отделки. '
			elif decor == 'предчистовая':
				d_decor = 'В квартире будет выполнена подготовка под чистовую отделку. '
			else:
				d_decor = 'Квартира с полной чистовой отделкой от застройщика. '

			if ipoteka == 'Да':
				d_ipoteka = 'Возможно оформление ипотеки. '
			else:
				d_ipoteka = ''

			if dogovor == 'Уступка с ДДУ':
				d_dogovor = 'Квартира продается по договору переуступки ДДУ.'
			elif dogovor == 'Уступка с ЖСК':
				d_dogovor = 'Квартира продается по договору переуступки ЖСК.'
			elif dogovor == 'КП':
				d_dogovor = 'Квартира продается по договору купли-продажи.'				

			#описание
			description = 'Id объекта - ' + str(ids) + '. Вашему вниманию предлагается ' + d_room + 'Объект расположен в ЖК ' + jk + '. ' + 'Очередь '+ och + '. ' + d_deadline + d_decor + d_ipoteka + d_dogovor
			inputDiskrip = self.driver.find_element_by_xpath('//*[@id="form-group-comfort"]/div/div/div/textarea[2]')
			inputDiskrip.clear()
			inputDiskrip.send_keys(description)
			#цена
			inputPrice = self.driver.find_element_by_xpath('//*[@id="input-price"]')
			inputPrice.clear()
			inputPrice.send_keys(price)
			#переуступка
			self.driver.find_element_by_xpath('//*[@id="dealType-REASSIGNMENT"]').click()
			#ипотека
			if ipoteka == 'Да':
				self.driver.find_element_by_xpath('//*[@id="additional-MORTGAGE"]').click()
			#торг
			self.driver.find_element_by_xpath('//*[@id="additional-HAGGLE"]').click()






			inputSave = self.driver.find_element_by_xpath('//*[@id="form-group-publish"]/div/div/div/div/div/h2/div/ul/li[2]/div').click()
			sleep(0.5)
			inputSave = self.driver.find_element_by_xpath('//*[@id="form-group-publish"]/div/div/div/div/div/div[1]/div[1]').click()
			sleep(0.5)
			inputSave = self.driver.find_element_by_xpath('//*[@id="form-group-publish"]/div/div/div/div/div/button/span').click()
			sleep(3)
			f = open('c:\\Python37\\time.txt', 'w')
			f.write('0')
			f.close()
			print ('Объявление номер - '+ str(ids) + ' загружено')
			self.driver.quit()

		except:
			# f = open('c:\\Python37\\time.txt', 'w')
			# f.write('1')
			# f.close()
			self.driver.quit()
			print('Что-то пошло не так')



def main():
	
	# connection = pymysql.connect(host='localhost',
	# 						user='root',
	# 						password='********',
	# 						db='bpi',
	# 						charset='utf8mb4',
	# 						cursorclass=pymysql.cursors.DictCursor)

	connection = pymysql.connect(host='mysql.9967724406.myjino.ru',
							user='047077889_lds',
							password='********',
							db='9967724406_bpi',
							charset='utf8mb4',
							cursorclass=pymysql.cursors.DictCursor)


	print ("connect successful!!")		
	
	with connection.cursor() as cursor:
		sql = "SELECT * FROM flats"
		cursor.execute(sql)
		c = cursor.fetchall()
	
	for i in range(len(c)):
		timeout = 1
		while timeout==1:
			b = Bot(c[i])
			f = open('c:\\Python37\\time.txt')
			for line in f:
				timeout=int(line)



	# for row in c:
	# 	try:
	# 		b = Bot(row)
	# 	except TimeoutException:
	# 		print('Что-то пошло не так')
	# 		self.driver.quit()
		# except:
			# print('Это объявление не удалось опубликовать')


main()