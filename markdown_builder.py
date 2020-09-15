from storage import Storage


def build_markdown_file():
	""" Build the markdown file for the saved urls. """

	storage = Storage()

	useful_urls = storage.get_all_urls()
