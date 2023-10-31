#!/usr/bin/env python
import setuptools

requirements = ["apache-airflow", "requests"]

setuptools.setup(
    name="airflow-movielens",
    version="0.1.1",
    description="Hooks, Sensors and operators for fetching data from the movielens API",
    author="Anonymous",
    author_email="anonymous@example.com",
    install_requires=requirements,
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/example-repo/airflow_movielens",
    license="MIT license",
)
