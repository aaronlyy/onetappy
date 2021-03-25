from setuptools import setup

with open("README.md", "r") as f:
  _long_description = f.read()


setup(
  name = 'onetappy',
  packages = ['onetappy'],
  version = '0.0.1',
  license='GPL-3.0 License',
  description = 'Wrapper around the onetap.com Cloud API',
  long_description = _long_description,
  long_description_content_type='text/markdown',
  author = 'Aaron Levi Can (aaronlyy)',
  author_email = 'aaronlevican@gmail.com',
  url = 'https://github.com/aaronlyy/onetappy',
  download_url = 'https://github.com/aaronlyy/onetappy/archive/v0.0.1.tar.gz',
  keywords = ['api', 'wrapper', 'json', 'cloud', 'csgo', 'configs'],
  install_requires=[
        "requests"
      ],
)