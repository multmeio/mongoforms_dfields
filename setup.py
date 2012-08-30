# encoding: utf-8
from setuptools import setup, find_packages

setup(
    name='mongoforms_dfields',
    version='0.',
    description='A ModelForm-DynamicFields',
    author=u'Luís Araújo',
    author_email='luis@multmeio.com.br',
    maintainer=u'Luís Araújo',
    maintainer_email='luis@multmeio.com.br',
    url='https://github.com/multmeio/mongoforms_dfields',
    packages=find_packages(
        exclude=['examples', 'examples.*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    requires=['Django', 
	    'mongoengine(>=0.6)', 
	    'pymongo(>=2.1)', 
	    'django_mongoforms(>=0.3)']
)