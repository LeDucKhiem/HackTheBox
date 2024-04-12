import os
from pwn import xor

def decrypt_file(filename,output_filename, key):
    with open(filename, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = xor(encrypted_data, key)
    with open(output_filename, "wb") as f:
        f.write(decrypted_data)

def main():
    key = b'bhUlIshutrea98liOp'
    folder = input("Enter a folder to decrypt: ")
    while len(folder) < 0:
        continue
    try:
        output_folder = input("Enter folder to write decrypted files: ")
        if len(output_folder) < 1:
            output_folder = "./decrypted_files"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        for filename in os.listdir(folder):
            if filename.endswith(".24bes"):  
                input_file_path = os.path.join(folder, filename)
                output_file_path = os.path.join(output_folder, filename.replace('.24bes', ''))
                decrypt_file(input_file_path, output_file_path, key)
        print("[+] Decrypt files finished!!!")
    except:
        print("[-] Can't open or create a folder")
        exit(1)
      
if __name__ == '__main__':
    main()
