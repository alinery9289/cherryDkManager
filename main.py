'''
Created on 2017.11.3

@author: zhangxusheng
'''

import docker

if __name__ == '__main__':
    client = docker.from_env(version="1.30")
    imageList = client.images.list()
    print imageList
    containerList = client.containers.list()
    print containerList
    