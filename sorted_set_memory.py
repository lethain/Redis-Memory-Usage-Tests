import redis
import uuid
import time

r = redis.Redis(host='localhost', port=6379, db=0)


# number of sets                                                                                      
for num_sets in (100, 1000,10000):
    for set_size in (100, 1000,10000):
        r.flushall()
        time.sleep(1.0)
        initial_size = r.dbsize()
        initial_info = r.info()

        for i in xrange(0, num_sets):
            # number of items per set                                                                 
            for j in xrange(0, set_size):
                        r.zadd("set.%s" % (i,), str(uuid.uuid4()), time.time())

        final_size = r.dbsize()
        final_info = r.info()

        print "For %s sets with %s values." % (num_sets, set_size)
        print "Keys: %s => %s" % (initial_size, final_size)
        print "Memory: %s => %s" % (initial_info['used_memory_human'],
                                    final_info['used_memory_human'])
        r.flushall()

