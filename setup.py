import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PycordUtils",
    version="0.0.2",
    author="Ghoul",
    description="A Useful Utility Library made to be used with pycord",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xFGhoul/PycordUtils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.6",
    include_package_data=True,
    install_requires=["py-cord"],
    extras_require={"voice": ["py-cord[voice]", "youtube-dl"]}
)