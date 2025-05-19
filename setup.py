from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt") as req:
    requirements = req.read().splitlines()

setup(
    name="tamilmv-bot",
    version="0.1.0",  # Tag থেকে v বাদ দিন
    description="Telegram bot for downloading from Tamilmv",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="MY-HERO-OP",
    author_email="heron3477@gmail.com",
    url="https://github.com/MY-HERO-OP/1tamilmv_v2_Bot",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
