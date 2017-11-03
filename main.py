'''
Created on 2017年11月3日

@author: zhangxusheng
'''

import docker

if __name__ == '__main__':
    client = docker.from_env(version="1.30")
    imageList = client.images.list()
    contannerList = client.containers.list()
    