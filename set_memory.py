def saddKeys(r):
    print("Start inserting keys..")
    # number of sets
    for num_sets in (100, 1000, 1000):
        for set_size in (100, 1000, 1000):
            r.flushall()
            time.sleep(1.0)
            initial_size = r.dbsize()
            initial_info = r.info()

            for i in range(num_sets):
                # number of items per set
                for j in range(set_size):
                    r.sadd("set.%s" % (i,), str(uuid.uuid4()))

            final_size = r.dbsize()
            final_info = r.info()

            print("For %s sets with %s values." % (num_sets, set_size))
            print("Keys: %s => %s" % (initial_size, final_size))
            print("Memory: %s => %s" % (initial_info['used_memory_human'],
                                        final_info['used_memory_human']))
            r.flushall()
    print("Done")
