from setuptools import setup, find_packages
from typing import List

HYPHON_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)

    return requirements

setup(
    name="my_ml_project",
    version="0.1",
    author="Anshul",
    description="A machine learning project",
    packages=find_packages(),
    install_requires=get_requirements("requirement.txt")
)