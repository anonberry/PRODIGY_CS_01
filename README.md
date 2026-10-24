# PRODIGY_CS_01
# Caesar Cipher in Python 🔐

## 📌 Project Overview

This project implements the **Caesar Cipher**, a simple encryption and decryption algorithm written in Python. It allows users to enter a message, specify a shift value, and choose whether to encrypt or decrypt the message.

The Caesar Cipher works by shifting each letter of the alphabet by a fixed number of positions while preserving uppercase and lowercase letters, spaces, numbers, and special characters.

This project was developed as a beginner-friendly exercise in Python programming and basic cryptography.

## 🎯 Objectives

- Understand the fundamentals of encryption and decryption.
- Implement the Caesar Cipher algorithm using Python.
- Practise functions, loops, conditional statements, and user input.
- Handle uppercase and lowercase letters.
- Preserve spaces, numbers, and special characters.
- Allow users to encrypt and decrypt messages interactively.

## ⚙️ Features

- **Message Encryption:** Converts plaintext into ciphertext using a specified shift.
- **Message Decryption:** Recovers the original message using the same shift value.
- **Custom Shift Value:** Allows users to choose their preferred shift.
- **Case Preservation:** Maintains uppercase and lowercase letters.
- **Character Preservation:** Leaves spaces, numbers, and special characters unchanged.
- **Input Validation:** Handles invalid operation choices.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** Functions, loops, conditionals, strings, ASCII/Unicode character conversion, and modular arithmetic.

## 📂 Project Structure

```text
PRODIGY_CS_01/
├── Caesar Cipher.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Install Python 3 on your computer.

Check your Python installation:

```bash
python --version
```

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/anonberry/PRODIGY_CS_01
   ```

2. Navigate to the project directory:

   ```bash
   cd PRODIGY_CS_01
   ```

3. Run the Python program:

   ```bash
   python "Caesar Cipher.py"
   ```


## 💻 Usage

When you run the program, you will be prompted to enter a message, a shift value, and an operation.

### Example 1: Encryption

**Input:**

```text
Enter your message: HELLO WORLD
Enter shift value: 3
Enter E to encrypt or D to decrypt: E
```

**Output:**

```text
Encrypted message: KHOOR ZRUOG
```

### Example 2: Decryption

**Input:**

```text
Enter your message: KHOOR ZRUOG
Enter shift value: 3
Enter E to encrypt or D to decrypt: D
```

**Output:**

```text
Decrypted message: HELLO WORLD
```

## 🧠 How It Works

The Caesar Cipher shifts each letter forward or backward through the alphabet.

For encryption, the formula is:

```text
E(x) = (x + shift) mod 26
```

For decryption, the formula is:

```text
D(x) = (x - shift) mod 26
```

The modulo operation ensures that letters wrap around the alphabet. For example, shifting `Z` forward by three positions produces `C`.

The program uses Python's `ord()` and `chr()` functions to convert characters to numerical values and back again.

## 🔒 Security Considerations

The Caesar Cipher is a classical substitution cipher intended for educational purposes. It is **not secure for protecting sensitive information** because its small key space makes it easy to break using brute force or frequency analysis.

This project demonstrates basic cryptographic concepts rather than modern, secure encryption.

## 📚 Learning Outcomes

Through this project, I practised:

- Implementing a classical encryption algorithm.
- Writing reusable Python functions.
- Manipulating strings and characters.
- Applying modular arithmetic.
- Handling user input and basic validation.
- Understanding the difference between classical ciphers and modern cryptography.

## 👤 Author


GitHub: [@anonberry](https://github.com/anonberry)

## 📄 License

This project is available for educational and learning purposes under the MIT License.
