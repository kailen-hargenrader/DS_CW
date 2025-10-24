from Distributed_Primality import (
    NODE_ID_FORMAT, 
    NODE_ADDRESS_FORMAT, 
    CLIENT_ID_FORMAT, 
    CLIENT_ADDRESS_FORMAT,
    REQUEST_ID_FORMAT,
    WORK_FORMAT
)

class Coordinator:
    """Middleman between clients and nodes.

    Tracks nodes, accepts client requests, assigns work to nodes, receives
    completion notifications, and exposes request status/results to clients.
    This component does not access the filesystem.
    """

    def __init__(self):
        """Initialize node registry."""
        pass

    # Node registry
    def register_node(self, node_id: NODE_ID_FORMAT, address: NODE_ADDRESS_FORMAT) -> None:
        """Register a storage/compute node with its network address.
        
        Args:
            node_id: The identifier of the node.
            address: The network address of the node.
        """
        pass

    # Client registry
    def register_client(self, client_id: CLIENT_ID_FORMAT, address: CLIENT_ADDRESS_FORMAT) -> None:
        """Register a client with its network address.
        
        Args:
            client_id: The identifier of the client.
            address: The network address of the client.
        """
        pass

    # Request registry
    def register_request(self, request_id: REQUEST_ID_FORMAT, client_id: CLIENT_ID_FORMAT, work: WORK_FORMAT) -> None:
        """Register a request with its client and work specification.
        
        Args:
            request_id: The identifier of the request.
            client_id: The identifier of the client.
            work: The work for the request.
        """

    # Scheduling and node interaction
    def assign_next_work(self, node_id: NODE_ID_FORMAT) -> None:
        """Assign the next work to a node.
        
        Args:
            node_id: The identifier of the node.
        """
        pass

    def receive_node_completion(self, node_id: NODE_ID_FORMAT, request_id: REQUEST_ID_FORMAT) -> None:
        """Record completion reported by a node for a request.
        
        Args:
            node_id: The identifier of the node.
            request_id: The identifier of the request.
        """
        pass

    def send_receipt(self, request_id: REQUEST_ID_FORMAT) -> None:
        """Send receipt to client for a request.
        
        Args:
            request_id: The identifier of the request.
        """
        pass
