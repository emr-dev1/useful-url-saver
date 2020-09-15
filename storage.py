import json
import uuid


class Storage:
	""" Provides the ability to interact with the storage layer. """


	def __init__(self):

		self.saved_urls = json.load(open('./data/saved-urls.json', mode='r'))


	def insert_url(self, useful_url: dict):
		""" Inserts  """

		self.saved_urls[useful_url['url']] = useful_url

		self.persist_current_state()


	def find_url(self, url):
		""" Returns the object for a URL """

		if self.saved_urls[url] != None:

			return self.saved_urls[url]

		return None


	def url_exists(self, url):
		""" Checks if the URL has already been saved. """

		urls = list(self.saved_urls.keys())

		if not url in urls:

			return False

		return True


	def persist_current_state(self):
		""" Writes the python dict object to JSON """

		with open('./data/saved-urls.json', mode='w+') as f:

			f.write(json.dumps(self.saved_urls))

			f.close()


	def get_all_urls(self):
		""" Gets all of the URLs that have been saved """

		return self.saved_urls
