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

## Building cython files
- Create a folder, and paste your whole code in file_name.pyx 
- create setup.py and copy the contents similar from setup.py in the project
- Building cython file
```python
python3 setup.py build_ext --inplace
```
- Execute it by importing via your console


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
