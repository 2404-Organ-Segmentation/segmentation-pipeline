from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'monai==1.3.0',
        'nibabel==5.2.0',
        'matplotlib==3.8.2',
        'tensorboard==2.15.1',
        'tqdm==4.66.1',
        'scipy==1.12.0',
        'numpy==1.24.1',
    ],
    author='2404 Organ Segmentation',
    author_email='joey.xiang426@gmail.com',
    description='Segmentation pipeline package for capstone project 2404 Organ Segmentation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/2404-Organ-Segmentation/segmentation-pipeline',
    license='MIT',
)
