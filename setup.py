from setuptools import setup, find_packages
setup(
    name="kubectl-lsdeploy",
    version="1.1",
    packages=find_packages(),
    scripts=['kubectl-lsdeploy.py'],

    install_requires=['kubernetes','prettytable','pyyaml','argparse'],

    package_data={
        # If any package contains *.txt or *.md files, include them:
        '': ['*.txt', '*.md'],
    },

    # metadata to display on PyPI
    author="Dominik Zorgnotti",
    author_email="dominik@why-did-it.fail",
    description="A plugin for kubectl that lists of deployments and namespaces",
    keywords="kubernetes plugin kubectl",
    url="https://github.com/dominikzorgnotti/kubectl-lsdeploy",   # project home page
    project_urls={
        "Bug Tracker": "https://github.com/dominikzorgnotti/kubectl-lsdeploy/issues",
        "Documentation": "https://github.com/dominikzorgnotti/kubectl-lsdeploy",
        "Source Code": "https://github.com/dominikzorgnotti/kubectl-lsdeploy",
    },
    classifiers=[
        'License :: GNU GENERAL PUBLIC LICENSE Version 3'
    ]
)
