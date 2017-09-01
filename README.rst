impulsare/ruler
===============================

.. image:: https://travis-ci.org/impulsare/ruler.svg?branch=master
    :target: https://travis-ci.org/impulsare/ruler

.. image:: https://scrutinizer-ci.com/g/impulsare/ruler/badges/quality-score.png?b=master
    :target: https://scrutinizer-ci.com/g/impulsare/ruler/

.. image:: https://scrutinizer-ci.com/g/impulsare/ruler/badges/coverage.png?b=master
    :target: https://travis-ci.org/impulsare/ruler


Overview
--------------------

Reads records from a queue (put there by ``reader``) and process records to another (``writer``).
It's a middleware that transforms / validate / generate data.

**WARNING** : For now it does nothing than passing records from one queue to another.


Installation / Usage
--------------------

To install use pip:

.. code-block:: bash

    $ pip install --upgrade impulsare-ruler



Configuration
-------------
To be able to use the ruler you need to have a complete configuration file
which looks like the following (the same is used for extractor / writer) :

.. code-block:: yaml

    job:
        db: /home/app/data/impulsare.db
    logger:
        level: DEBUG
        directory: /home/app/log
        handlers:
            file: true
            console: true
    distributer:
        host: redis


An extra config also defines where to send the data once it has been *ruled* :


.. code-block:: yaml

    ruler:
        queue: writer



Run the listener
----------------

.. code-block:: shell

    $ CONFIG_FILE=/home/app/conf/config.yml queue-listener -h redis -q ruler


Tests
--------

.. code-block:: bash

    $ pip install -r requirements.txt
    $ pip install -r requirements-dev.txt
    $ py.test


**WARNING** : As the component is not ready yet, it contains no tests.
