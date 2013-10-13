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
		self.assertIn('Message with 300 Chars', body.text)