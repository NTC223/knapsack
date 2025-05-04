from math import gcd

# Hàm tìm modular inverse của r mod m (Euclid mở rộng)
def modinv(r, m):
    for x in range(1, m):
        if (r * x) % m == 1:
            return x
    raise Exception("Modular inverse not found")

# Mã hóa dãy bit M bằng public key B
def encrypt(M, B):
    return sum([bit * b for bit, b in zip(M, B)])

# Giải mã ciphertext C về dãy bit M gốc
def decrypt(C, W, r, m):
    r_inv = modinv(r, m)
    C_prime = (C * r_inv) % m

    # Dùng greedy để tìm dãy bit từ dãy siêu tăng W
    M = []
    for w in reversed(W):
        if C_prime >= w:
            M.insert(0, 1)
            C_prime -= w
        else:
            M.insert(0, 0)
    return M

# ---------- DEMO ----------
# Dãy siêu tăng W
W = [2, 3, 7, 14, 30]
m = 71  # m > sum(W)
r = 17  # gcd(r, m) = 1

# Tạo khóa công khai
B = [(r * w) % m for w in W]

# Bản rõ dạng bit
M = [1, 0, 1, 1, 0]

# Mã hóa
C = encrypt(M, B)
print("Ciphertext:", C)

# Giải mã
decrypted = decrypt(C, W, r, m)
print("Decrypted:", decrypted)
