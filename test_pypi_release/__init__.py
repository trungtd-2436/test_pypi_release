from pkg_resources import DistributionNotFound

__version__ == "0.0.0"
try:
    from test_pypi_release.__version__ import version as __version__
except DistributionNotFound:
    pass
