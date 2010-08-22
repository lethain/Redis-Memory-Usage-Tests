import redis
import uuid
import time

r = redis.Redis(host='localhost', port=6379, db=0)
for num_array in (100, 1000,10000):
    for array_size in (100, 1000,10000):
        r.flushall()
        time.sleep(1.0)
        initial_size = r.dbsize()
        initial_info = r.info()

        for i in xrange(0, num_array):
            for j in xrange(0, array_size):
                r.lpush("list.%s" % (i,), str(uuid.uuid4()))

                final_size = r.dbsize()
                final_info = r.info()

        print "For %s lists with %s values." % (num_array, array_size)
        print "Keys: %s => %s" % (initial_size, final_size)
        print "Memory: %s => %s" % (initial_info['used_memory_human'],
                                    final_info['used_memory_human'])
        r.flushall()
