IRC ===> #p2pool-mag

WORKER_PORT 33550

P2P_PORT 9452   

p2pool-mag Requirements:
-------------------------
Generic:
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local bitcoind. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py --net magcoin

Then run your miner program, connecting to 127.0.0.1 on port 33550 with any
username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 33550 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help



Official wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Notes for MagCoin:

=========================
Requirements:
-------------------------
In order to run P2Pool with the MagCoin network, you would need to build and install the
X11 module that includes the proof of work code that MagCoin uses for hashes.

Linux:



    apt-get install libboost1.48-all-dev python-dev

    git clone https://github.com/PCFiL/xcoin-hash

    cd xcoin-hash
    python setup.py install


Running P2Pool:
-------------------------
Run P2Pool with the "--net magcoin" option.
Run your miner program, connecting to 127.0.0.1 on port 33550.

Sponsors:
-------------------------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool
