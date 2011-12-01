from setuptools import setup, find_packages

version = '0.1'

setup(name='oc-svenweb',
      version=version,
      description="opencore svenweb client package",
      long_description="""\
""",
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Ethan Jucovy',
      author_email='opencore-dev@lists.coactivate.org',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['opencore'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [topp.zcmlloader]
      opencore = opencore.svenweb
      """,
      )
