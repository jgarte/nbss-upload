from setuptools import setup

setup(
    name="nb-upload",
    version="0.1",
    url="https://github.com//nbss-upload",
    description="Upload notebooks to a notebooksharing.space instance",
    license="3-clause BSD",
    author="jgart",
    author_email="jgart@dismail.de",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["nbss_upload"],
    entry_points = {
        'console_scripts': ['nbss-upload=nbss_upload:main'],
    },
    install_requires=["requests"],
    platforms="any",
    zip_safe=False,
)
