hattrick-oauth
==============

Example of using the oauth2 library for developing Python CHPP applications.

Scope
-----
This is a short example on how to use the oauth2 Python library for interacting with the Hattrick [1] CHPP interface. It is not intended to be a complete wrapper or library: the main intention is to provide a starting point for Python CHPP developers.

Forking the project and improving it is more than encouraged, as it lacks some features (in particular, the possibility of using oauth_callback on the request_token call) and would really benefit from redesigning it as a proper library - also, there are no plans at the moment for maintaning/improving this repository.

Usage
-----
Please check the [example](example.py) file.

Dependencies
------------
* python-oauth2 [2]




[1] http://www.hattrick.org

[2] https://github.com/simplegeo/python-oauth2
