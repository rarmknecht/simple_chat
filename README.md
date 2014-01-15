simple_chat
===========

Playground Application to Practice Various Concepts

 - Python Network Traffic
 - Message Queuing
 - Git Branches

###Network Traffic
While researching how to support non-blocking IO, I discovered that there is a general purpose networking library called `Twisted <http://twistedmatrix.com/trac/`.  This library is event-driven and covers many of the corner cases that would take a significant amount of time to discover, understand, and address.

It can be installed with: `pip install twisted`

###Unit Testing
Unit testing is now supported.  Main check is for conformance to the PEP8 Style Guide.

Run the test be executing: `python -m unittest discover`

The unittest and pep8 modules are required. Both can be installed through pip:
    
    $ pip install unittest
    $ pip install pep8
