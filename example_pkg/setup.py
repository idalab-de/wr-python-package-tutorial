# setup.py is the build script for setuptools. 
# It tells setuptools about your package (such as the name and version)
# as well as which code files to include.

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    # This is the package distribution name. You should replace with your own 
    # username, this ensures that you have a unique package name and that your 
    # package doesn’t conflict with packages uploaded by other people.
    name="example-pkg-YOUR-USERNAME-HERE",  
    # Package version
    version="0.0.1",
    # Used to identify the author of the package
    author="Example Author",
    author_email="author@example.com",
    # Short, one-sentence summary of the package
    description="A small example package",
    # Detailed description of the package. 
    # This is shown on the package detail package on the Python Package Index. 
    # In this case, the long description is loaded from README.md automatically.
    long_description=long_description,
    # Indicates what type of markup is used for the long description
    long_description_content_type="text/markdown",
    # URL for the homepage of the project, usually link of a repository
    url="https://github.com/pypa/sampleproject",
    # A list of all Python import packages that should be included in the Distribution Package.
    # find_packages() to automatically discover all packages and subpackages.
    packages=setuptools.find_packages(),
    # Required package dependencies to be installed with
    install_requires=[
        "package_name_1", 
        "package_name_2"
    ],
    # Classifier gives the index and pip some additional metadata about your package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)