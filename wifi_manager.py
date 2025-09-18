import subprocess
import re
from cryptography.fernet import Fernet
import base64
import hashlib
from getpass import getpass

# Function to generate a Fernet key from a password
def generate_key_from_password(password: str) -> bytes:
    # Convert password into a SHA256 hash, then make it URL-safe for Fernet
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

# Function to extract Wi-Fi SSIDs and passwords
def extract_wifi_passwords():
    wifi_list = []
    try:
        # Get all Wi-Fi profiles
        profiles = subprocess.check_output("netsh wlan show profiles", shell=True).decode(errors="ignore")
        profiles = re.findall("All User Profile     : (.*)", profiles)

        for profile in profiles:
            try:
                # Get Wi-Fi details including password
                profile = profile.strip()
                details = subprocess.check_output(f"netsh wlan show profile name=\"{profile}\" key=clear", shell=True).decode(errors="ignore")
                password = re.search("Key Content            : (.*)", details)
                password = password.group(1) if password else "N/A"
                wifi_list.append(f"SSID: {profile}| Password: {password}")
            except:
                continue
    except Exception as e:
        print(f"Error: {e}")
    return "\n".join(wifi_list)

# Encrypt Wi-Fi passwords and save
def encrypt_and_save(password: str):
    key = generate_key_from_password(password)
    fernet = Fernet(key)

    wifi_data = extract_wifi_passwords()
    encrypted_data = fernet.encrypt(wifi_data.encode())

    with open("wifi_passwords.enc", "wb") as file:
        file.write(encrypted_data)

    print("✅ Wi-Fi passwords encrypted and saved in 'wifi_passwords.enc'")

# Decrypt Wi-Fi passwords and show
def decrypt_and_show(password: str):
    try:
        key = generate_key_from_password(password)
        fernet = Fernet(key)

        with open("wifi_passwords.enc", "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data).decode()
        print("\n📂 Decrypted Wi-Fi Passwords:\n")
        print(decrypted_data)
    except Exception:
        print("❌ Wrong password or corrupted file!")

# Main program
def main():
    print("🔐 Wi-Fi Password Manager ---")
    print("1. Extract & Encrypt Wi-Fi Passwords")
    print("2. Decrypt Saved Wi-Fi Passwords")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        master_pass = getpass("Set a master password: ")
        encrypt_and_save(master_pass)
    elif choice == "2":
        master_pass = getpass("Enter your master password: ")
        decrypt_and_show(master_pass)
    else:
        print("❌ Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()
