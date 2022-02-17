#!/usr/bin/env python

# Copyright (C) 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import paho.mqtt.client as mqtt
import yaml
import os

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))

with open('{}/src/config.yaml'.format(ROOT_PATH),'r', encoding='utf8') as conf:
    configuration = yaml.load(conf, Loader=yaml.FullLoader)

def publish_uri_wav(client, type, payload):
    topic = None
    if type =='string':
        topic = configuration['MQTT_AUDIO']['TOPIC_URI']
    elif type =='wav':
        topic = configuration['MQTT_AUDIO']['TOPIC_WAV']
    if topic is not None:
        infot = client.publish(topic, payload)
        infot.wait_for_publish()
        client.disconnect()


def on_connect_publish(rc):
    print("Connected with result code "+str(rc))

def on_message_publish(obj, mid):
    print("mid: " + str(mid))

def mqtt_start_publish():
    client = mqtt.Client()
    client.on_connect = on_connect_publish
    client.on_publish = on_message_publish
    client.username_pw_set(configuration['MQTT_AUDIO']['UNAME'], configuration['MQTT_AUDIO']['PSWRD'])
    client.connect(configuration['MQTT_AUDIO']['IP'], 1883, 60)
    return client

client = mqtt_start_publish()
publish_uri_wav(client, 'string', 'test')