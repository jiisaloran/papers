from distutils.core import setup
import versioneer

setup(name='papers',
      version=versioneer.get_version(),
      cmdclass = versioneer.get_cmdclass(),
      author='Mahe Perrette',
      author_email='mahe.perrette@gmail.com',
      description='utilities to keep your PDF library organized',
      url='https://github.com/jiisaloran/papers',
      maintainer='Jani Saloranta',
      maintainer_email='jiisaloran@gmail.com',
      packages=['papers'],
      scripts=['scripts/papers'],
      license = "MIT",
      requires = ["bibtexparser","crossrefapi","fuzzywuzzy", "unidecode", "scholarly", "six"],
      )

