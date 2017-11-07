'''
Created on 2017.11.3

@author: zhangxusheng
'''

import docker

VERSION = "1.30"
IMAGE_NAME = "cherry:version3"
COMMAND = ["cd /root/Project", "./start_celery_worker.sh"]
CPU_PER_CON = 2

if __name__ == '__main__':
    client = docker.from_env(version="1.30")
    imageList = client.images.list()
    print imageList
    for i in range(3):
        oneContainer = client.containers.run(image = IMAGE_NAME,
                                             command = COMMAND, 
                                             cpuset_cpus = str(i*CPU_PER_CON)+"-"+str((i+1)*CPU_PER_CON-1),
                                             environment = ["worker_name=cherryDK_"+i],
                                             name = "cherryDK_"+i,
                                             mem_limit = str(2*CPU_PER_CON)+"g")
        print oneContainer.logs()
    
    containerList = client.containers.list(all=True)
    print containerList
    
    