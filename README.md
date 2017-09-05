# Cluster Graph Demo based on Echarts, Redis and Flask

Cluster Graph Demo based on Echarts, Redis, Flask, Python 2.7+

![demo](/pic/pic.jpg)

## Preparation

```
Python 2.7+
Redis 3.2.100
Echarts, jQuery in `static/` folder
```

### Redis server

Make sure that the Redis server is running with the following configuration, if you don't change the configuration of Redis client.

```python
redis_client = redis.StrictRedis(host='127.0.0.1',port=6377,db=1)
```

You can generate the sample data by using `tools/generate_data.py`.

## Run

```bash
cd flask_echarts/
pip install -r requirements.txt
python app.py
```

Then visit `http://localhost:5000` in your browser.

## Overview

The format of topic_ids for input just likes `list` or `range` in Python, as below:

|Input of text | Python List |
|------|------|
|"0,50,100,150,200,250"|list(0,50,100,150,200,250)|
|"1:10"|range(1,11)|
|"0:99:10"|range(0, 100, 10)|
