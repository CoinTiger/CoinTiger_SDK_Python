from setuptools import setup


setup(
    name="cointiger-sdk",
    version="0.1.2",
    description="sdk for cointiger exchange, containd rest api and websocket api",

    url="https://github.com/jianglijie/cointiger-python.git",
    author="jianglijie",
    author_email="jianglj@jianglijie.net",

    packages=["cointiger_sdk", "test"],
    install_requires=[
        "requests",
        "websocket-client",
    ],
    zip_safe=False
)
