Shutter
=======
Tango device for shutter device

What's inside
-------------
This repository contains installation files required to use Shutter Tango 
Device Class. 
 
How to install
--------------

First, clone git repository:
```console
git clone https://github.com/synchrotron-solaris/dev-solaris-shutter.git
```
Then, enter the repository:
```console
cd dev-solaris-shutter
```
Now you can use:
```console
python setup.py install
```
or:
```console
pip install .
```

How to run
----------
After installation, there is only one script: `Shutter`.
You can use it via:
```console
Shutter instance_name
```
Remember that Device Server instance has to registered in database previously.

Requirements
------------

- `setuptools`
- `facadedevice` >= 1.0.1
- `pytango` >= 9.2.1

License
-------
This sample project is distributed under LGPLv3 (see `LICENSE` file).
