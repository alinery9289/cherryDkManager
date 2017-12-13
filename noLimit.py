'''
Created on 2017.11.3

@author: zhangxusheng
'''

import docker

VERSION = "1.30"
IMAGE_NAME = "cherry:version3"
COMMAND = ["/bin/bash", "/root/Project/start_celery_worker.sh"]
NUM = 3

if __name__ == '__main__':
    client = docker.from_env(version="1.30")
    imageList = client.images.list()
    print imageList
    for i in range(NUM):
        oneContainer = client.containers.run(image = IMAGE_NAME,
                                             command = COMMAND,
                                             detach=True,
                                             environment = ["worker_name=cherryDK_"+str(i),"C_FORCE_ROOT=true"],
                                             name = "cherryDK_No_Limit_"+str(i))
        print oneContainer.logs()

    containerList = client.containers.list(all=True)
    print containerList


