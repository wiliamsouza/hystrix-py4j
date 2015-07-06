hystrix-py4j
============

A Netflix Hystrix in Python using py4j.

This is an exploration path instead of porting everything maybe binding to
Java code would make the process of having hystrix running on Python fast.


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

Start Java JVM:

```
gradle startHystrixPython
```

Run tests:

```
python setup.py test
```


LICENSE
-------

Copyright 2015 Hystrix Python Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
