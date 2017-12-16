'''
Created on 2017.11.3

@author: zhangxusheng
'''

import docker
import re

VERSION = "1.30"
IMAGE_NAME = "cherry:version3"
COMMAND = ["/bin/bash", "/root/Project/start_celery_worker.sh"]
CPU_PER_CON = 2
PATTERN = "cherryDK_No_Limit_[0-9]+"

if __name__ == '__main__':
    client = docker.from_env(version="1.30")
    containerList = client.containers.list();
    print containerList
    for oneContainer in containerList:
        
        if (re.match(PATTERN, oneContainer.name)):  
            print oneContainer.name
            oneContainer.stop()
            oneContainer.remove()


