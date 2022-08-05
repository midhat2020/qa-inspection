from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in qa_inspection/__init__.py
from qa_inspection import __version__ as version

setup(
	name="qa_inspection",
	version=version,
	description="Quality Inspection",
	author="Precihole",
	author_email="erpadmin@preciholesports.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
