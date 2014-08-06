from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(

    magcoin=math.Object(
        PARENT=networks.nets['magcoin'],
        SHARE_PERIOD=45, # seconds
        CHAIN_LENGTH=12*60*60//15, # shares
        REAL_CHAIN_LENGTH=12*60*60//15, # shares
        TARGET_LOOKBEHIND=20, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=10, # blocks
        IDENTIFIER='4d6167436f696e58'.decode('hex'),
        PREFIX='4d61676e694c6f71'.decode('hex'),
        P2P_PORT=9555,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=33550,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-mag',
        VERSION_CHECK=lambda v: True,
    ),


)
for net_name, net in nets.iteritems():
    net.NAME = net_name
