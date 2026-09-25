import time

class SystemLogger:
    def __init__(self, prefix: str = "SYS"):
        self.prefix = prefix

    def _timestamp(self) -> str:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    def info(self, message: str) -> None:
        print(f"[{self._timestamp()}] [{self.prefix}] [INFO]: {message}")

    def warn(self, message: str) -> None:
        print(f"[{self._timestamp()}] [{self.prefix}] [WARN]: {message}")

logger = SystemLogger(prefix="AUTH")