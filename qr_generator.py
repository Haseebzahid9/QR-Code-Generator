import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H
from pathlib import Path


EC_MAP = {
    "L": ERROR_CORRECT_L,
    "M": ERROR_CORRECT_M,
    "Q": ERROR_CORRECT_Q,
    "H": ERROR_CORRECT_H,
}


def generate_qr(data, filename="qr.png", box_size=10, border=4, fill_color="black", back_color="white", error_correction="M", output_dir="output"):
    """Generate and save a QR code image. Returns the saved path."""
    ec = EC_MAP.get(error_correction.upper(), None)
    if ec is None:
        raise ValueError("Invalid error correction level. Choose from L/M/Q/H")

    qr = qrcode.QRCode(
        version=None,
        error_correction=ec,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    path = out_dir / f"{filename if filename.lower().endswith('.png') else filename + '.png'}"
    img.save(path)
    return str(path)
