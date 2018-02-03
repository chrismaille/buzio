Tutorial
========

This document will explain how to install Buzio_ and use it in your projects.

Installing Buzio
-----------------

Install Buzio using the command::

    $ pip install buzio

Importing the Library
---------------------

.. code-block:: python

    from buzio import console, formatStr

The ``console`` is a instance of the ``Console`` class initialized with default color themes. You can also import the class and instantiate with your own settings (See the :doc:reference for more info)

The ``formatStr`` is also a instance of the ``Console`` class too, but instead of printing in terminal the message, this instance just return the formatted text.

Example:

.. code-block:: python
    
    >>> from buzio import console, formatStr
    >>> ret = console.ask("What is the sum of 2+2?")
    What is the sum of 2+2? : 4
    >>> print(ret)
    4
    >>> ret = formatStr.ask("What is the sum of 2+2")
    >>> print(ret)
    ['\x1b[33mWhat is the sum of 2+2 \x1b[0m']

The Output styles
-----------------

Use the following styles to print your data:

=================== ======================= ===========
Method              Text Color              Show Prefix
=================== ======================= ===========
console.box         Fore.CYAN               No
console.error       Fore.RED                Yes
console.info        Fore.CYAN               Yes
console.section     Fore.LIGHTYELLOW_EX     No
console.success     Fore.GREEN              Yes
console.warning     Fore.YELLOW             Yes
=================== ======================= ===========

The *Text Color* objects are based in colorama_ settings. Please check colorama documentation for all available constants and the :doc:`reference` for create your own styles.

The *Show Prefix* column tells if the text to be printed will be the section name append in in. For example, ``console.sucess("Operation Complete")`` will be printed as::

    $ Success: Operation Complete

You can control this behavior with the ``use_prefix`` paramenter. For example: ``console.info("Starting download...", use_prefix=False)```

The Input styles
----------------

Use the following styles to print your input data questions:

================ ====================== =========== =============== ============
Method           Text Color             Use Default Custom Question Can Validate
================ ====================== =========== =============== ============
console.ask      Fore.YELLOW            Yes         N/A             Yes
console.choose   Fore.LIGHTYELLOW_EX    Yes         Yes             No
console.confirm  Fore.LIGHTMAGENTA_EX   Yes         No              No
console.select   Fore.LIGHTYELLOW_EX    Yes         Yes             No
================ ====================== =========== =============== ============

The *Text Color* objects are based in colorama_ settings. Please check `colorama source code`_ for all available constants and the :doc:`reference` for create your own styles.

The *Use Default* means you can pass a default value for answer. This can be a python object too. Example: ``console.ask("What is the sum of 2+2?", default=4)``

The *Custom Question* means you can pass a custom question for the command. Example: ``console.choose(my_list, question="What's your prefered fruit?")``

The *Can Validate* means you can pass a callable object, so Buzio_ can validate the prompt answer before return the value to your code. Example: ``console.ask("What is the sum of 2+2?", default=4, validator=check_sum)``

Returning data
++++++++++++++

Data returned from input styles are:

* ``console.ask``: string typed.
* ``console.choose``: the *python object* selected from original list
* ``console.confirm``: boolean
* ``console.select``: the *index* for the select object in original list

Special Commands
----------------

================ =============================
Method           Description       
================ =============================
console.clear    Clear the terminal
console.progress Show a animated progress bar
console.run      Run a terminal command
console.slugify  Create a slug from text
console.unitext  Convert any text to ascii
================ ============================

Use the ``console.clear`` method to clear the terminal.

Use the ``console.progress`` to generate a animated progress bar.

Use the ``console.run`` method to run terminal commands. The return data will be a boolean (if task was succeded) or the capture ``stdout`` from command (use ``get_stdout=True``). Please check :doc:`reference` page for all options.

.. code-block:: python

    >>> console.run("lsb_release -a", get_stdout=True)
    No LSB modules are available.
    Distributor ID: Ubuntu
    Description:    Ubuntu 17.10
    Release:    17.10
    Codename:   artful

Use the ``console.slugify`` to generate a slug version from text::

.. code-block:: python

    >>> console.slugify("Hello World")
    hello_word

Use the ``console.unitext`` to convert text to ascii::

.. code-block:: python

    >>> console.unitext("São Paulo")
    Sao Paulo


.. _Buzio: https://github.com/chrismaille/buzio
.. _colorama: https://pypi.python.org/pypi/colorama
.. _colorama source code: https://github.com/tartley/colorama/blob/8fc6600344f1e1425cfb2f8112056d55ec9b9873/colorama/ansi.py#L49