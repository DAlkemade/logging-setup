import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="logging_setup_dla",  # Replace with your own username
    version="0.0.1",
    author="Daan Alkemade",
    author_email="dla26@cam.ac.uk",
    description="Standard logging setup for Daan Alkemade",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.7',
    install_requires=requirements
)
