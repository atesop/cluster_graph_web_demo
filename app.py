# -*- coding:utf8 -*-
from flask import Flask, request, render_template, jsonify
import redis
import json
import pickle
app = Flask(__name__)

import codecs

all_data = {}
redis_client = redis.StrictRedis(host='127.0.0.1',port=6377,db=1)
def load_file():
    with codecs.open("d:\\data\\topic_vid_2dvector_100_101_102.txt", "r") as f:
        for line in f:
            records = line.strip().split()
            all_data.setdefault(records[-3],[]).append((float(records[-2]), float(records[-1])))

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/labeldata",methods=["post"])
def labeldata():
    params = request.json
    print(params)
    labels = []
    for label in params.get("labels"):
        # label = str(label)
        pos = label.find(":")
        pos_arr = label.split(":")
        len_pos_arr = len(pos_arr)
        if len_pos_arr == 1:
            labels.append(pos_arr[0])
        else:
            begin = int(pos_arr[0])
            end = int(pos_arr[1])
            step = int(pos_arr[2]) if len_pos_arr > 2 else 1
            for i in range(begin, end+1, step):
                labels.append(str(i))
    if len(labels) == 0:
        return jsonify(data={})
    data = {}
    topics = []
    xys= []
    for label in labels:
        xys.append(pickle.loads(redis_client.get(label)))
    print(sum([len(xy) for xy in xys]))

    # for k,v in all_data.items():
        # topics.append(k)
        # xys.append(v)
    data["xy"] = xys
    data["topic"] = labels
    return jsonify(data=data)

@app.route("/test")
def test():
    data = {}
    topics = []
    xys= []
    for k,v in all_data.items():
        topics.append(k)
        xys.append(v)
    data["xy"] = xys
    data["topic"] = topics
    return jsonify(data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

