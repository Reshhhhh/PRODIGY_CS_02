from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            encrypted_pixel = (b, g, r)
            pixels[i, j] = encrypted_pixel
    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            decrypted_pixel = (b, g, r)
            pixels[i, j] = decrypted_pixel
    img.save(output_path)
    print("Image decrypted successfully!")


print("IMAGE ENCRYPTION AND DECRYPTION")
input_image = input("Enter the absolute file location: ")
encrypted_image = input("Enter the absolute file loaction that the encrypted image should be stored: ")
decrypted_image = input("Enter the absolute file location that the decrypted image should be stored: ")

encrypt_image(input_image, encrypted_image, key=None)
decrypt_image(encrypted_image, decrypted_image, key=None)
