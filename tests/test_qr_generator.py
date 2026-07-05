import tempfile
from pathlib import Path
from qr_generator import generate_qr


def test_generate_qr_creates_file(tmp_path):
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    path = generate_qr(
        data="Hello World",
        filename="test_qr.png",
        box_size=4,
        border=2,
        fill_color="black",
        back_color="white",
        error_correction="M",
        output_dir=str(out_dir),
    )
    p = Path(path)
    assert p.exists()
    assert p.suffix == ".png"
