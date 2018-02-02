.. Buzio documentation master file, created by
   sphinx-quickstart on Fri Oct 27 10:56:33 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Buzio's documentation!
=================================

This document will guide you how to install, configure and use Buzio_ in your projects.

What is Buzio?
---------------

Buzio_ is a python library tool for printing formatted text in terminal, similar to termcolor_ or colored_. But unlike these, Buzio_ has some new features like:

Generate fancy formats
......................

"Section" example 1:

.. code-block:: python

	from buzio import console

	console.section("First Section")

Terminal output::

	$ >> First Section
	$ ----------------

"Section" example 2:

.. code-block:: python

	from buzio import console

	console.section("Main Section", full_width=True, transform="upper center")

Terminal output::

	$ >                                 MAIN SECTION                                 <
	$ --------------------------------------------------------------------------------


Humanize Python objects
.......................

Buzio_ can automatically humanize any python object for printing in terminal:

.. code-block:: python

	from datetime import datetime, timedelta
	from buzio import console
	
	today = datetime.now()
	yesterday = today - timedelta(days=1)
	my_dict = {
		"start day": yesterday,
		"end day": today
	}

	console.box(my_dict, date_format="%a, %b-%d-%Y")

The output on terminal will be (in blue color)::

	$ *********************************
	$ *                               *
	$ *  start day: Thu, Feb-01-2018  *
	$ *   end day: Fri, Feb-02-2018   *
	$ *                               *
	$ *********************************

Ask for Input data
..................

You can use Buzio_ to automatically generate "choose" and "select" questions, based on Python objects:

"Choose" example:

.. code-block:: python

	from buzio import console

	my_choices = [
		"Orange",
		"Apple",
		"Potato"
	]

	console.choose(my_choices)

Terminal output::

	$ 1. Orange
	$ 2. Apple
	$ 3. Potato
	$ 
	$ Select (1-3): ?

"Select" example:

.. code-block:: python

	from buzio import console

	my_options = [
		"Save",
		"Save and Exit",
		"Cancel"
	]

	console.select(my_options)

Terminal output::

	$ Select: (S)ave and Exit, S(A)ve, (C)ancel? 


You can also "ask" a question and use a method to validate the answer:

.. code-block:: python

	from buzio import console

	def check_answer(answer):
	   return int(answer) == 4

	console.ask("What is the sum of 2+2", validator=check_answer)
	print("Thanks!")

Terminal output::

	$ What is the sum of 2+2? : 3
	$ Please answer again: 4
	$ Thanks!


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   tutorial
   reference

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Buzio: https://github.com/chrismaille/buzio
.. _colored: https://pypi.python.org/pypi/colored
.. _termcolor: https://pypi.python.org/pypi/termcolor