import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='glaring_simulation',
    packages=find_packages(include=['glaring_simulation']),
    version='0.1.0',
    description='Augmentation methods: glaring
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/thomle295/glaring_simulation",
    author='ThomLe',
    author_email="thomlestudy295@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    license='MIT',
    install_requires=[
        'numpy',
        'opencv-python'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)
