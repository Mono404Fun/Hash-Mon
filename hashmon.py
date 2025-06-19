import hashlib, colorama, pyfiglet, time
from tkinter import filedialog as fd

colorama.init()
CYAN = colorama.Fore.CYAN
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN

def print_banner():
    print(GREEN)
    print(pyfiglet.figlet_format("HASHMON", font="bloody"))
    print(f"{CYAN}Welcome to the advanced HASHMON utility, by Monoal.\nGithub: https://www.github.com/Mono404Fun! Don't forget to have fun ")

def hash_text(plain_text, algo):
    hash_dict = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1, 'sha224': hashlib.sha224, 'sha256': hashlib.sha256,
        'sha384': hashlib.sha384, 'sha512': hashlib.sha512, 'sha3_224': hashlib.sha3_224,
        'sha3_256': hashlib.sha3_256, 'sha3_384': hashlib.sha3_384, 'sha3_512': hashlib.sha3_512,
        'blake2b': hashlib.blake2b, 'blake2s': hashlib.blake2s,
        'shake_128': hashlib.shake_128, 'shake_256': hashlib.shake_256
    }
    return hash_dict[algo](plain_text).hexdigest()

def bruteforce_hash(user_hash, wordlist, algo):
    hash_dict = {
        'md5': hashlib.md5, 'sha1': hashlib.sha1, 'sha224': hashlib.sha224,
        'sha256': hashlib.sha256, 'sha384': hashlib.sha384, 'sha512': hashlib.sha512,
        'sha3_224': hashlib.sha3_224, 'sha3_256': hashlib.sha3_256, 'sha3_384': hashlib.sha3_384,
        'sha3_512': hashlib.sha3_512, 'blake2b': hashlib.blake2b, 'blake2s': hashlib.blake2s,
        'shake_128': hashlib.shake_128, 'shake_256': hashlib.shake_256
    }
    for line in wordlist:
        line = line.strip("\n").encode()
        calculated_hash = hash_dict[algo](line).hexdigest()
        if user_hash == calculated_hash:
            return line
    return None

def get_user_input(prompt, input_type=int, required=True, valid_range=None):
    while True:
        try:
            user_input = input(prompt)
            if required and not user_input:
                raise ValueError("Input cannot be empty.")
            user_input = input_type(user_input)
            if valid_range and user_input not in valid_range:
                raise ValueError(f"Input must be in range {valid_range}.")
            return user_input
        except ValueError as e:
            print(f"{RED}Error: {e}. Please try again.{CYAN}")

def get_hash_description(algo):
    descriptions = {
        'md5': "MD5 (Message-Digest Algorithm 5) is a widely used hash function producing a 128-bit hash value.",
        'sha1': "SHA-1 (Secure Hash Algorithm 1) is a cryptographic hash function producing a 160-bit hash value.",
        'sha224': "SHA-224 is a truncated version of SHA-256, producing a 224-bit hash value.",
        'sha256': "SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function producing a 256-bit hash value.",
        'sha384': "SHA-384 is a truncated version of SHA-512, producing a 384-bit hash value.",
        'sha512': "SHA-512 (Secure Hash Algorithm 512-bit) is a cryptographic hash function producing a 512-bit hash value.",
        'sha3_224': "SHA-3-224 is a member of the SHA-3 family, producing a 224-bit hash value.",
        'sha3_256': "SHA-3-256 is a member of the SHA-3 family, producing a 256-bit hash value.",
        'sha3_384': "SHA-3-384 is a member of the SHA-3 family, producing a 384-bit hash value.",
        'sha3_512': "SHA-3-512 is a member of the SHA-3 family, producing a 512-bit hash value.",
        'blake2b': "BLAKE2b is a cryptographic hash function optimized for 64-bit platforms, producing a variable-length hash value.",
        'blake2s': "BLAKE2s is a cryptographic hash function optimized for 32-bit platforms, producing a variable-length hash value.",
        'shake_128': "SHAKE-128 is an extendable-output function (XOF) from the SHA-3 family, producing a variable-length hash value.",
        'shake_256': "SHAKE-256 is an extendable-output function (XOF) from the SHA-3 family, producing a variable-length hash value."
    }
    return descriptions.get(algo, "No description available.")

print_banner()

hash_options = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 
                'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 
                'blake2b', 'blake2s', 'shake_128', 'shake_256']

