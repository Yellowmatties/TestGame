# gcc -std=c99 -O3 -shared -o world \
#   -I src -I deps/noise deps/noise/noise.c src/world.class

from ctypes import CDLL, CFUNCTYPE, c_float, c_int, c_void_p
from collections import OrderedDict

dll = CDLL('./world')

WORLD_FUNC = CFUNCTYPE(None, c_int, c_int, c_int, c_int, c_void_p)

def dll_seed(x):
    dll_seed(x)

def dll_create_world(p, q):
    result = {}
    def world_func(x, y, z, w, arg):
        result[(x, y, z)] = w
    dll.create_world(p, q, WORLD_FUNC(world_func), None)
    return result

dll.simplex2.restype = c_float
dll.simplex2.argtype = [c_float, c_float, c_int, c_float, c_float]
def dll_simplex2(x, y, octaves=1, perstistence=0.5, lacunarity=2.0):
    return dll.simplex2(x, y, octaves, perstistence, lacunarity)
