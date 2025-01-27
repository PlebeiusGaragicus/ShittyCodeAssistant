from setuptools import setup, find_packages

setup(
    name="shitty_code_assistant",
    version="0.1.0",
    author="PlebbyG",
    author_email="plebeiusgaragicus@gmail.com",
    description="Quickly copy relevant code snippets for in-context learning",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",

    packages=find_packages(),

    # py_modules=["sca"],j

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

    # Add any dependencies if needed
    install_requires=[
        'pyperclip'
    ],
)
