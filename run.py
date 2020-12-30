import argparse
import sys
import redis
from hash_memory import hsetKeys
from list_memory import lpushKeys
from set_memory import saddKeys
from sorted_set_memory import zaddKeys
from string_memory import setKeys

parser = argparse.ArgumentParser()
parser.add_argument('--option', help="Please Select one of hte option [hset, lpush, sadd, zadd, set]")
parser.add_argument('--hostname',  help="redis hostname", type=str)

args = parser.parse_args()
# Make redis connection
r = redis.Redis(host=args.hostname, port=6379, db=0)

if args.option == "hset":
    hsetKeys(r)
elif args.option == "lpush":
    lpushKeys(r)
elif args.option == "sadd":
    saddKeys(r)
elif args.option == "zadd":
    zaddKeys(r)
elif args.option == "set":
    setKeys(r)
else:
    print("Please Select one of hte option [hset, lpush, sadd, zadd, set]")
    sys.exit(1)
