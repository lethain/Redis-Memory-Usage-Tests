# Redis-Memory-Usage-Tests


Collection of tests to measure redis memory usage.

## Run script

```
python run.py --option  [hset, lpush, sadd, zadd, set] --hostname [redis hostname]
```
Exmaple:
```
python run.py --option  set --hostname localhost
```


## Building image
```
docker build . -t redismemoryusagetests:latest
```
### Using Docker
Exmaple
```
 docker run -ti --network="host" redismemoryusagetests:latest --option set --hostname localhost
```