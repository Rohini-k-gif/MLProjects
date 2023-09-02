from setuptools import find_packages,setup
from typing import List

#Next line is to get -e . in requirements.txt
hyphen_e='-e .'
def get_reqs(file_path:str)->List [str]: 
    requirements=[]
    with open(file_path) as file_obj: 
        'reading  requirements.txt file line by line'
        requirements=file_obj.readlines() 
        'replacing newline chr in requirements by blank'
        requirements=[req.replace("\n","") for req in requirements] 
        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
    return requirements
setup (
    name='MLProject',
    version='0.0.1',
    author='Rohini',
    author_email='rmadedu08@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)