import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.c=weakref.ref(a.c,callback)
keepalive.append(a)
keepalive.append(lst)
keepalive.append(callback)
gcthrm=threading.Thread(target=gc.collect)
gcthrm.start()
gcthrm.join()
del keepalive`

## Building docker image
Build docker image from root folder of project:
`docker build . -t python_samples_<VERSION_TAG>`

## Patching vulnerability
Patch vulnerability in `docker-entrypoint.sh`:

1. Run docker build and save the build in intermediate docker file `docker build . -t python_samples_vulnerable_<VERSION_TAG>_build`
2. Stop running docker container
3. Start running docker container from patched docker image (replacing vulnerable image name with patched image name): 
`docker run -d --rm --name="python_samples_<VERSION_TAG>" python_samples_<VERSION_TAG>`

## Starting docker container
Start running docker container (depends on vulnerable or patched version): 

