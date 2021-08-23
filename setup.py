import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rizapubsub",
    version="0.0.1",
    author="Riza Masykur",
    author_email="hanirizo@gmail.com",
    description="A Pubsub",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rizoadev/rizapubsub",
    project_urls={
        "Bug Tracker": "https://github.com/rizoadev/rizapubsub/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)