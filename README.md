# Wifi-Manager
 Wi-Fi Password Manager built with Python — extract, encrypt, and securely manage your saved Wi-Fi credentials.
:

🔐 Wi-Fi Password Extractor with Encryption (Python)

This project extracts saved Wi-Fi SSIDs and passwords from a Windows system, then securely encrypts them using a master password. The same password must be entered later to decrypt and view the Wi-Fi details.

⚙️ Features

✅ Extracts all saved Wi-Fi SSIDs & passwords (Windows only).

✅ Encrypts results with a master password (no external key file needed).

✅ Decrypts only if the correct master password is entered.

✅ Provides security & privacy by preventing unauthorized access.

📂 How It Works

Run the program

python wifi_manager.py


Choose an option:

1 → Extract & Encrypt Wi-Fi Passwords

2 → Decrypt Saved Wi-Fi Passwords

When encrypting → set a master password in the terminal.

When decrypting → re-enter the same password to unlock.

🛠️ Tech Used

Python (subprocess, regex, cryptography, getpass)

Networking Basics (Wi-Fi profiles, SSID, saved credentials)

Encryption (symmetric password-based key generation)

📌 Learning Outcome

Improved understanding of network security & automation.

Learned to implement password-based encryption in Python.

Practiced secure coding and real-world network data handling.

🚀 Example Output
Wi-Fi Password Manager ---
1. Extract & Encrypt Wi-Fi Passwords
2. Decrypt Saved Wi-Fi Passwords
Enter your choice (1/2): 1

✅ Wi-Fi passwords encrypted and saved in 'wifi_passwords.enc'

Enter password to decrypt file: ********
SSID: MyWiFi, Password: hello1234
SSID: OfficeWiFi, Password: N/A

🔑 Note

Works only on Windows (uses netsh command).

Saved passwords remain secure unless decrypted with the correct master password.
