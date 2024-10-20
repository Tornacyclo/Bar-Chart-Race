import setuptools
import re

with open('bar_chart_race/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split("'")[1]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BCR",
    version=version,
    author="Peace Hegemony",
    author_email="",
    description="Create animated bar chart races using Matplotlib or Plotly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="visualization animation bar chart race matplotlib pandas plotly",
    url="https://github.com/Tornacyclo/bar_chart_race.git",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas>=0.24", "matplotlib>=3.1"],
    python_requires='>=3.6',
    include_package_data=True,
)
