##Django Boilerplate

Django Boilerplate is a set of project layouts that through trial and error we use
as a best practice.  Details about each project are stored in conf/project.py and are imported to
allow for maximum re-usability.


#Assumptions

* Python 2.7, PIP, and virtualenv installed.
* Use south
* Django 1.6 is the latest version of django at the current time.


## Vagrant/Salt

Included with the boilerplate structure is a salt/vagrant setup for easily
creating replicated development environments.  You can modify the core salt state
and add remove states as you see fit.  Make sure to go through  and remove the references
to ``test``.


