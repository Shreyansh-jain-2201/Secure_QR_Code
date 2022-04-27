import qrcode
import numpy as np
from PIL import Image
import base64
from io import BytesIO
from AdvancedEncryptionStandards import encryption, decryption



def QRencode(DeceptiveText, name):
    # Name of the QR code Image file
    qr = qrcode.QRCode(version=1, box_size=12)
    # add data to the QR code
    qr.add_data(DeceptiveText)
    # compile the data into a QR code array
    qr.make()
    image = qr.make_image()
    image.save(name)


def ImageToString(name):
    # converts qr image to utf-8 string
    with open(name, "rb") as image2string:
        return(base64.standard_b64encode(image2string.read()).decode("utf-8"))

def StringToImage(byte, newName):
    # Opens the image from the byte array
    decodeit = open(newName, 'wb')
    # Writes the byte array to the image
    decodeit.write(base64.standard_b64decode(byte))
    decodeit.close()


# main function
def main():

    SecretText = input("Enter the secret text: ")
    DeceptiveText = input("Enter the deceptive text: ")
    Key = input("Enter the secret key: ")
    # Name of the QR code Image file
    name = input("Enter the name of the orginal QRimage without secret text: ")
    # Name of the QR code Image file after hiding secret text
    newName = input("Enter the name of the new QRimage with secret text: ")

    # Encrypting the text
    # Generates the cipher text

    cipherText = encryption(SecretText, Key).lower()
    print("\n\n")
    print("The cipher text is: ", cipherText, "\n")
    print("\n")

    # Encoding the Deceptive text onto a QR code
    QRencode(DeceptiveText, name)

    # Reading the QR code image
    qrImage = ImageToString(name)

    # Hiding the secret cipher text into the QR code data
    qrImage = qrImage[0:-32] + cipherText + qrImage[-32:]

    # Creating a new QR code image with the hidden text
    byte = bytes(qrImage, 'utf-8')
    StringToImage(byte, newName)
    print("\n\n----Image with the secret text has been created and sent to the reciever.----\n\n")

    # Reciever recieves the image reads the QR code
    newQrImage = ImageToString(newName)
    print("The new QR image as decoded by the reciever is: ", newQrImage)
    print("\n")
    
    # Reciever obtains the hidden text ciphertext from the QR code and decrypts it
    cipher = newQrImage[-len(cipherText)-32:-32].upper()
    plaintext = decryption(cipher, Key)
    print("\n")
    print("The plain text recieved by the reciever is: ", plaintext, "\n")

if __name__ == "__main__":
    main()
