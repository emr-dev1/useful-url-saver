from useful_url_saver import gather_url_info, Storage

# TODO write tests

class TestUsefulUrlSaver:


	def test_gather_url_info(self):
		""" Test the gather_url_info function """

		url_info = gather_url_info('https://dev.to/jessicagarson/resources-for-learning-python-hd6')

		assert url_info['title'] == 'Resources for Learning Python - DEV'

		assert url_info['path'] == '/jessicagarson/resources-for-learning-python-hd6'

		assert url_info['domain'] == 'dev.to'

