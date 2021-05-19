from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='linkedin_scraping',
      version="0.7.2",
      description='Selenium Scraper for Linkedin Profiles',
      long_description=readme(),
      author="KrishACS",
      author_email='acssathya333@gmail.com',
      license='MIT',
      url='https://github.com/KrishACS/scrape-linkedin-selenium',
      packages=['linkedin_scraping'],
      entry_points={'console_scripts': [
          'scrapeli=linkedin_scraping.cli:scrape']},
      keywords='linkedin selenium scraper web scraping',
      #   include_package_data=True,
      #   package_data={'scraper': ['data/*.txt']},
      zip_safe=False,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'
      ],
      install_requires=[
          'beautifulsoup4>=4.6.0',
          'bs4',
          'selenium',
          'click',
          'joblib'
      ]
      )
