from setuptools import setup, find_packages


requirements = []

setup(
      name="ndtreepy",
      version = "0.0.8", #@version@#
      description="handle,.in progressing..,APIs",
      author="ihgazni2",
      url="https://github.com/ihgazni2/ndtreepy",
      author_email='', 
      license="MIT",
      long_description = "refer to .md files in https://github.com/ihgazni2/ndtreepy",
      classifiers=[
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Programming Language :: Python',
          ],
      packages= find_packages(),
      entry_points={
          'console_scripts': [
              'ndtreepy=ndtreepy.bin:main'
          ]
      },
      package_data={
          'resources':['RESOURCES/*']
      },
      include_package_data=True,
      install_requires=requirements,
      py_modules=['ndtreepy'], 
)


# python3 setup.py bdist --formats=tar
# python3 setup.py sdist







