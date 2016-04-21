from setuptools import setup


def read_text(filename):
	with open(filename) as f:
		return f.read()


setup(
	name='predictivepunter',
	version='0.0.0',
	description='Applying predictive analytics to horse racing via Python',
	long_description=read_text('README.rst'),
	classifiers=[
		'Development Status :: 1 - Planning',
		'Environment :: Console',
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.4',
		'Topic :: Scientific/Engineering :: Information Analysis'
	],
	keywords='predictive analytics horse racing',
	url='https://github.com/JayTeeGeezy/predictivepunter',
	author='Jason Green',
	author_email='JayTeeGeezy@outlook.com',
	license='MIT',
	packages=[
		'predictivepunter'
	],
	scripts=[
	],
	entry_points={
		'console_scripts': [
			'scrape=predictivepunter.scrape:main'
		]
	},
	install_requires=[
		'cache_requests',
		'lxml',
		'pymongo',
		'pypunters',
		'pyracing'
	],
	test_suite='nose.collector',
	tests_require=[
		'cache_requests',
		'lxml',
		'nose',
		'pymongo',
		'pypunters',
		'pyracing'
	],
	dependency_links=[
		'https://github.com/JayTeeGeezy/pypunters/tarball/develop#egg=pypunters-0.0.0',
		'https://github.com/JayTeeGeezy/pyracing/tarball/develop#egg=pyracing-0.0.0'
	],
	include_package_data=True,
	zip_safe=False
	)