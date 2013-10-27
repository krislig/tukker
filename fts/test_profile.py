import os
from os import path

from functional_tests import FunctionalTest, ROOT
from dal import DAL

class TestProfile(FunctionalTest):

	def setUp(self):
		path_to_database = path.join(path.curdir, "databases")
		self.db = DAL('sqlite://storage.sqlite', folder=path_to_database)
		self.db.import_table_definitions(path_to_database)

		self.create_user()
		self.login()

		self.url = ROOT + '/tukker/default/profile/john'
		get_browser=self.browser.get(self.url)

	def test_can_view_profile(self):
		response_code = self.get_response_code(self.url)
		self.assertEqual(response_code, 200)

	def test_has_right_title(self):
		title=self.browser.title
		self.assertEqual("john's Profile", title)

	def test_has_page_the_needed_elements(self):
		# name = self.browser.find_element_by_id('profile-name')
		# self.assertEqual(name.text, "john")

		nickname = self.browser.find_element_by_id('nickname')
		self.assertEqual(nickname.text, "john")

		# image = self.browser.find_element_by_id('profile-image')
		# self.assertEqual("auth_user.image", image.get_attribute("src"))

	def tearDown(self):
		self.url = ROOT + '/tukker/default/user/logout'
		get_browser=self.browser.get(self.url)

		self.db.auth_user.truncate()
		self.db.commit()

		dirPath = path.join(path.curdir, "uploads")
		fileList = os.listdir(dirPath)

		for fileName in fileList:
			os.remove(dirPath + "/" + fileName)

	def create_user(self):
		self.url = ROOT + '/tukker/default/user/register'
		get_browser = self.browser.get(self.url)

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

		self.url = ROOT + '/tukker/default/user/logout'
		get_browser = self.browser.get(self.url)

	def login(self):
		self.url = ROOT + '/tukker/default/user/logout'
		get_browser = self.browser.get(self.url)

		self.url = ROOT + '/tukker/default/user/login'
		get_browser=self.browser.get(self.url)

		user_email = self.browser.find_element_by_id("auth_user_email")
		user_email.send_keys("john@tukker.me")

		user_password = self.browser.find_element_by_id("auth_user_password")
		user_password.send_keys("pass")

		submit_button = self.browser.find_element_by_xpath("//input[@type='submit']")
		submit_button.click()
