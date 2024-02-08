from setuptools import setup

setup(
    name='uni2bn',
    version='0.1',
    py_modules=['uni2bn'],
    author='SAKIBWEB',
    author_email='sakib.sr20@gmail.com',
    description='A Python package to convert Unicode Bangla text to Bangla characters.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sakibweb/uni2bn',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)