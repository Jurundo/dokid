from .service import *

def create_service(path):
    '''Creates a service from a path to the ini file. Returns a ServiceThread object.'''
    name = path.split("/")[-1]
    if name.endswith(".ini"):
        name = name.split(".")
        name.pop(-1)
        name = ".".join(name)
    service = Service(name, path)
    return ServiceThread(service=service)