import uuid
import time
def setKeys(r):
    print("Start inserting keys..")
    for num_strings in (10000000,):
        r.flushall()
        time.sleep(1.0)
        initial_size = r.dbsize()
        initial_info = r.info()

        for i in range(num_strings):
            r.set(str(uuid.uuid4()), time.time())
        final_size = r.dbsize()
        final_info = r.info()

        print("For %s strings." % (num_strings,))
        print("Keys: %s => %s" % (initial_size, final_size))
        print("Memory: %s => %s" % (initial_info['used_memory_human'],
                                    final_info['used_memory_human']))
        r.flushall()
    print("Done")