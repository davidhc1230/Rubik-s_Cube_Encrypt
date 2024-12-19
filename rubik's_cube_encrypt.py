import getpass
import os
import random
import time

def rotate_row(row, shift):
    """Rotate a row to the left"""
    shift = shift % len(row)  # Avoid exceeding row length
    return row[shift:] + row[:shift]  # Left rotation

def rotate_column(matrix, col_idx, shift):
    """Rotate a column upwards"""
    column = [row[col_idx] for row in matrix]
    shift = shift % len(column)  # Avoid exceeding column length
    rotated = column[shift:] + column[:shift]  # Upward rotation
    for i in range(len(matrix)):
        matrix[i][col_idx] = rotated[i]

def generate_shift_code(input_number):
    """Generate shift code based on input number"""
    code = [int(digit) for digit in str(input_number)]
    return code

def calculate_offset(key):
    """Calculate offset based on key (sum modulo)"""
    digits = [int(d) for d in str(key)]
    return sum(digits) % 10  # Limit offset to range 0-9

def calculate_iterations(key):
    """Calculate the number of iterations (N) based on the key"""
    digits = [int(d) for d in str(key)]
    return sum(digits)

def encrypt_text_file(file_path, row_code, col_code, iterations):
    """Encrypt a text file N times"""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Record the original length of each line
    original_lengths = [len(line.rstrip()) for line in lines]
    max_len = max(original_lengths)

    # Pad all lines to the same length using '\u0000' as padding character
    matrix = [list(line.rstrip().ljust(max_len, '\u0000')) for line in lines]

    for _ in range(iterations):
        # Calculate offset
        offset = calculate_offset("".join(map(str, row_code)))  # Calculate offset using row shift code

        # Rotate rows
        for i in range(len(matrix)):
            shift = row_code[i % len(row_code)]
            matrix[i] = rotate_row(matrix[i], shift)

        # Rotate columns
        for j in range(max_len):
            shift = col_code[j % len(col_code)]
            rotate_column(matrix, j, shift)

        # Encrypt line lengths
        original_lengths = [length + offset for length in original_lengths]

    # Append encrypted line lengths to the file
    encrypted_content = "\n".join("".join(row) for row in matrix)
    encrypted_content += "\n" + ",".join(map(str, original_lengths))  # Append encrypted line lengths
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'w', encoding='utf-8') as enc_file:
        enc_file.write(encrypted_content)

    print(f"File has been encrypted and saved as: {encrypted_file_path}")

def decrypt_text_file(file_path, row_code, col_code, iterations):
    delay = random.uniform(10, 15)
    print(f"Please wait... Processing decryption.")
    time.sleep(delay)
    """Decrypt a text file N times"""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Extract encrypted line lengths and remove them
    encrypted_lengths = list(map(int, lines[-1].split(',')))
    lines = lines[:-1]

    max_len = len(lines[0].rstrip())  # Maximum line length
    matrix = [list(line.rstrip().ljust(max_len, '\u0000')) for line in lines]

    for _ in range(iterations):
        # Calculate offset
        offset = calculate_offset("".join(map(str, row_code)))  # Calculate offset using row shift code

        # Decrypt line lengths
        encrypted_lengths = [length - offset for length in encrypted_lengths]

        # Reverse column rotation
        for j in range(max_len):
            shift = col_code[j % len(col_code)]
            rotate_column(matrix, j, -shift)

        # Reverse row rotation
        for i in range(len(matrix)):
            shift = row_code[i % len(row_code)]
            matrix[i] = rotate_row(matrix[i], -shift)

    # Restore each line based on original lengths and remove padding characters
    decrypted_content = "\n".join("".join(row[:encrypted_lengths[i]]) for i, row in enumerate(matrix))
    decrypted_file_path = file_path.replace('.encrypted', '.decrypted')
    with open(decrypted_file_path, 'w', encoding='utf-8') as dec_file:
        dec_file.write(decrypted_content)

    print(f"File has been decrypted and saved as: {decrypted_file_path}")

def main():
    print("Welcome to the text file encryption and decryption program!")
    file_name = input("Please enter the name of the text file to process (including extension): ").strip()

    if not os.path.isfile(file_name):
        print("Invalid file name. Please check and rerun the program.")
        return

    operation = input("Please choose an operation: 1 for Encrypt, 2 for Decrypt: ").strip()
    if operation not in ['1', '2']:
        print("Invalid operation. Please choose '1' for Encrypt or '2' for Decrypt.")
        return

    # Use getpass to hide input
    input_number = getpass.getpass("Please enter a numeric key of up to 12 digits: ").strip()
    if not input_number.isdigit() or len(input_number) > 12:
        print("Invalid numeric key. Please enter a positive integer of 1 to 12 digits.")
        return

    row_code = generate_shift_code(input_number)
    col_code = generate_shift_code(input_number[::-1])
    iterations = calculate_iterations(input_number)

    if operation == '1':
        encrypt_text_file(file_name, row_code, col_code, iterations)
    elif operation == '2':
        decrypt_text_file(file_name, row_code, col_code, iterations)

if __name__ == '__main__':
    main()
