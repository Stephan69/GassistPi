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
    if type =='uri':
        topic = configuration['MQTT_AUDIO']['TOPIC_URI']
    elif type =='wav':
        topic = configuration['MQTT_AUDIO']['TOPIC_WAV']
    if topic is not None:
        infot = client.publish(topic, payload)
        infot.wait_for_publish()

def mqtt_create_client():
    client = mqtt.Client()
    #client.username_pw_set(configuration['MQTT_AUDIO']['UNAME'], configuration['MQTT_AUDIO']['PSWRD'])
    client.connect(configuration['MQTT_AUDIO']['IP'], 1883, 65535)
    client.loop_start()
    return client
