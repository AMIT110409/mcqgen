## this we initalize to install local package in environment . 

from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Amit Rathore',
    author_email='amitrathore110409@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)
