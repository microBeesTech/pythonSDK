import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="microbees",
    version="0.0.1",
    author="microBees Technology Ltd",
    author_email="support@microbees.com",
    description="Offical microBees dev API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microBeesTech/pythonHASS",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
