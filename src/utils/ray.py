import socket


def get_local_ray_dir():
    hname = socket.gethostname()
    #this has been changed
    raise NotImplementedError('You must specify the local directory for ray to store results')
    local_dir += 'ray_results'
    return local_dir
