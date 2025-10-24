from .filesystem import AFSFilesystem
from .coordinator import Coordinator
from Distributed_Primality import (
    WORK_FORMAT, 
    RESULT_FORMAT, 
    NODE_ID_FORMAT, 
    NODE_ADDRESS_FORMAT, 
    REQUEST_ID_FORMAT,
    PATH_FORMAT
)

class Node:
    """Storage/compute node that executes coordinator-assigned work."""

    def __init__(
        self, 
        node_id: NODE_ID_FORMAT, 
        address: NODE_ADDRESS_FORMAT, 
        filesystem: AFSFilesystem, 
        coordinator: Coordinator
    ):
        """Initialize node identity, address, filesystem, and coordinator link."""
        pass

    def execute_work(self, work: WORK_FORMAT) -> None:
        """Execute the work specification and write results to the filesystem."""
        pass

    def write_result(self, path: PATH_FORMAT, result: RESULT_FORMAT) -> None:
        """Write the result to the filesystem."""
        pass

    def report_completion(self, request_id: REQUEST_ID_FORMAT) -> None:
        """Notify the coordinator that the request is complete."""
        pass
