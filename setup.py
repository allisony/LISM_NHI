import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LISM_NHI",
    version="0.0.1",
    author="Allison Youngblood",
    author_email="allison.a.youngblood@nasa.gov",
    description="N(HI) estimator for stars inside 100 pc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/allisony/LISM_NHI",
    project_urls={
        "Bug Tracker": "https://github.com/allisony/LISM_NHI/issues",
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

