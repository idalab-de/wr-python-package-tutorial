# wr-python-package-tutorial

If you are developing your own application, creating your own modules and packages will help you organize and modularize your code, which makes coding, maintenance, and debugging easier.

This tutoiral walks you through how to package a simple Python project. It will show you how to add the necessary files and structure to create the package, how to build the package, and how to upload it to the Python Package Index.

## Setups

First of all, clone this repository to your local host:
```
git clone https://github.com/idalab-de/wr-python-package-tutorial.git 
cd wr-python-package-tutorial
```

You may want to install the following packages which we'll use later:
```
python3 -m pip install --user --upgrade setuptools wheel twine
```

To be able to upload the package into the index, you’ll need to register an account on Test PyPI. To register an account, go to https://test.pypi.org/account/register/ and complete the steps on that page. You will also need to verify your email address before you’re able to upload any packages. 

Once you've registered your account, don't forget to generate a `PyPI API token` so you will be able to securely upload your project. Go to https://test.pypi.org/manage/account/#api-tokens and create a new API token; don’t limit its scope to a particular project, since you are creating a new project.

## Example Package

We've prepared an example package in the `example_pkg` folder. 
The README.md file there describes the basic functionalities about this package. Your challenge now is to distribute this package to the TestPypi index server and verify the result by using pip to install your package. 

To build distribution packages for the package. (These are archives that are uploaded to the Package Index and can be installed by pip):
```
python3 setup.py sdist bdist_wheel
```

To upload your distribution packages:
```
python3 -m twine upload --repository testpypi dist/*
```

And to install your package from TestPyPI:
```
pip install -i https://test.pypi.org/simple/ YOUR_PACKAGE
```

If you've managed the installation, you may also want to try out the following tasks:
* Generate a file consisting some fake web logs (log_generator.py)
* Parse the generated logs and insert them into a local SQLite database (log_db_writer.py)
* Count different visitor browsers ever since 30.Sep.2011


## Literature & Recommended Reading
https://packaging.python.org/tutorials/packaging-projects/