while True:
    time.sleep(2)
    print("\n#################################################################################################\n")
    print(f"""{GREEN}
1> Convert plain text to hash <Hashing>
2> Convert hash to plain text <BruteForcing>
    """)
    operation_choice = get_user_input("> Choose an option from the list [Ex: 1] >>> ", valid_range=range(1, 3))

    if operation_choice == 1:
        input_text = input("\t> Enter plain text [Ex: Hello, world!] >>> ").encode()
        if not input_text:
            print(f"{RED}Error: Plain text cannot be empty. Please try again.{CYAN}")
            continue
        print(f"""{GREEN}
\tHashing Options:
\t\t1> Convert plain text to MD5 hash
\t\t2> Convert plain text to SHA-1 hash
\t\t3> Convert plain text to SHA-224 hash
\t\t4> Convert plain text to SHA-256 hash
\t\t5> Convert plain text to SHA-384 hash
\t\t6> Convert plain text to SHA-512 hash
\t\t7> Convert plain text to SHA-3-224 hash
\t\t8> Convert plain text to SHA-3-256 hash
\t\t9> Convert plain text to SHA-3-384 hash
\t\t10> Convert plain text to SHA-3-512 hash
\t\t11> Convert plain text to BLAKE2b hash
\t\t12> Convert plain text to BLAKE2s hash
\t\t13> Convert plain text to SHAKE-128 hash
\t\t14> Convert plain text to SHAKE-256 hash
        """)
        hash_algo_choice = get_user_input("\t> Choose an option from the list >>> ", valid_range=range(1, 15))
        selected_algo = hash_options[hash_algo_choice - 1]
        start_time = time.time()
        calculated_hash = hash_text(input_text, selected_algo)
        end_time = time.time()
        hash_length = len(calculated_hash)
        execution_time = end_time - start_time
        description = get_hash_description(selected_algo)
        print(f"{RED}\t> Hash: {calculated_hash}")
        print(f"{RED}\t> Hash Length: {hash_length} characters")
        print(f"{RED}\t> Execution Time: {execution_time:.4f} seconds")
        print(f"{RED}\t> Algorithm Description: {description}")
        input("\t> Press Enter to exit...")

    elif operation_choice == 2:
        input("\t> Press Enter to open a wordlist...")
        wordlist_file = fd.askopenfile(
            title="Open a Wordlist",
            filetypes=(("Text File", "*.txt"),)
        )
        if not wordlist_file:
            print(f"{RED}Error: No file selected. Please try again.{CYAN}")
            continue
        wordlist_path = wordlist_file.name
        if wordlist_path:
            with open(wordlist_path, "r") as f:
                wordlist = f.readlines()
            user_hash = input("\t> Enter hash [Ex: 6cd3556deb0da54bca060b4c39479839] >>> ")
            if not user_hash:
                print(f"{RED}Error: Hash cannot be empty. Please try again.{CYAN}")
                continue
            print(f"""{GREEN}
\tBruteForcing Options:
\t\t1> Bruteforce MD5 hash
\t\t2> Bruteforce SHA-1 hash
\t\t3> Bruteforce SHA-224 hash
\t\t4> Bruteforce SHA-256 hash
\t\t5> Bruteforce SHA-384 hash
\t\t6> Bruteforce SHA-512 hash
\t\t7> Bruteforce SHA-3-224 hash
\t\t8> Bruteforce SHA-3-256 hash
\t\t9> Bruteforce SHA-3-384 hash
\t\t10> Bruteforce SHA-3-512 hash
\t\t11> Bruteforce BLAKE2b hash
\t\t12> Bruteforce BLAKE2s hash
\t\t13> Bruteforce SHAKE-128 hash
\t\t14> Bruteforce SHAKE-256 hash
            """)
            brute_force_algo_choice = get_user_input("\t> Choose an option from the list >>> ", valid_range=range(1, 15))
            selected_algo = hash_options[brute_force_algo_choice - 1]
            start_time = time.time()
            found_value = bruteforce_hash(user_hash, wordlist, selected_algo)
            end_time = time.time()
            execution_time = end_time - start_time
            if found_value:
                print(f"{RED}\t> Hash value found: {found_value.decode()}")
                print(f"{RED}\t> Execution Time: {execution_time:.4f} seconds")
                input("\t> Press Enter to exit...")
            else:
                print(f"{RED}\t> We didn't find the value of the hash {user_hash}")
        else:
            continue