from functional_tests import FunctionalTest, ROOT

class TestHomePage(FunctionalTest):

	def test_can_view_home_page(self):

		self.browser.get(ROOT + '/tukker/')

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Message with 300 Chars', body.text)