from setuptools import setup

setup(
    name='nyseconverter',
    version='0.1',
    description='NYSE Converter',
    url='https://github.com/LAKSSHMENARAYAN/Nyse-converter',
    author='LAKSSHMENARAYAN',
    author_email='aknuecengineer@gmail.com',
    license='MIT',
    packages=['nyseconverter'],
    zip_safe=False,
    install_requires=[
          'dask[complete]<=2023.3.0',
      ],
     entry_points = {
        'console_scripts': ['nysec=nyseconverter:main'],
    }
)
