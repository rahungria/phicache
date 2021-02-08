import setuptools
import phicache


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


GITHUB_URL = "https://github.com/rahungria/phicache"


setuptools.setup(
    name="phicache",
    packages=['phicache'],
    version=phicache.__version__,
    author="raphi",
    author_email="rhja93@gmail.com",
    description="A cache to store data with metadata and strategies to tailor access",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    download_url=f'{GITHUB_URL}/archive/{phicache.__version__}.tar.gz',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
