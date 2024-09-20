import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog, simpledialog
import numpy as np
import os


def read_input(file_path):
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
            return None
    else:
        messagebox.showerror("Error", "File not found.")
        return None


def vigenere_encrypt(plaintext, key):
    key = key.lower()
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('a')
            encrypted_char = chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a'))
            ciphertext += encrypted_char.upper() if char.isupper() else encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    key = key.lower()
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('a')
            decrypted_char = chr(((ord(char.lower()) - ord('a') - shift) % 26) + ord('a'))
            plaintext += decrypted_char.upper() if char.isupper() else decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    return plaintext


def generate_playfair_matrix(key):
    key = key.lower().replace('j', 'i')
    matrix = []
    for char in key + "abcdefghiklmnopqrstuvwxyz":
        if char not in matrix and char.isalpha():
            matrix.append(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    print(f"Character '{char}' not found in matrix: {matrix}")
    return None


def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = plaintext.lower().replace("j", "i").replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += 'x'
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        row1, col1 = find_position(matrix, plaintext[i])
        row2, col2 = find_position(matrix, plaintext[i + 1])

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext


def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_position(matrix, ciphertext[i])
        row2, col2 = find_position(matrix, ciphertext[i + 1])

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]

    return plaintext


def hill_encrypt(plaintext, key_matrix):
    plaintext_words = plaintext.lower().replace(" ", "")
    vector_size = len(key_matrix)

    if len(plaintext_words) % vector_size != 0:
        plaintext_words += 'x' * (vector_size - len(plaintext_words) % vector_size)

    plaintext_vector = [ord(char) - ord('a') for char in plaintext_words]
    ciphertext = ""

    for i in range(0, len(plaintext_vector), vector_size):
        chunk = plaintext_vector[i:i + vector_size]
        encrypted_chunk = np.dot(key_matrix, chunk) % 26
        ciphertext += ''.join(chr(num + ord('a')) for num in encrypted_chunk)

    return ' '.join([ciphertext[i:i + vector_size] for i in range(0, len(ciphertext), vector_size)])


def hill_decrypt(ciphertext, key_matrix):
    ciphertext_words = ciphertext.replace(" ", "")
    determinant = int(np.round(np.linalg.det(key_matrix)))
    inv_determinant = pow(determinant, -1, 26)
    adjugate_matrix = np.round(np.linalg.inv(key_matrix) * determinant).astype(int) % 26
    inv_key_matrix = (inv_determinant * adjugate_matrix) % 26

    ciphertext_vector = [ord(char) - ord('a') for char in ciphertext_words]
    plaintext = ""

    for i in range(0, len(ciphertext_vector), len(key_matrix)):
        chunk = ciphertext_vector[i:i + len(key_matrix)]
        decrypted_chunk = np.dot(inv_key_matrix, chunk) % 26
        plaintext += ''.join(chr(int(num) + ord('a')) for num in decrypted_chunk)

    return plaintext.replace('x', '')

class CryptographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Cipher Kriptografi")

        main_frame = tk.Frame(root, padx=10, pady=10)
        main_frame.pack(padx=10, pady=10)

        tk.Label(main_frame, text="Pilih Cipher:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W)
        self.cipher_var = tk.StringVar(value="vigenere")
        tk.Radiobutton(main_frame, text="Vigenere", variable=self.cipher_var, value="vigenere").grid(row=0, column=1, sticky=tk.W)
        tk.Radiobutton(main_frame, text="Playfair", variable=self.cipher_var, value="playfair").grid(row=0, column=2, sticky=tk.W)
        tk.Radiobutton(main_frame, text="Hill", variable=self.cipher_var, value="hill").grid(row=0, column=3, sticky=tk.W)

        tk.Button(main_frame, text="Pilih File", command=self.load_file).grid(row=1, column=0, columnspan=4, pady=5)

        tk.Label(main_frame, text="Masukkan pesan:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W)
        self.message_text = scrolledtext.ScrolledText(main_frame, width=50, height=10)
        self.message_text.grid(row=3, column=0, columnspan=4, pady=5)

        tk.Label(main_frame, text="Masukkan kunci (min 12 karakter):", font=("Arial", 12)).grid(row=4, column=0, sticky=tk.W)
        self.key_entry = tk.Entry(main_frame, width=50)
        self.key_entry.grid(row=5, column=0, columnspan=4, pady=5)

        tk.Button(main_frame, text="Enkripsi", command=self.encrypt, bg="green", fg="white").grid(row=6, column=1, padx=5, pady=5)
        tk.Button(main_frame, text="Dekripsi", command=self.decrypt, bg="red", fg="white").grid(row=6, column=2, padx=5, pady=5)

        tk.Label(main_frame, text="Hasil:", font=("Arial", 12)).grid(row=7, column=0, sticky=tk.W)
        self.result_text = scrolledtext.ScrolledText(main_frame, width=50, height=10)
        self.result_text.grid(row=8, column=0, columnspan=4, pady=5)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            message = read_input(file_path)
            if message:
                self.message_text.delete(1.0, tk.END)
                self.message_text.insert(tk.END, message)

    def encrypt(self):
        cipher = self.cipher_var.get()
        message = self.message_text.get(1.0, tk.END).strip()
        key = self.key_entry.get().strip()

        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus minimal 12 karakter.")
            return

        try:
            if cipher == "vigenere":
                result = vigenere_encrypt(message, key)
            elif cipher == "playfair":
                result = playfair_encrypt(message, key)
            elif cipher == "hill":
                key_matrix = self.get_hill_key_matrix()
                if key_matrix is None:
                    return
                result = hill_encrypt(message, key_matrix)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def decrypt(self):
        cipher = self.cipher_var.get()
        message = self.message_text.get(1.0, tk.END).strip()
        key = self.key_entry.get().strip()

        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus minimal 12 karakter.")
            return

        try:
            if cipher == "vigenere":
                result = vigenere_decrypt(message, key)
            elif cipher == "playfair":
                result = playfair_decrypt(message, key)
            elif cipher == "hill":
                key_matrix = self.get_hill_key_matrix()
                if key_matrix is None:
                    return
                result = hill_decrypt(message, key_matrix)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def get_hill_key_matrix(self):
        matrix_str = simpledialog.askstring("Matriks Kunci",
                                            "Masukkan matriks kunci Hill Cipher (misal: [[2, 3], [1, 6]]):")
        if matrix_str:
            try:
                key_matrix = eval(matrix_str)
                return np.array(key_matrix)
            except Exception as e:
                messagebox.showerror("Error", "Matriks kunci tidak valid.")
                return None
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptographyApp(root)
    root.mainloop()