import hashlib
from dataclasses import dataclass
from pathlib import Path

from yparser.src.pool import Pool, PoolInstance


@dataclass
class HashResult:
    """MD5 hash of a file."""

    path: Path
    digest: str


class Hasher(PoolInstance):
    """Worker that calculates file hashes."""

    def __init__(self, input_queue, output_queue=None, logger_queue=None):
        super().__init__(input_queue, output_queue, logger_queue)

    def run_func(self, path: str) -> HashResult | None:
        file_path = Path(path)
        if not file_path.is_file():
            return None
        md5 = hashlib.md5()
        with file_path.open('rb') as f:
            for chunk in iter(lambda: f.read(8192), b""):
                md5.update(chunk)
        result = HashResult(path=file_path, digest=md5.hexdigest())
        return result


class HasherPool(Pool):
    def __init__(self, n_workers: int, output_queue=None):
        super().__init__(
            pool_instance=Hasher,
            n_workers=n_workers,
            output_queue=output_queue,
        )
