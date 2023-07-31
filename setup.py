from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open (file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        return requirements




setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='mausam',
    author_email='mausam22sharma@gmail.com',
    install_requires=['pandas','sklearn'],
    packages=find_packages()
)