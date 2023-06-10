# performace-poc

## Desciption

[Link to article](https://medium.com/@ratneshchandak/from-python-to-cython-turbocharging-your-code-for-lightning-fast-execution-b5e883898ac6)

Project to analyze execution time via different ways in python
- Normal python file execution
- Building python package and running by importing it
- Compiling it with cython and running by importing it

## pip
Project package at https://test.pypi.org/project/py-performance-poc/


## install

```python
pip install -i https://test.pypi.org/simple/ py-performance-poc==0.0.3
```

## Building python package
```python
python3 -m build
python3 -m twine upload --repository testpypi dist/*
```
## Building cython files
- Create a folder, and paste your whole code in file_name.pyx 
- create setup.py and copy the contents similar from setup.py in the project
- Building cython file
```python
python3 setup.py build_ext --inplace
```
- Execute it by importing via your console


## python_to_cython: Create your own and test it out
- Create virtual environment which will be needed for installing python [Follow this if you are new](https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code/68076478#68076478) 
- Activate the virtual environment
- Create a folder <your_folder_name>
- create am empty __init__.py file
- create a <your_file_name>.py file
- Paste [sample content](https://github.com/ratnesh93/performace-poc/blob/main/python_to_cython/performance.py) into it or create your own conent for computations
- create a <test_your_file_name>.py file.
- Import your python class in the test file and call the method for computations.
- Run above multiple times and record your execution times. 
```python
python path_to_your_file/test_your_file_name.py
```
- Now lets start cython programming
- Create <your_cython_file_name>.pyx and paste the contents of the <your_file_name>.py file
- Create setup.py and add [below code](https://github.com/ratnesh93/performace-poc/blob/main/python_to_cython/setup.py) in it.
```python
from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [Extension("<your_cython_file_name>", ["<your_cython_file_name>.pyx"])]

setup(
    ext_modules = cythonize(extensions)
)
```
- Now build your cython file
```python
python3 setup.py build_ext --inplace
```
- After successful build, you will see one new build folder, one new <your_cython_file_name>.c and one new <your_cython_file_name.cypthon...>.so file
- Now create <test_your_cython_file_name>.py
- Import your cython class in the test file and call the method for computations.
- Run above multiple times and record your execution times. Run in same machine and in similar conditions.
```python
python path_to_your_file/test_your_cython_file_name.py
```

## Experiment
|n | time (seconds)-python | time (seconds)-cython | Performance Improvement (%) |
|--|--|--|--|
| Average |35.367467|26.993737|23.67636|
|--|--|--|--|
|1|34.81232|26.96337||
|2|36.34826|26.79724||
|3|36.06108|27.10838||
|4|34.89695|27.13302||
|5|34.80449|26.63584||
|6|34.87149|27.09555||
|7|35.90095|26.8832||
|8|35.46488|27.66893||
|9|35.02143|26.80006||
|10|35.49282|26.85178||

## What is minimum file needed after build for cython to run the program
- file_name.pyc
- compiled_file_name.so
- You only need your .so and .pyx file, copy that in your project and start using by importing it.

## Usage

```python
source <path_to_project>/.venv/bin/activate
python <path_to_project>/test_performance.py
python <path_to_project>/test_cython_performance.py
```

```python
from performance import Performance
my_test_performance = Performance()
my_test_performance.some_random_computations()
```

```python
from cython_performance import Performance

my_test_performance = Performance()
my_test_performance.some_random_computations()
```

## Conclusion
- Converting same piece of code into python package, did not made a difference in execution time 
- Comiling with cython same piece of code, executed faster than normal python compiler
- Execution in cython seems faster, needs more methods to test it out

## Results
- test_performance.py took on average of 35.367467 seconds
- test_cython_performance.py took on average of 26.993737 seconds
- Cython code executed 23.67636% faster on average.

## Collaboration
- Please add your methods and raise PR to compare execution time via different ways.
