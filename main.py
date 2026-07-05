from validator import validate_nonempty, validate_url, validate_email, validate_phone
from qr_generator import generate_qr
from utils import ensure_output_dir, make_filename


def menu():
    print("===========================")
    print(" QR Code Generator")
    print("===========================")
    print("1. Text QR")
    print("2. Website QR")
    print("3. Email QR")
    print("4. Phone QR")
    print("5. Wi-Fi QR")
    print("6. Exit")


def main():
    ensure_output_dir()
    while True:
        menu()
        choice = input("Enter Choice: ").strip()
        if choice == "1":
            data = input("Enter text: ").strip()
            if not validate_nonempty(data):
                print("Input cannot be empty")
                continue
        elif choice == "2":
            data = input("Enter website URL: ").strip()
            if not validate_url(data):
                print("Invalid URL")
                continue
        elif choice == "3":
            email = input("Enter email address: ").strip()
            if not validate_email(email):
                print("Invalid email")
                continue
            subject = input("(optional) Subject: ").strip()
            body = input("(optional) Body: ").strip()
            data = f"mailto:{email}?subject={subject}&body={body}"
        elif choice == "4":
            phone = input("Enter phone number (with country code): ").strip()
            if not validate_phone(phone):
                print("Invalid phone number")
                continue
            data = f"tel:{phone}"
        elif choice == "5":
            ssid = input("SSID: ").strip()
            if not validate_nonempty(ssid):
                print("SSID cannot be empty")
                continue
            auth = input("Auth (WPA/WEP/nopass): ").strip() or "WPA"
            password = "" if auth.lower() == "nopass" else input("Password: ").strip()
            hidden = input("Hidden? (y/N): ").strip().lower() == "y"
            hidden_flag = "true" if hidden else "false"
            data = f"WIFI:T:{auth};S:{ssid};P:{password};H:{hidden_flag};"
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
            continue

        filename = input("Custom filename (leave blank to auto-generate): ").strip()
        if not filename:
            filename = make_filename()

        box_size = input("Box size (default 10): ").strip() or "10"
        border = input("Border (default 4): ").strip() or "4"
        fill = input("Fill color (default black): ").strip() or "black"
        back = input("Background color (default white): ").strip() or "white"
        ec = input("Error correction (L/M/Q/H) (default M): ").strip().upper() or "M"

        try:
            out_path = generate_qr(
                data,
                filename=filename,
                box_size=int(box_size),
                border=int(border),
                fill_color=fill,
                back_color=back,
                error_correction=ec,
            )
            print("QR Successfully Generated")
            print(f"Saved As: {out_path}")
        except Exception as e:
            print("Failed to generate QR:", e)


if __name__ == "__main__":
    main()
