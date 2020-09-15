from setuptools import setup, find_packages

setup(
	name='useful-url',
	version='0.1',
	py_modules=find_packages(),
	install_requires=[
		'Click',
		'beautifulsoup4',
		'requests',
	],
	entry_points='''
		[console_scripts]
		useful-url=useful_url_saver:main
	'''
)
