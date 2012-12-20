from setuptools import setup, find_packages
import os

version = '0.2.0.dev0'

tests_require=['zope.testing', 'Products.PloneTestCase']

setup(name='collective.periodcriterion',
      version=version,
      description='Additional date criterion for (old-style) Plone collections, '
                  'that add concepts of "today", "this month", "this year"',
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        ],
      keywords='plone plonegov collection criterion',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://plone.org/products/collective.periodcriterion',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone>=4.2',
          'plone.app.querystring',
      ],
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
