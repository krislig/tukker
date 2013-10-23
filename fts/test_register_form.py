import os
from os import path

from functional_tests import FunctionalTest, ROOT

class TestRegisterPage(FunctionalTest):

	def setUp(self):
		self.url= ROOT +'/tukker/default/user/register'
		get_browser = self.browser.get(self.url)

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

		# nickname = self.browser.find_element_by_name('nickname')
		# nickname.send_keys("john")

		register_button = self.browser.find_element_by_xpath("//input[@type='submit']")
		register_button.click()

		welcome_message = self.browser.find_element_by_css_selector(".alert")
		self.assertEqual('Welcome to Tukker.Me', welcome_message.text)

		self.url = ROOT + '/tukker/default/user/logout'
		get_browser = self.browser.get(self.url)

	def tearDown(self):
		path_to_database = path.join(path.curdir, "databases")
		db = DAL('sqlite://storage.sqlite', folder=path_to_database)
		db.import_table_definitions(path_to_database)

		db_query = db(db.auth_user.email == 'john@tukker.me').select()

		if len(db_query) > 0:
			db_query[0].delete_record()
			db.commit()



