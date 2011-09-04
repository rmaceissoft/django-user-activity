from setuptools import setup, find_packages

setup(
    name = "django-user-activity",
    version='0.1',
    author = "Reiner Marquez Alvarez",
    author_email = "rmaceissoft@gmail.com",
    description = "A simple app for register user's activities using signals and generate reports with them",
    license = "GPL",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests', 'docs']),
    classifiers = [
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)