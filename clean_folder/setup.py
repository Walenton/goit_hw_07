from setuptools import setup

setup(
    name='clean_folder',
    version='0.1.0',
    description='clean and sort your folder',
    url='https://github.com/Walenton/goit_repo',
    author='Valentyn Tonkonih',
    author_email='xzibitness@gmail.com',
    license='MIT',
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)