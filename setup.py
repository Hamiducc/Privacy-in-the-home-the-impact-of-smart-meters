from setuptools import setup

setup(name='pyHS110',
      version='0.3.4',
      description='Interface for TPLink HS1xx plugs, HS2xx wall switches & LB1xx bulbs',
      url='https://github.com/GadgetReactor/pyHS110',
      author='Sean Seah (GadgetReactor)',
      author_email='sean@gadgetreactor.com',
      license='GPLv3',
      packages=['pyHS110'],
      install_requires=['click', 'click-datetime', 'typing'],
      python_requires='>=3.4',
      entry_points={
            'console_scripts': [
                  'pyhs100=pyHS110.cli:cli',
            ],
      },
      zip_safe=False)
