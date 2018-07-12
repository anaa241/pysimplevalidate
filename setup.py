from setuptools import setup


setup(
    name='PySimpleValidate',
    version=__import__('pyautogui').__version__,
    url='https://github.com/asweigart/pysimplevalidate',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=('A collection of string-based validation functions, suitable for use in other Python 2 and 3 applications.'),
    license='BSD',
    packages=['pysimplevalidate'],
    test_suite='tests',
    install_requires=[],
    keywords="input validation text string",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
        'Programming Language :: Python :: 3.5'
        'Programming Language :: Python :: 3.6'
        'Programming Language :: Python :: 3.7'
    ],
)