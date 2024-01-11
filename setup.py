from setuptools import find_packages, setup

setup(
    name='microBeesPy',
    packages=find_packages(),
    version='0.0.1',
    description='microBees Python Library',
    author_email="support@microbees.com",
    author='microbeestech',
    license='MIT',
    install_requires=[],
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["microBeesPy"],                    # Name of the python package
)