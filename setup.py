"""
This file configures the Python package with entrypoints used for future runs on Databricks.

Please follow the `entry_points` documentation for more details on how to configure the entrypoint:
* https://setuptools.pypa.io/en/latest/userguide/entry_point.html
"""

from setuptools import find_packages, setup
from dbx_demo_hybrid import __version__

setup(
    name="dbx_demo_hybrid",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    entry_points = {
        "console_scripts": [
            "etl = dbx_demo_hybrid.workloads.sample_etl_job:entrypoint",
            "ml = dbx_demo_hybrid.workloads.sample_ml_job:entrypoint"
    ]},
    version=__version__,
    description="",
    author="",
)
