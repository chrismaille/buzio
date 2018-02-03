Welcome to Buzio's documentation!
=================================

[![PyPI](https://img.shields.io/pypi/v/nine.svg)](https://pypi.python.org/pypi/buzio)
[![Build Status](https://travis-ci.org/chrismaille/buzio.svg?branch=master)](https://travis-ci.org/chrismaille/buzio)
[![PyPI](https://img.shields.io/pypi/pyversions/buzio.svg)](https://pypi.python.org/pypi/buzio)
[![Coverage Status](https://coveralls.io/repos/github/chrismaille/buzio/badge.svg?branch=master)](https://coveralls.io/github/chrismaille/buzio?branch=master)
[![Documentation Status](https://readthedocs.org/projects/buzio/badge/?version=latest)](http://buzio.readthedocs.io/en/latest/?badge=latest)

* Read the Docs: http://buzio.readthedocs.io/
* Source Code: https://github.com/chrismaille/buzio

**Buzio** is a python library tool for printing formatted text in terminal, similar to [termcolor](https://pypi.python.org/pypi/termcolor) or [colored](https://pypi.python.org/pypi/colored).

### Installing Buzio

Install Buzio using the command:

```bash
    $ pip install buzio
```

### Importing the Library

```python
    from buzio import console, formatStr
```

The `console` is a instance of the `Console` class initialized with default color themes. You can also import the class and instantiate with your own settings (See the documentation for more info)

The `formatStr` is also a instance of the `Console` class too, but instead of printing in terminal the message, this instance just return the formatted text.

#### The default color themes:

|Method            | Text Color          |
|------------------|---------------------|
|console.box       |  Fore.CYAN          |
|console.error     |  Fore.RED           |
|console.info      |  Fore.CYAN          |
|console.section   |  Fore.LIGHTYELLOW_EX|
|console.success   |  Fore.GREEN         |
|console.warning   |  Fore.YELLOW        |

These colors are based in [colorama](https://pypi.python.org/pypi/colorama) constants.

### Generate fancy formats

**"Section" example 1**:

```python
    from buzio import console

    console.section("First Section")
```

Terminal output::

```bash
$ >> First Section
$ ----------------
```

### Humanize Python objects

**Buzio** can automatically humanize any python object for printing in terminal:

```python
    from datetime import datetime, timedelta
    from buzio import console
    
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    my_dict = {
        "start day": yesterday,
        "end day": today
    }

    console.box(my_dict, date_format="%a, %b-%d-%Y")
```

The output on terminal will be:

```bash
    $ *********************************
    $ *                               *
    $ *  start day: Thu, Feb-01-2018  *
    $ *   end day: Fri, Feb-02-2018   *
    $ *                               *
    $ *********************************
```

### Ask for Input data

You can use **Buzio** to automatically generate "choose" and "select" questions, based on Python objects:

**"Choose" example:**

```python
    from buzio import console

    my_choices = [
        "Orange",
        "Apple",
        "Potato"
    ]

    console.choose(my_choices)
```

Terminal output::

```bash
    $ 1. Orange
    $ 2. Apple
    $ 3. Potato
    $ 
    $ Select (1-3): ?
```

### Run terminal commands

You can use **Buzio** to run terminal commands (using Python `subprocess`) and get the *stdout* result:

```python
    >>> from buzio import console
    >>> ret = console.run("echo HelloWorld!", get_stdout=True, verbose=True)
    Cmd: echo HelloWorld!
    >>> print(ret)
    HelloWorld!
```

### Further reading

Please check full documentation in http://buzio.readthedocs.io/
