import os
from os import path
from dal import DAL

from functional_tests import FunctionalTest, ROOT

class TestRegisterPage(FunctionalTest):

	def setUp(self):
		self.url= ROOT +'/tukker/default/user/register'
		get_browser = self.browser.get(self.url)

		path_to_database = path.join(path.curdir, "databases")
		self.db = DAL('sqlite://storage.sqlite', folder=path_to_database)
		self.db.import_table_definitions(path_to_database)

		self.db.auth_user.insert(
			first_name = 'Duplicate',
			last_name = 'Nickname',
			email='test@user.com',
			password = 'test',
			nickname = 'duplicate'
		)

		self.db.commit()

	def test_can_view_home_page(self):
		response_code = self.get_response_code(self.url)
		self.assertEqual(response_code, 200)

	def test_has_right_title(self):
		title=self.browser.title
		self.assertEqual('Tukker.Me Registration', title)

	def test_put_values_in_register_form(self):
		first_name = self.browser.find_element_by_name('first_name')
		first_name.send_keys("John")

		last_name = self.browser.find_element_by_name('last_name')
		last_name.send_keys("Tukker")

		email = self.browser.find_element_by_name('email')
		email.send_keys("john@tukker.me")
		
		password = self.browser.find_element_by_name('password')
		password.send_keys("pass")

		verify_password = self.browser.find_element_by_name('password_two')
		verify_password.send_keys("pass")

		nickname = self.browser.find_element_by_name('nickname')
		nickname.send_keys("john")

		image = self.browser.find_element_by_name('image')
		path_to_image = path.abspath(path.join(path.curdir, "fts/test_image.png"))
		image.send_keys(path_to_image)

		register_button = self.browser.find_element_by_xpath("//input[@type='submit']")
		register_button.click()

		welcome_message = self.browser.find_element_by_css_selector(".alert")
		self.assertEqual('Welcome to Tukker.Me', welcome_message.text)

		self.url = ROOT + '/tukker/default/user/logout'
		get_browser = self.browser.get(self.url)

	def test_put_values_in_register_form_with_empty_nickname(self):
		first_name = self.browser.find_element_by_name('first_name')
		first_name.send_keys("John")

		last_name = self.browser.find_element_by_name('last_name')
		last_name.send_keys("Tukker")

		email = self.browser.find_element_by_name('email')
		email.send_keys("john@tukker.me")
		
		password = self.browser.find_element_by_name('password')
		password.send_keys("pass")

		verify_password = self.browser.find_element_by_name('password_two')
		verify_password.send_keys("pass")

		# nickname = self.browser.find_element_by_name('nickname')
		# nickname.send_keys("john")

		image = self.browser.find_element_by_name('image')
		path_to_image = path.abspath(path.join(path.curdir, "fts/test_image.png"))
		image.send_keys(path_to_image)

		register_button = self.browser.find_element_by_xpath("//input[@type='submit']")
		register_button.click()

		error_message = self.browser.find_element_by_id("nickname__error")
		self.assertEqual('enter a value', error_message.text)

	def test_put_values_in_register_form_nickname_with_24_chars(self):
		first_name = self.browser.find_element_by_name('first_name')
		first_name.send_keys("John")

		last_name = self.browser.find_element_by_name('last_name')
		last_name.send_keys("Tukker")

		email = self.browser.find_element_by_name('email')
		email.send_keys("john@tukker.me")
		
		password = self.browser.find_element_by_name('password')
		password.send_keys("pass")

		verify_password = self.browser.find_element_by_name('password_two')
		verify_password.send_keys("pass")

		nickname = self.browser.find_element_by_name('nickname')
		nickname.send_keys("012345678901234567890123")

		image = self.browser.find_element_by_name('image')
		path_to_image = path.abspath(path.join(path.curdir, "fts/test_image.png"))
		image.send_keys(path_to_image)

		register_button = self.browser.find_element_by_xpath("//input[@type='submit']")
		register_button.click()

		error_message = self.browser.find_element_by_id("nickname__error")
		self.assertEqual('enter from 0 to 20 characters', error_message.text)


	def test_put_values_in_register_form_nickname_unique(self):
		first_name = self.browser.find_element_by_name('first_name')
		first_name.send_keys("John")

		last_name = self.browser.find_element_by_name('last_name')
		last_name.send_keys("Tukker")

		email = self.browser.find_element_by_name('email')
		email.send_keys("john@tukker.me")
		
		password = self.browser.find_element_by_name('password')
		password.send_keys("pass")

		verify_password = self.browser.find_element_by_name('password_two')
		verify_password.send_keys("pass")

		nickname = self.browser.find_element_by_name('nickname')
		nickname.send_keys("duplicate")

		image = self.browser.find_element_by_name('image')
		path_to_image = path.abspath(path.join(path.curdir, "fts/test_image.png"))
		image.send_keys(path_to_image)

		register_button = self.browser.find_element_by_xpath("//input[@type='submit']")
		register_button.click()

		error_message = self.browser.find_element_by_id("nickname__error")
		self.assertEqual('value already in database or empty', error_message.text)


	def tearDown(self):
		self.db.auth_user.truncate()
		self.db.commit()

		dirPath = path.join(path.curdir, "uploads")
		fileList = os.listdir(dirPath)

		for fileName in fileList:
			os.remove(dirPath + "/" + fileName)
