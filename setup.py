from setuptools import find_packages, setup

from shutter_ds.version import __version__, licence
from shutter_ds import __doc__, __author__, __author_email__

setup(
    name="tangods-shutter",
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    license=licence,
    description="A simple facade device for shutter",
    long_description=__doc__,
    url="https://github.com/synchrotron-solaris/dev-solaris-shutter.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["setuptools"],
    entry_points={
        "console_scripts": ["Shutter = "
                            "shutter_ds.shutter:run"]}
)
