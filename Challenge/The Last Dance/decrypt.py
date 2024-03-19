from pwn import xor

def readData():
    with open("out.txt", "r") as f:
        data = f.read().splitlines()
        encrypted_message = bytes.fromhex(data[1])
        encrypted_flag = bytes.fromhex(data[2])
    return encrypted_message, encrypted_flag

def main():
    message = b"Our counter agencies have intercepted your messages and a lot "
    message += b"of your agent's identities have been exposed. In a matter of "
    message += b"days all of them will be captured"
    encrypted_message, encrypted_flag = readData()
    #flag = encrypted_message xor encrypted_flag xor message
    flag = xor(encrypted_flag, encrypted_message, message)
    print("FLAG:", flag)

if __name__ == "__main__":
    main()
