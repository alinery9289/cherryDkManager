'''
Created on 2017.11.3

@author: zhangxusheng
'''

import docker

VERSION = "1.30"
IMAGE_NAME = "cherry:version3"
COMMAND = ["/bin/bash", "/root/Project/start_celery_worker.sh"]
CPU_NUM = 16

def getCPUs(num, i, cpuNum):
    x = cpuNum/num
    if (cpuNum%num>0):
        x+=1
    re =str((i*x)%cpuNum)
    for j in range(i*x+1,(i+2)*x):
        re+=(","+str(j%cpuNum))
    return re

if __name__ == '__main__':
    client = docker.from_env(version="1.30")
    imageList = client.images.list()
    print imageList
    NUM = input("Please input the container number:")
    if (NUM>CPU_NUM):
        print ("error")
    for i in range(NUM):
        cpus = getCPUs(NUM ,i ,CPU_NUM)
        print cpus
        oneContainer = client.containers.run(image = IMAGE_NAME,
                                             command = COMMAND,
                                             detach=True,
                                             cpuset_cpus = cpus,
                                             environment = ["worker_name=cherryDK_"+str(i),"C_FORCE_ROOT=true"],
                                             name = "cherryDK_"+str(i)
#                                              ,mem_limit = str(2*CPU_PER_CON)+"g"
                                             )
        print oneContainer.logs()
    containerList = client.containers.list(all=True)
    print containerList



