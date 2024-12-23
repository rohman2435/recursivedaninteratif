import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Fungsi rekursif untuk simulasi pencarian data

def search_data_recursive(n, process_time=0.01):
    if n <= 0:
        return
    # Simulasi overhead stack call
    time.sleep(process_time)  # Simulasi waktu proses
    search_data_recursive(n - 1, process_time * 1.2)  # Tambah overhead

# Fungsi iteratif untuk simulasi pencarian data
def search_data_iterative(n, process_time=0.01):
    for _ in range(n):
        time.sleep(process_time)  # Simulasi waktu proses

# List untuk menyimpan data grafik
n_values = []
recursive_times = []
iterative_times = []

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, recursive_times, label="Recursive", marker='o', linestyle='-', color='r')
    plt.plot(n_values, iterative_times, label="Iterative", marker='o', linestyle='-', color='b')
    plt.title("Performance Comparison: Recursive vs Iterative (E-Commerce Data Search)")
    plt.xlabel("Number of Searches (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Fungsi untuk mencetak tabel waktu eksekusi
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["n", "Recursive Time (s)", "Iterative Time (s)"]
    min_len = min(len(n_values), len(recursive_times), len(iterative_times))
    for i in range(min_len):
        table.add_row([n_values[i], recursive_times[i], iterative_times[i]])
    print(table)

# Program utama
while True:
    try:
        n = int(input("Masukkan jumlah pencarian (n) (atau ketik -1 untuk keluar): "))
        if n == -1:
            print("Program selesai. Terima kasih!")
            break
        if n < 0:
            print("Masukkan nilai n yang positif!")
            continue

        n_values.append(n)

        # Ukur waktu eksekusi algoritma rekursif
        print(f"Memulai proses rekursif untuk {n} pencarian...")
        start_time = time.time()
        search_data_recursive(n)
        recursive_time = time.time() - start_time
        recursive_times.append(recursive_time)
        print(f"Waktu eksekusi rekursif: {recursive_time:.4f} detik")

        # Ukur waktu eksekusi algoritma iteratif
        print(f"Memulai proses iteratif untuk {n} pencarian...")
        start_time = time.time()
        search_data_iterative(n)
        iterative_time = time.time() - start_time
        iterative_times.append(iterative_time)
        print(f"Waktu eksekusi iteratif: {iterative_time:.4f} detik")

        # Cetak tabel waktu eksekusi
        print("\nTabel Waktu Eksekusi:")
        print_execution_table()

        # Perbarui grafik
        update_graph()

    except ValueError:
        print("Masukkan jumlah pencarian (n) yang valid!")