Flipper!
=======================

|PyPI| |GitHub-license| |Requires.io| |Travis|

    Built from `makenew/python-package <https://github.com/makenew/python-package>`__.n
.. |PyPI| image:: https://img.shields.io/pypi/v/flipper.svg
   :target: https://pypi.python.org/pypi/flipper
   :alt: PyPI
.. |GitHub-license| image:: https://img.shields.io/github/license/mPharma/flipper.svg
   :target: ./LICENSE.txt
   :alt: GitHub license
.. |Requires.io| image:: https://img.shields.io/requires/github/mPharma/flipper.svg
   :target: https://requires.io/github/mPharma/flipper/requirements/
   :alt: Requires.io
.. |Travis| image:: https://img.shields.io/travis/mPharma/flipper.svg
   :target: https://travis-ci.org/mPharma/flipper
   :alt: Travis

Description
-----------

Feature flipper that uses environment variables to ftoggle features

e.g.

::
    import flipper

    @periodic_task(run_every=(crontab(hour='10', minute='0', day_of_week='mon,wed,fri')))
    def fire_past_dispensation_due_date_chain():
        """
        at 10 am on mondays wednesdays and fridays,
        fire this chain. which will result in sending a bunch of notifications
        """

        # this block will do nothing unless FEATURE_SLACK_DISPENSATION_DUE
        # environment variable is set to 1
        flipper.flippit('slack_dispensation_due',
                        chain(get_past_dispensation_due_date.s(),
                              build_slack_dispensation_due_payloads.s(),
                              fire_dispensation_due_payloads.s(), ).apply_async)()
        return True

Installation
------------

This package is registered on the `Python Package Index (PyPI)`_
as flipper_.

Add this line to your application's requirements.txt

::

    flipper

and install it with

::

    $ pip install -r requirements.txt

If you are writing a Python package which will depend on this,
add this to your requirements in ``setup.py``.

Alternatively, install it directly using pip with

::

    $ pip install flipper

.. _flipper: https://pypi.python.org/pypi/flipper
.. _Python Package Index (PyPI): https://pypi.python.org/

Development and Testing
-----------------------

Source Code
~~~~~~~~~~~

The `flipper source`_ is hosted on GitHub.
Clone the project with

::

    $ git clone https://github.com/mPharma/flipper.git

.. _flipper source: https://github.com/mPharma/flipper

Requirements
~~~~~~~~~~~~

You will need `Python 3`_ with pip_.

Install the development dependencies with

::

    $ pip install -r requirements.devel.txt

.. _pip: https://pip.pypa.io/
.. _Python 3: https://www.python.org/

Tests
~~~~~

Lint code with

::

    $ python setup.py lint


Run tests with

::

    $ python setup.py test

Contributing
------------

Please submit and comment on bug reports and feature requests.

To submit a patch:

1. Fork it (https://github.com/mPharma/flipper/fork).
2. Create your feature branch (``git checkout -b my-new-feature``).
3. Make changes. Write and run tests.
4. Commit your changes (``git commit -am 'Add some feature'``).
5. Push to the branch (``git push origin my-new-feature``).
6. Create a new Pull Request.

License
-------

This Python package is licensed under the MIT license.

Warranty
--------

This software is provided "as is" and without any express or implied
warranties, including, without limitation, the implied warranties of
merchantibility and fitness for a particular purpose.
