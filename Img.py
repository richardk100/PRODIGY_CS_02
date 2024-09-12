from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    # Convert the image into a NumPy array
    image_array = np.array(image)
    
    # Encrypt by XORing each pixel with the key
    encrypted_array = image_array ^ key
    
    # Convert the array back to an image
    encrypted_image = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'")

# Function to decrypt the image
def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    # Convert the image into a NumPy array
    encrypted_array = np.array(encrypted_image)
    
    # Decrypt by XORing again with the same key (XOR is reversible)
    decrypted_array = encrypted_array ^ key
    
    # Convert the array back to an image
    decrypted_image = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'")

# Main function to run encryption and decryption
if __name__ == "__main__":
    # Image file path
    image_path = r"C:\Users\admin\Desktop\Image_Encryption\philip-oroni-CrJGbb7kzU4-unsplash.jpg"  
    key = 42  # Simple numeric key for XOR encryption
    
    # Encrypt the image
    encrypt_image(image_path, key)
    
    # Decrypt the image
    decrypt_image("encrypted_image.png", key)




