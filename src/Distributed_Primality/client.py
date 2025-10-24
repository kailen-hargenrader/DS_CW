from .coordinator import Coordinator
from Distributed_Primality import (
    PATH_FORMAT, 
    WORK_FORMAT, 
    RESULT_FORMAT
)


class Client:
    """Client that submits read/write requests via the coordinator."""

    def __init__(self, coordinator: Coordinator):
        """Initialize with a coordinator reference to handle client requests.
        
        Args:
            coordinator: The coordinator instance to handle client requests.
        """
        pass

    def request_work(self, work: WORK_FORMAT) -> None:
        """Request the coordinator to execute work.
        
        Args:
            work: The work to execute.
        """
        pass

    def read_result(self, path: PATH_FORMAT) -> RESULT_FORMAT:
        """Read the result from the filesystem."""
        pass
