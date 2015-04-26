hystrix-py4j
============

A Netflix Hystrix in Python using py4j.

What is Hystrix?
----------------

For more information see the [Netflix Hystrix]
(https://github.com/Netflix/Hystrix/wiki) Wiki documentation.


How it works
------------

To know more see the [Netflix Hystrix]
(https://github.com/Netflix/Hystrix/wiki/How-it-Works) Wiki How it works
section documentation.


Features
--------

It is a test using py4j.

Dependecies
-----------

 * JDK 1.8.0_45
 * Graddle 2.3

Installation
------------

Create a virtualenv:

```
mkproject --python=fullpath_to_python_3.4> hystrix-py4j
```

Get the code:

```
git clone https://github.com/wiliamsouza/hystrix-py4j.git .
```

Build Java code:

```
gradle build
```

It will download project dependencies, build the souce code.

Install Python code:

```
python setup.py develop
```

The last command enter your code in "Development Mode" it creates an
`egg-link` in your virtualenv's `site-packages` making it available
on this environment `sys.path`. For more info see [setuptools development-mode]
(https://pythonhosted.org/setuptools/setuptools.html#development-mode)

Development and test dependencies
---------------------------------

`setup.py` will handle test dependencies, to install development use:

```
pip install -e .[dev]
```

Tests
-----

```
python setup.py test
```
