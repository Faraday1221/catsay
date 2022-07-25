from setuptools import setup

setup(
    name="catsay",
    version="0.0.0",
    entry_points={
        "console_scripts": ["catsay=catsay.__main__:cli"],
    },
    python_requires=">=3.6",
    package_dir={"": "src"},
    packages=["catsay"],
    package_data={"catsay": ["img/*.txt"]},
)
