import uuid
import time
def hsetKeys(r):
    print("Start inserting keys..")
    for num_hashes in (10000,):
        for hash_size in (1000,):
            r.flushall()
            time.sleep(1.0)
            initial_size = r.dbsize()
            initial_info = r.info()

            for i in range(num_hashes):
                for j in range(hash_size):
                    r.hset("hash.%s" % (i,), str(uuid.uuid4()), time.time())

                    final_size = r.dbsize()
                    final_info = r.info()

            print("For %s sets with %s values." % (num_hashes, hash_size))
            print("Keys: %s => %s" % (initial_size, final_size))
            print("Memory: %s => %s" % (initial_info['used_memory_human'],
                                        final_info['used_memory_human']))
            r.flushall()
    print("Done")
