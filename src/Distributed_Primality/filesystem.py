from Distributed_Primality import PATH_FORMAT, DATA_FORMAT

class AFSFilesystem:
    """Filesystem for AFS (v1)."""

    def __init__(self):
        """Initialize filesystem."""
        pass

    def open_file(self, path: PATH_FORMAT) -> None:
        """Open a file at the specified path."""
        pass

    def create_file(self, path: PATH_FORMAT) -> None:
        """Create an empty file at the specified path."""
        pass

    def write_file(self, path: PATH_FORMAT, data: DATA_FORMAT) -> None:
        """Write data to file at the specified path."""
        pass

    def read_file(self, path: PATH_FORMAT) -> DATA_FORMAT:
        """Read the contents of the file at the specified path."""
        pass

    def close_file(self, path: PATH_FORMAT) -> None:
        """Close the file at the specified path."""
        pass
