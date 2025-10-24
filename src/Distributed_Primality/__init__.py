"""Distributed_Primality AFS v1 skeleton package."""

__version__ = "0.1.0"

from .filesystem import AFSFilesystem  
from .coordinator import Coordinator  
from .node import Node   
from .client import Client  

WORK_FORMAT = list[int]
RESULT_FORMAT = dict[int, bool]
STORAGE_FORMAT = dict[int, bool]
PATH_FORMAT = str
DATA_FORMAT = bytes
CLIENT_ID_FORMAT = str
CLIENT_ADDRESS_FORMAT = str
NODE_ID_FORMAT = str
NODE_ADDRESS_FORMAT = str
REQUEST_ID_FORMAT = str
