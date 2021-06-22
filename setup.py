from setuptools import setup, find_packages

install_requires = [
    "pyzmq==22.1.0",
    "reindent==3.5.1",
    "PyYAML==5.4.1",
]

setup(
    name="flex-task",
    author="Pablo Buitrago",
    author_email="messaging@energyweb.org",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=install_requires,
    extras_require={
        "all": install_requires
    }
)