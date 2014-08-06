import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc
from operator import *


@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)

nets = dict(

    magcoin=math.Object(
        P2P_PREFIX='d3b7c0f4'.decode('hex'),
        P2P_PORT=22557,
        ADDRESS_VERSION=110,
        RPC_PORT=22556,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'magcoin address' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),                           
        SUBSIDY_FUNC=lambda height: 10000*100000000,
        BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data)),
        BLOCK_PERIOD=60,
        SYMBOL='MAG',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'MagCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/MagCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.magcoin'), 'magcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1), 
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),



)
for net_name, net in nets.iteritems():
    net.NAME = net_name
