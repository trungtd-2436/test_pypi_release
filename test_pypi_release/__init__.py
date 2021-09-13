from pkg_resources import DistributionNotFound

__version__ = None
try:
    from test_pypi_release.__version__ import version as __version__
except DistributionNotFound:
    __version__ == "0.0.0"  # package is not installed
    pass
