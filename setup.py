from setuptools import setup

setup (
    name = "cym",
    version = "0.0.1",
    packages=["cym"],
    entry_points={
        'console_scripts': [
            'cym=cym.__main__:main'
        ]
    }
)