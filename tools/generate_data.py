# -*- coding:utf8 -*-

import pickle
import redis
import random
from collections import defaultdict

all_data = {}

def generate_data(topic_num=256, x_axis=32, y_axis = 32, dot_max = 100, dot_prop=0.4, prefix_id="id", prefix_title="title"):
    cur_topic_id = 0
    step = x_axis * y_axis // topic_num
    for x in range(0, x_axis, step):
        for y in range(0, y_axis, step):
            if cur_topic_id >= topic_num:
                break
            for dot in range(dot_max):
                idid = "{}-{}-{}-{}".format(prefix_id, x, y, dot) 
                if random.uniform(0, 1) < dot_prop:
                    all_data.setdefault(cur_topic_id,[]).append( 
                        (random.uniform(0, 1) + x, random.uniform(0,1) + y, idid, "{}{}".format(prefix_title, idid))
                    )
            cur_topic_id+=1
        if cur_topic_id >= topic_num:
            break

generate_data()

r = redis.StrictRedis("localhost", 6377, 1)
pipe = r.pipeline()
for label, data_list in all_data.items():
    pickled_object = pickle.dumps(data_list)
    pipe.set(label, pickled_object)
pipe.execute() 