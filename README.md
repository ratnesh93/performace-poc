# performace-poc

## Desciption
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
- Create virtual environment which will be needed for installing python (Follow this if you are new: https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code/68076478#68076478) 
- Activate the virtual environment
- Create a folder <your_folder_name>
- create am empty __init__.py file
- create a <your_file_name>.py file
- Paste content of python_to_cython/performance.py into it or create your own conent for computations
- create a <test_your_file_name>.py file.
- Import your python class in the test file and call the method for computations.
- Run above multiple times and record your execution times. 
- Now lets start cython programming
- Create <your_cython_file_name>.pyx and paste the contents of the <your_file_name>.py file
- Create setup.py and copy contents of python_to_cython/setup.py into it with modification of <your_cython_file_name>
- Now build your cython file
```python
python3 setup.py build_ext --inplace
```
- After successful build, you will see one new build folder, one new <your_cython_file_name>.c and one new <your_cython_file_name.cypthon...>.so file
- Now create <test_your_cython_file_name>.py
- Import your cython class in the test file and call the method for computations.
- Run above multiple times and record your execution times. Run in same machine and in similar conditions.

## What is minimum file needed after build for cython to run the program
- file_name.pyc
- compiled_file_name.so
- You only need your .so and .pyx file, copy that in your project and start using by importing it.

## Usage

```python
from py_performace_poc import performace
a = performace.TestPerformace()
a.test_random()
```

```python
from src.py_performace_poc import performace_cython

a= performace_cython.TestPerformace()
a.test_random()
```

## Conclusion
- Converting same piece of code into python package, did not made a difference in execution time 
- Comiling with cython same piece of code, executed faster than normal python compiler
- Execution in cython seems faster, needs more methods to test it out

## Results
- test_random func executed around 34 sec both by executing as a python file and building python package and importing and executing it.
- test_random func tooks around 26 seconds by executing via cython compiler

## Collaboration
- Please add your methods and raise PR to compare execution time via different ways.
