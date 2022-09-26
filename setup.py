import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="adilhadizul", # Replace with your username

    version="0.0.1",

    author="Adil Hadi",

    author_email="zulkhairil.a@pg.com",

    description="Clean Extract Visualise",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/adilhadizul/tmux_buffer",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.7',

)