from setuptools import setup, find_namespace_packages
import pathlib
import sys

home_page = "https://github.com/trungtd-2436/test_pypi_release"
assert sys.version_info >= (3, 6, 2), "test_pypi_release requires Python 3.6.2+"

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="test_pypi_release",
    use_scm_version={
        "write_to": "test_pypi_release/__version__.py",
        "version_scheme": "guess-next-dev",
        "local_scheme": "node-and-date"
    },
    author="Tran Duc Trung B",
    author_email="tran.duc.trung-b@gmail.com",
    setup_requires=["setuptools_scm"],
    description="A test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=home_page,
    project_urls={
        "Bug Tracker": "{}/issues".format(home_page),
    },
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=requirements,
    package_dir={"": "."},
    packages=find_namespace_packages(include=["test_pypi_release", "MANIFEST.in"]),
)
