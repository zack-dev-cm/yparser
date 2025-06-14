from queue import Queue
from yparser.src.cleaner.hasher import HasherPool, HashResult


class Cleaner:
    """Utility class for running hashing workers."""

    def __init__(self, n_workers: int = 1):
        self.output_queue: Queue = Queue()
        self.hasher_pool = HasherPool(
            n_workers=n_workers,
            output_queue=self.output_queue,
        )

    def hash_files(self, paths: list[str]) -> list[HashResult]:
        """Compute MD5 hashes for the given file paths."""
        for path in paths:
            self.hasher_pool.input_queue.put(path)
        self.hasher_pool.input_queue.join()
        results = []
        while not self.output_queue.empty():
            results.append(self.output_queue.get())
        return results
