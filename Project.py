import qrcode
import base64
from io import BytesIO
from PIL import Image

from AdvancedEncryptionStandards import encryption, decryption


def generate_qr_code(data, name):
    qr = qrcode.QRCode(version=1, box_size=12)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(name)


def image_to_string(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string


def string_to_image(encoded_string, new_name):
    decoded_bytes = base64.b64decode(encoded_string)
    with open(new_name, "wb") as image_file:
        image_file.write(decoded_bytes)


def main():
    secret_text = input("Enter the secret text: ")
    deceptive_text = input("Enter the deceptive text: ")
    key = input("Enter the secret encryption key: ")

    # Encrypt the secret text
    cipher_text = encryption(secret_text, key).lower()
    print("\nThe cipher text is:", cipher_text, "\n")

    # Generate QR code for deceptive text
    generate_qr_code(deceptive_text, "WithoutSecretText.png")

    # Read QR code image and convert it to a string
    qr_image_string = image_to_string("WithoutSecretText.png")

    # Embed the secret cipher text into the QR code data
    modified_qr_image_string = qr_image_string[:-32] + cipher_text + qr_image_string[-32:]

    # Create a new QR code image with the embedded secret text
    string_to_image(modified_qr_image_string, "WithSecretText.png")
    print("\n\n----Image with the secret text has been created and sent to the receiver.----\n\n")

    # Receiver receives the image and decodes the QR code
    new_qr_image_string = image_to_string("WithSecretText.png")
    print("The new QR image as decoded by the receiver is:", new_qr_image_string, "\n")

    # Receiver extracts the hidden cipher text from the QR code and decrypts it
    cipher = new_qr_image_string[-len(cipher_text) - 32:-32].upper()
    plaintext = decryption(cipher, key)
    print("The plain text received by the receiver is:", plaintext, "\n")


if __name__ == "__main__":
    main()
