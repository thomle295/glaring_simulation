from setuptools import find_packages, setup


setup(
    name='glaring_simulation',
    packages=find_packages(include=['glaring_simulation']),
    version='0.1.0',
    description='Augmentation methods: glaring',
    author='ThomLe',
    license='MIT',
    install_requires=[
        'numpy',
        'opencv-python'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)
