import click
import requests
import bs4
from datetime import datetime
from urllib.parse import urlparse
from pathlib import Path
from storage import Storage


def gather_url_info(url: str) -> dict:
	""" Makes an HTTP GET request to gather information about the URL """

	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
		'Referrer': 'https://google.com',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.9',
		'Pragma': 'no-cache'
	}

	req = requests.get(url)

	soup = bs4.BeautifulSoup(req.text, 'html.parser')

	title = soup.find('title').get_text()

	parsed_url = urlparse(url)

	return {
		'title': title,
		'path': parsed_url[2],
		'domain': parsed_url[1]
	}


def handle_add_url(url):
	""" Handles the adding of a new URL """

	storage = Storage()

	if not storage.url_exists(url):

		useful_url = gather_url_info(url)

		useful_url['url'] = url

		useful_url['created'] = str(datetime.now())

		storage.insert_url(useful_url)

	else:

		click.echo('\nURL already exists')


def handle_file_generation(file_type='*'):

	pass


@click.command()
@click.option(
	'-a', '--add-url', 'add_url',
	help='The URL that is wanted to be added to your saved list of URLs.',
	type=str
)
@click.option(
	'-g', '--generate', 'generate',
	help='Generates the .md and .html files. Use "all" to generate both.',
	type=str
)
def main(add_url, generate):
	"""
	A tool that allows you to quickly and easily save the URLs to resources that you find
	useful from the terminal. To quickly and easily add a new useful URL just call the
	`useful-url` app then paste in the URL you want to save.
	"""

	if add_url:

		click.echo('Saving URL: {}'.format(add_url))
		click.echo('Please wait...')

		handle_add_url(add_url)


	if generate:

		click.echo('Formatting {}'.format(generate))

		# TODO handle the generations of both file types


if __name__ == '__main__':

	main()
