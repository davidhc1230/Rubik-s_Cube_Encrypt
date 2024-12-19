# 🧩 Rubik's Cube Encrypt

## 📌 Overview

Rubik's Cube Encrypt is a playful experiment inspired by the mechanics of a Rubik's Cube. This Python program provides a unique encryption tool based on dynamic row and column rotations, drawing parallels to the rotations of a cube. While modern encryption methods like AES or RSA are far more robust, this project is meant to foster creativity, problem-solving skills, and the discovery of personal blind spots.

⚠️ **Note:** This tool is not recommended for securing sensitive data. Instead, it serves as a fun exercise to think outside the box, learn by doing, and appreciate the complexities of encryption.

---

## 📌 Features

- **Dynamic Encryption**: Encrypts text files through multiple iterations of row and column rotations, combined with line-length offsets.
- **Customizable Iterations**: The number of encryption cycles is determined by the sum of the digits in the provided key.
- **Decryption Support**: Fully reversible process to restore the original content.
- **Lightweight and Easy to Use**: A simple tool for learning and experimentation.

---

## 📌 Workflow

1. **Input the Key**: Enter a numeric key (up to 12 digits). The sum of its digits determines the number of encryption iterations.
2. **Encrypt or Decrypt**: Choose between encryption or decryption operations.
3. **Output Files**:
   - Encrypted files are saved with the `.encrypted` extension.
   - Decrypted files are restored with the `.decrypted` extension.

---

## 📌 Environment Setup and Running Scripts

### 1. **Environment Setup**

* Ensure Python 3 or above is installed on your system.

### 2. **Run the Program**

Run the following command to start the tool:

```bash
python rubiks_cube_encrypt.py
```

Follow the prompts to input the file name, choose the operation, and provide the encryption key.

---

## 📌 File Structure

```
project/
├── rubiks_cube_encrypt.py    # Main script
└── sample.txt               # Example text file for testing
```

---

## 📌 Notes

- This tool is purely experimental and should not be used for production-level encryption.
- It is designed to inspire creative problem-solving and demonstrate the basics of custom encryption logic.
- For robust encryption, consider using well-established libraries like `cryptography` or `PyCrypto`.

---

## 📌 Version Information

### v1.0

Initial release includes:

- Encryption and decryption using row and column rotations.
- Iterative encryption cycles based on the key's numeric sum.
- Randomized decryption delays to mimic real-world decryption complexities.

