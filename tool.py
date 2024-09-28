# coding=utf-8
import os
from os.path import dirname, abspath
import yaml


def read_yaml(key):
    path = dirname(abspath(__file__))
    path = os.path.join(path, 'Config', 'Config.yaml')
    with open(path, "r") as f:
        value = yaml.safe_load(f)
    return value[key]


# data = read_yaml('db').get('name')
# print(data)
# print(data)  # {'age': 45, 'name': 'zhangsan'}
# def read_dbconfig():
