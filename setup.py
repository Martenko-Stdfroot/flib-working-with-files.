from setuptools import setup, find_packages

setup(
    name="flib",
    version="0.2.0",
    author="Stdfroot Martenko", 
    author_email="Martenko-Stdfroot@github.com",
    description="File operations library with logging and security features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
    include_package_data=True,
)