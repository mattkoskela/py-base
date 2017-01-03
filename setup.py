from setuptools import setup

setup(
    name="pybase",
    version="2.0.0",
    author="Matt Koskela",
    author_email="mattkoskela@gmail.com",
    packages=["namespace", "namespace.pybase"],
    namespace_packages = ["namespace"],
    scripts=[
        "bin/sample_script"
    ],
    url="http://example.com/",
    license="LICENSE",
    description="A quick starting point for namespaced python packages",
    long_description=open("README.md").read(),
    install_requires=[
        "PyMySQL==0.7.9",
    ]
)
