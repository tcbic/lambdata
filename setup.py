import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lambdata-tcbic",
    version="0.0.2",
    author="tcbic",
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/tcbic/lambdata",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)