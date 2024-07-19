from setuptools import setup, find_packages

setup(
    name="shitty_code_assistant",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI utility to print directory tree and file contents.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    py_modules=["sca"],
    entry_points={
        'console_scripts': [
            'sca=sca:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],  # Add any dependencies if needed
)