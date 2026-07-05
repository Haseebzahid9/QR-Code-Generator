from pathlib import Path
from datetime import datetime


def ensure_output_dir(path: str = "output"):
    Path(path).mkdir(parents=True, exist_ok=True)


def make_filename(prefix: str = "qr") -> str:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{ts}.png"
