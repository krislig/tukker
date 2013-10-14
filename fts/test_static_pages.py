from functional_tests import FunctionalTest, ROOT

class TestHomePage(FunctionalTest):

	def setUp(self):
		self.url= ROOT +'/tukker/'
		get_browser = self.browser.get(self.url)

	def test_can_view_home_page(self):
		response_code = self.get_response_code(self.url)
		self.assertEqual(response_code, 200)

	def test_has_right_title(self):
		title=self.browser.title
		self.assertEqual('Microposts On Steroids', title)

	def test_has_right_heading(self):
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Messages With 300 Chars', body.text)


class TestPrivacyPage(FunctionalTest):
	def setUp(self):
		self.url = ROOT + '/tukker/default/privacy'
		get_browser=self.browser.get(self.url)

	def test_can_view_privacy_page(self):
		response_code = self.get_response_code(self.url)
		self.assertEqual(response_code, 200)

	def test_has_right_title(self):
		title = self.browser.title
		self.assertEqual('Tukker.Me Privacy Policy', title)

	def test_has_right_heading(self):
		heading = self.browser.find_element_by_tag_name('h1')
		self.assertIn('Tukker.Me Privacy Policy', heading.text)

class TestAboutPage(FunctionalTest):
	def setUp(self):
		self.url = ROOT + '/tukker/default/about'
		get_browser=self.browser.get(self.url)

	def test_can_view_about_page(self):
		response_code = self.get_response_code(self.url)
		self.assertEqual(response_code, 200)

	def test_has_right_title(self):
		title = self.browser.title
		self.assertEqual('About Tukker.Me', title)

	def test_has_right_heading(self):
		heading = self.browser.find_element_by_tag_name('h1')
		self.assertIn('About Tukker.Me', heading.text)