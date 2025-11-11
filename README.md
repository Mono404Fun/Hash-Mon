# 🛡️ HASHMON — The Python utility for hashing and bruteforcing](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?logo=windows)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)
![Made with ❤️](https://img.shields.io/badge/Made%20by-Monoal-blueviolet)

> **HASHMON** is a clean, interactive, and powerful Python tool designed for **cryptographic hashing** and **hash reverse engineering (bruteforce cracking)** — all from a user-friendly terminal interface.  
> With support for a wide range of industry-standard hash algorithms, it delivers both educational value and practical utility for cybersecurity learners, enthusiasts, and developers.

---

## ✨ Features at a Glance

- 🔐 **Hash Text Instantly**  
  Supports MD5, SHA1, SHA2, SHA3, BLAKE2, and SHAKE families.

- 🔍 **Reverse Hashes with Wordlists**  
  Crack known hashes using your own wordlist and algorithm of choice.

- ⚙️ **Fully Interactive CLI Interface**  
  Clean menu system, colored output, ASCII banners, and error handling.

- 🧪 **Fast and Lightweight**  
  No bloated frameworks. Pure Python and standard libraries (plus a touch of `colorama` and `pyfiglet`).

- 🧠 **Educational Purpose**  
  Learn how hashing and cracking work under the hood.

- 📦 **Single-File Simplicity**  
  One `.py` file. Drop it anywhere and run.

---

## 🚀 Introduction

**HASHMON** (Hash Monitor) was built to simplify the process of generating and analyzing cryptographic hashes in a beautiful and interactive way.

Whether you're:

- a **student** learning about cybersecurity,
- a **developer** validating checksums,
- or a **hacker** testing your wordlists,

HASHMON gives you full control with a minimal and professional design.

🔗 **GitHub**: [github.com/Mono404Fun](https://github.com/Mono404Fun)  
🧪 **Language**: Python 3  
📁 **File count**: One. Just one.

---

## 🔧 Installation & Requirements

HASHMON is a Python-based terminal utility. You only need Python 3.8+ and a few lightweight libraries to get started.

### ✅ Requirements

- Python **3.8 or higher**
- Required modules:
  - `colorama`
  - `pyfiglet`
  - `tkinter` *(comes built-in with most Python installations)*

---

### ⚙️ Install Dependencies

Use `pip` to install the required modules:

```bash
pip install colorama pyfiglet
```

> ⚠️ Make sure Tkinter is installed and working on your system.
> On some Linux distros, you may need to install it manually:

```bash
sudo apt install python3-tk
```

### 📥 Clone & Run
```bash
git clone https://github.com/Mono404Fun/HASHMON.git
cd HASHMON
python hashmon.py
```

That's it. You're ready to go. 💥

## 🚦 Usage & Features

HASHMON is fully interactive — just run it in your terminal and follow the prompts.  
It offers two major features:

---

### 1️⃣ Convert Plain Text to Hash

Choose this option to convert any string into a cryptographic hash using your selected algorithm.

#### 🔤 Example:
```shell
Choose an option from the list [Ex: 1] >>> 1
Enter plain text [Ex: Hello, world!] >>> password123
Choose a hashing algorithm >>> SHA-256
```

#### 🔎 Output:
```shell
Hash: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
Hash Length: 64 characters
Execution Time: 0.0002 seconds
Algorithm Description: SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function producing a 256-bit hash value.
```


---

### 2️⃣ Bruteforce a Hash using Wordlist

Choose this option to attempt reversing a hash by comparing it against a wordlist.

#### 📂 Steps:
- Open a wordlist (`.txt`) using the file browser
- Enter the hash to crack
- Select the corresponding hashing algorithm

#### 🔤 Example:
```shell
Choose an option from the list [Ex: 2] >>> 2
Open a wordlist file...
Enter hash >>> 482c811da5d5b4bc6d497ffa98491e38
Choose algorithm >>> MD5
```

#### ✅ Output:
```shell
Hash value found: password123
Execution Time: 0.0124 seconds
```


> ❌ If not found, HASHMON will notify you that the value doesn't exist in the wordlist.

---

All output is color-coded and clear — optimized for fast use, readability, and fun.

## 🔐 Supported Hashing Algorithms

HASHMON supports a wide variety of modern and legacy cryptographic hash algorithms.  
Each one comes with a built-in description for better understanding.

| Algorithm     | Description                                                                                      |
|---------------|--------------------------------------------------------------------------------------------------|
| **MD5**       | Message-Digest Algorithm 5. Produces a 128-bit hash. Common but cryptographically broken.       |
| **SHA-1**     | Secure Hash Algorithm 1. Produces a 160-bit hash. No longer considered secure for cryptography. |
| **SHA-224**   | Truncated version of SHA-256, outputs a 224-bit hash.                                            |
| **SHA-256**   | Industry-standard 256-bit cryptographic hash. Strong and widely used.                           |
| **SHA-384**   | Truncated version of SHA-512, optimized for 384-bit output.                                     |
| **SHA-512**   | High-strength 512-bit secure hash.                                                               |
| **SHA3-224**  | Member of the SHA-3 family, outputs 224-bit hash.                                                |
| **SHA3-256**  | Secure 256-bit hash from the SHA-3 family.                                                       |
| **SHA3-384**  | SHA-3 variant producing a 384-bit hash.                                                          |
| **SHA3-512**  | Strong 512-bit SHA-3 algorithm.                                                                  |
| **BLAKE2b**   | Optimized for 64-bit platforms. Very fast and secure.                                            |
| **BLAKE2s**   | Optimized for 32-bit platforms. Compact and secure.                                              |
| **SHAKE-128** | Extendable-output function (XOF). Outputs variable-length hashes.                               |
| **SHAKE-256** | Stronger XOF version. Variable-length and highly flexible.                                       |

> 📚 Need details while running? HASHMON displays the full description of your selected algorithm during execution.

## 📸 Screenshots / Demo

Here’s a quick look at how HASHMON looks in action:

### Text Hashing Example
![Screenshot (22)](https://github.com/user-attachments/assets/ca1a5559-6acc-4cb7-8f8b-1788c94a0b33)

---

### Hash BruteForcing Example
![Screenshot (25)](https://github.com/user-attachments/assets/de0ca76a-a20d-4044-8726-dcd7d30a198c)

#### This is the WordList file "wordlist.txt":

![Screenshot (26)](https://github.com/user-attachments/assets/a1217020-8cf1-4b6b-91fe-87d0d93a3782)

---
