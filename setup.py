from setuptools import find_packages,setup
from typing import List

HYPHEN_DOT_E ='-e .'
def get_requirements(file_path:str)->List[str]:# inputting file path in the form of string and returning list of strings.
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if HYPHEN_DOT_E in requirements:
        requirements.remove(HYPHEN_DOT_E)
        
    return requirements

setup(
    name = 'WaferFaultPrediction',
    version = '0.0.1',
    author = 'Megha',
    author_email = 'abc@gmail.com',
    #install_requries = ['pandas','sklearn'],
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()
    
)