import os
import psycopg2
import pandas as pd
from tabulate import tabulate
from config import config
from datetime import datetime
import sys


# FUNGSI UNTUK KONEK KE DATABASE POSTGRESQL
def connect():
    try:
        conn = None
        params = config()
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        print("PostgreSQL database version:")
        cur.execute("SELECT version()")

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### JENIS KELAMIN ################################################
def read_data_jenis_kelamin():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM jenis_kelamin ORDER BY id_jenis_kelamin ASC"
        df = pd.read_sql_query(sql, conn)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_jenis_kelamin(id_jenis_kelamin, nama_jenis_kelamin):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO jenis_kelamin (id_jenis_kelamin, nama_jenis_kelamin)
        VALUES (%s, %s)
        """
        cur = conn.cursor()
        cur.execute(sql, (id_jenis_kelamin, nama_jenis_kelamin))
        conn.commit()
        cur.close()
        print("Data berhasil ditambahkan ke tabel jenis_kelamin.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_jenis_kelamin(id_jenis_kelamin):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "DELETE FROM jenis_kelamin WHERE id_jenis_kelamin = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_jenis_kelamin,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel jenis_kelamin.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_jenis_kelamin(id_jenis_kelamin, nama_jenis_kelamin):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        UPDATE jenis_kelamin
        SET nama_jenis_kelamin = %s
        WHERE id_jenis_kelamin = %s
        """
        cur = conn.cursor()
        cur.execute(sql, (nama_jenis_kelamin, id_jenis_kelamin))
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel jenis_kelamin.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### JENIS KELAMIN ################################################

################################### ROLE ################################################


def insert_data_role(id_role, nama_role, deskripsi):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO role (id_role, nama_role, deskripsi)
        VALUES (%s, %s, %s)
        """
        cur = conn.cursor()
        cur.execute(sql, (id_role, nama_role, deskripsi))
        conn.commit()
        cur.close()
        print("Data berhasil ditambahkan ke tabel role.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_role(id_role):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "DELETE FROM role WHERE id_role = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_role,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel role.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_role(id_role, nama_role, deskripsi):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        UPDATE role
        SET nama_role = %s,
            deskripsi = %s
        WHERE id_role = %s
        """
        cur = conn.cursor()
        cur.execute(sql, (nama_role, deskripsi, id_role))
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel role.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def read_data_role():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM role"
        df = pd.read_sql_query(sql, conn)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### ROLE ################################################

################################### KECAMATAN ################################################


def read_data_kecamatan():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM kecamatan ORDER BY id_kecamatan ASC"
        df = pd.read_sql_query(sql, conn)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_kecamatan(id_kecamatan, nama_kecamatan):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO kecamatan (id_kecamatan, nama_kecamatan)
        VALUES (%s, %s)
        """
        cur = conn.cursor()
        cur.execute(sql, (id_kecamatan, nama_kecamatan))
        conn.commit()
        cur.close()
        print("Data berhasil ditambahkan ke tabel kecamatan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_kecamatan(id_kecamatan):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "DELETE FROM kecamatan WHERE id_kecamatan = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_kecamatan,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel kecamatan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_kecamatan(id_kecamatan, nama_kecamatan):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        UPDATE kecamatan
        SET nama_kecamatan = %s
        WHERE id_kecamatan = %s
        """
        cur = conn.cursor()
        cur.execute(sql, (nama_kecamatan, id_kecamatan))
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel kecamatan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### KECAMATAN ################################################

################################### KELURAHAN ################################################


def read_data_kelurahan():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM kelurahan ORDER BY id_kelurahan ASC"
        df = pd.read_sql_query(sql, conn)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_kelurahan(id_kelurahan, nama_kelurahan):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO kelurahan (id_kelurahan, nama_kelurahan)
        VALUES (%s, %s)
        """
        cur = conn.cursor()
        cur.execute(sql, (id_kelurahan, nama_kelurahan))
        conn.commit()
        cur.close()
        print("Data berhasil ditambahkan ke tabel kelurahan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_kelurahan(id_kelurahan):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "DELETE FROM kelurahan WHERE id_kelurahan = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_kelurahan,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel kelurahan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_kelurahan(id_kelurahan, nama_kelurahan):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        UPDATE kelurahan
        SET nama_kelurahan = %s
        WHERE id_kelurahan = %s
        """
        cur = conn.cursor()
        cur.execute(sql, (nama_kelurahan, id_kelurahan))
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel kelurahan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### KELURAHAN ################################################


################################### ALAMAT ################################################
def insert_data_alamat(
    id_alamat, nama_jalan, no_rumah, kecamatan_id_kecamatan, kelurahan_id_kelurahan
):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO alamat (Id_Alamat, Nama_Jalan, No_Rumah, Kecamatan_id_kecamatan, Kelurahan_id_kelurahan)
        VALUES (%s, %s, %s, %s, %s)
        """
        cur = conn.cursor()
        cur.execute(
            sql,
            (
                id_alamat,
                nama_jalan,
                no_rumah,
                kecamatan_id_kecamatan,
                kelurahan_id_kelurahan,
            ),
        )
        conn.commit()
        cur.close()
        print("Data berhasil ditambahkan ke tabel alamat.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def read_data_alamat():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM alamat"
        df = pd.read_sql_query(sql, conn)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_alamat(
    id_alamat, nama_jalan, no_rumah, kecamatan_id_kecamatan, kelurahan_id_kelurahan
):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        UPDATE alamat
        SET Nama_Jalan = %s,
            No_Rumah = %s,
            Kecamatan_id_kecamatan = %s,
            Kelurahan_id_kelurahan = %s
        WHERE Id_Alamat = %s
        """
        cur = conn.cursor()
        cur.execute(
            sql,
            (
                nama_jalan,
                no_rumah,
                kecamatan_id_kecamatan,
                kelurahan_id_kelurahan,
                id_alamat,
            ),
        )
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel alamat.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_alamat(id_alamat):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "DELETE FROM alamat WHERE Id_Alamat = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_alamat,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel alamat.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### ALAMAT ################################################

################################### AKUN ################################################


def read_data_akun():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM akun ORDER BY id_akun ASC"
        df = pd.read_sql_query(sql, conn)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_akun(
    id_akun,
    username,
    password,
    role_id_role,
    jenis_kelamin_id_jenis_kelamin,
    alamat_id_alamat,
    nomor_telepon,
):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        # Get the current date
        tanggal_masuk = datetime.now().date()

        sql = """
        INSERT INTO akun (id_akun, username, password, role_id_role, jenis_kelamin_id_jenis_kelamin, alamat_id_alamat, nomor_telepon, tanggal_masuk)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur = conn.cursor()
        cur.execute(
            sql,
            (
                id_akun,
                username,
                password,
                role_id_role,
                jenis_kelamin_id_jenis_kelamin,
                alamat_id_alamat,
                nomor_telepon,
                tanggal_masuk,
            ),
        )
        conn.commit()
        cur.close()
        print("Data berhasil ditambahkan ke tabel akun.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_akun(id_akun):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "DELETE FROM akun WHERE id_akun = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_akun,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel akun.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_akun(
    id_akun,
    username,
    password,
    role_id_role,
    jenis_kelamin_id_jenis_kelamin,
    alamat_id_alamat,
    nomor_telepon,
):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        UPDATE akun
        SET username = %s,
            password = %s,
            role_id_role = %s,
            jenis_kelamin_id_jenis_kelamin = %s,
            alamat_id_alamat = %s,
            nomor_telepon = %s
        WHERE id_akun = %s
        """
        cur = conn.cursor()
        cur.execute(
            sql,
            (
                username,
                password,
                role_id_role,
                jenis_kelamin_id_jenis_kelamin,
                alamat_id_alamat,
                nomor_telepon,
                id_akun,
            ),
        )
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel akun.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### AKUN ################################################


################################### LOGIN ################################################
def login(username, password):
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM akun WHERE username = %s AND password = %s"
        cur = conn.cursor()
        cur.execute(sql, (username, password))
        user = cur.fetchone()

        if user:
            user_id = user[0]
            id_role = user[3]

            if id_role == 1:
                print("Selamat datang Owner")
                allfitur_Owner()
            elif id_role == 2:
                print("Selamat datang Staff")
                allfitur_Staff()
            else:
                print("Role tidak valid")

        else:
            print("Login gagal, username atau password salah")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### LOGIN ################################################


################################### MENU AWAL ################################################
def main():
    os.system("cls")
    while True:
        print("Selamat datang di (Batik Karimata) Bataka Jember")
        print("MENU")
        print("1.Login")
        print("2.Keluar Aplikasi")
        user_input = input("Masukkan opsi: ")
        if user_input == "1":
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            login(username, password)
        elif user_input == "2":
            sys.exit()
        else:
            print("Opsi tidak valid. Silahkan coba lagi.")


################################### MENU AWAL ################################################


################################### ONLY FOR OWNER ################################################
def allfitur_Owner():
    os.system("cls")
    while True:
        print("HALO OWNER!!")
        print("MENU:")
        print("1.Bahan")
        print("2.Bahan Keluar")
        print("3.Ketersediaan Bahan")
        print("4.Fitur Pokok")
        print("5.Tambah Data AKUN")
        print("6.Keluar Aplikasi")

        user_input = input("pilih opsi: ")
        if user_input == "1":
            print("belum ada fitur dek")
        elif user_input == "2":
            print("belum ada fitur")
        elif user_input == "3":
            print("Belum ada fitur")
        elif user_input == "4":
            fiturpokok_owner()
        elif user_input == "5":
            daftar_Tambah_Data()
        elif user_input == "6":
            sys.exit()
        else:
            print("Pilihan invalid")


################################### ONLY FOR OWNER ################################################


################################### ONLY FOR STAFF ################################################
def allfitur_Staff():
    os.system("cls")
    while True:
        print("HALO STAFF!!")
        print("MENU:")
        print("1.Bahan")
        print("2.Bahan Keluar")
        print("3.Ketersediaan Bahan")
        print("4.Data Fitur Pokok")
        print("5.Keluar Aplikasi")

        user_input = input("pilih opsi: ")
        if user_input == "1":
            print("belum ada fitur dek")
        elif user_input == "2":
            print("belum ada fitur")
        elif user_input == "3":
            print("Belum ada fitur")
        elif user_input == "4":
            fiturpokok_staff()
        elif user_input == "5":
            sys.exit()
        else:
            print("Pilihan invalid")


################################### ONLY FOR STAFF ################################################


################################### CRUD AKUN ################################################
def daftar_Tambah_Data():
    os.system("cls")
    while True:
        print("Menu:")
        print("1.Data akun")
        print("2.Tambah Akun")
        print("3.Edit Data")
        print("4.Delete Akun")
        print("5.Kembali")

        user_input = input("Pilih opsi: ")
        if user_input == "1":
            read_data_akun()
        elif user_input == "2":
            id_akun = input("Masukkan id_akun: ")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            role_id_role = input("Masukkan role_id_role: ")
            jenis_kelamin_id_jenis_kelamin = input(
                "Masukkan jenis_kelamin_id_jenis_kelamin: "
            )
            alamat_id_alamat = input("Masukkan alamat_id_alamat: ")
            nomor_telepon = input("Masukkan nomor_telepon: ")
            insert_data_akun(
                id_akun,
                username,
                password,
                role_id_role,
                jenis_kelamin_id_jenis_kelamin,
                alamat_id_alamat,
                nomor_telepon,
            )

        elif user_input == "3":
            id_akun = input("Masukkan id_akun yang ingin diupdate: ")
            username = input("Masukkan username baru: ")
            password = input("Masukkan password baru: ")
            role_id_role = input("Masukkan role_id_role baru: ")
            jenis_kelamin_id_jenis_kelamin = input(
                "Masukkan jenis_kelamin_id_jenis_kelamin baru: "
            )
            alamat_id_alamat = input("Masukkan alamat_id_alamat baru: ")
            nomor_telepon = input("Masukkan nomor_telepon baru: ")

            # Panggil fungsi untuk mengupdate data akun
            update_data_akun(
                id_akun,
                username,
                password,
                role_id_role,
                jenis_kelamin_id_jenis_kelamin,
                alamat_id_alamat,
                nomor_telepon,
            )
        elif user_input == "4":
            id_akun = input("Masukkan ID Akun yang akan dihapus: ")
            delete_data_akun(id_akun)
        elif user_input == "5":
            allfitur_Owner()
        else:
            print("Opsi Tidak Valid")


################################### CRUD AKUN ################################################


################################### Fitur Pokok For owner ################################################
def fiturpokok_owner():
    os.system("cls")
    while True:
        print("1.Crud Role")
        print("2.Crud Jenis_Kelamin ")
        print("3.Crud Kecamatan")
        print("4.Crud Kelurahan")
        print("5.Crud Alamat")
        print("6.Kembali")

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            menu_crud_role()
        elif user_input == "2":
            menu_crud_jenis_kelamin()
        elif user_input == "3":
            menu_crud_kecamatan()
        elif user_input == "4":
            print("belum")
        elif user_input == "5":
            print("belum")
        elif user_input == "6":
            allfitur_Owner()
        else:
            print("Opsi Tidak valid")


################################### Fitur Pokok For Owner ################################################


################################### Fitur Pokok For Staff ################################################
def fiturpokok_staff():
    os.system("cls")
    while True:
        print("1.Data Jenis_Kelamin ")
        print("2.Data Kecamatan")
        print("3.Data Kelurahan")
        print("4.Data Alamat")
        print("5.Kembali")

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_jenis_kelamin()
        elif user_input == "2":
            read_data_kecamatan()
        elif user_input == "3":
            read_data_kelurahan()
        elif user_input == "4":
            read_data_alamat()
        elif user_input == "5":
            allfitur_Staff()
        else:
            print("Opsi Tidak valid")


################################### Fitur Pokok For Staff ################################################


################################### MENU CRUD ROLE ################################################
def menu_crud_role():
    os.system("cls")
    while True:
        print("1.Baca Data")
        print("2.Tambah Data")
        print("3.Edit Data")
        print("4.Hapus Data")
        print("5.Kembali")

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_role()
        elif user_input == "2":
            id_role = input("Masukkan ID Role: ")
            nama_role = input("Masukkan Nama Role: ")
            deskripsi = input("Masukkan Deskripsi: ")
            insert_data_role(id_role, nama_role, deskripsi)
        elif user_input == "3":
            id_role = input("Masukkan ID Role yang akan diupdate: ")
            nama_role = input("Masukkan Nama Role baru: ")
            deskripsi = input("Masukkan Deskripsi baru: ")
            update_data_role(id_role, nama_role, deskripsi)
        elif user_input == "4":
            id_role = input("Masukkan ID Role yang akan dihapus: ")
            delete_data_role(id_role)
        elif user_input == "5":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD ROLE ################################################


################################### MENU CRUD Jenis_Kelamin ################################################
def menu_crud_jenis_kelamin():
    os.system("cls")
    while True:
        print("1.Baca Data")
        print("2.Tambah Data")
        print("3.Edit Data")
        print("4.Hapus Data")
        print("5.Kembali")

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_jenis_kelamin()
        elif user_input == "2":
            id_jenis_kelamin = input("Masukkan ID Jenis Kelamin: ")
            nama_jenis_kelamin = input("Masukkan Nama Jenis Kelamin: ")
            insert_data_jenis_kelamin(id_jenis_kelamin, nama_jenis_kelamin)
        elif user_input == "3":
            id_jenis_kelamin = input("Masukkan ID Jenis Kelamin yang akan diupdate: ")
            nama_jenis_kelamin = input("Masukkan Nama Jenis Kelamin baru: ")
            update_data_jenis_kelamin(id_jenis_kelamin, nama_jenis_kelamin)
        elif user_input == "4":
            id_jenis_kelamin = input("Masukkan ID Jenis Kelamin yang akan dihapus: ")
            delete_data_jenis_kelamin(id_jenis_kelamin)
        elif user_input == "5":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Jenis_Kelamin ################################################


################################### MENU CRUD Kecamatan ################################################
def menu_crud_kecamatan():
    os.system("cls")
    while True:
        print("1.Baca Data")
        print("2.Tambah Data")
        print("3.Edit Data")
        print("4.Hapus Data")
        print("5.Kembali")

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_kecamatan()
        elif user_input == "2":
            id_kecamatan = input("Masukkan ID Kecamatan: ")
            nama_kecamatan = input("Masukkan Nama Kecamatan: ")
            insert_data_kecamatan(id_kecamatan, nama_kecamatan)
        elif user_input == "3":
            id_kecamatan = input("Masukkan ID Kecamatan yang akan diupdate: ")
            nama_kecamatan = input("Masukkan Nama Kecamatan baru: ")
            update_data_kecamatan(id_kecamatan, nama_kecamatan)
        elif user_input == "4":
            id_kecamatan = input("Masukkan ID Kecamatan yang akan dihapus: ")
            delete_data_kecamatan(id_kecamatan)
        elif user_input == "5":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Kecamatan ################################################


################################### MENU CRUD Kecamatan ################################################
def menu_crud_kecamatan():
    os.system("cls")
    while True:
        print("1.Baca Data")
        print("2.Tambah Data")
        print("3.Edit Data")
        print("4.Hapus Data")
        print("5.Kembali")

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_kecamatan()
        elif user_input == "2":
            id_kecamatan = input("Masukkan ID Kecamatan: ")
            nama_kecamatan = input("Masukkan Nama Kecamatan: ")
            insert_data_kecamatan(id_kecamatan, nama_kecamatan)
        elif user_input == "3":
            id_kecamatan = input("Masukkan ID Kecamatan yang akan diupdate: ")
            nama_kecamatan = input("Masukkan Nama Kecamatan baru: ")
            update_data_kecamatan(id_kecamatan, nama_kecamatan)
        elif user_input == "4":
            id_kecamatan = input("Masukkan ID Kecamatan yang akan dihapus: ")
            delete_data_kecamatan(id_kecamatan)
        elif user_input == "5":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Kecamatan ################################################


################################### MENU CRUD Kelurahan ################################################
def menu_crud_kelurahan():
    os.system("cls")
    while True:
        print("1.Baca Data")
        print("2.Tambah Data")
        print("3.Edit Data")
        print("4.Hapus Data")
        print("5.Kembali")

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_kelurahan()
        elif user_input == "2":
            id_kelurahan = input("Masukkan ID Kelurahan: ")
            nama_kelurahan = input("Masukkan Nama Kelurahan: ")
            insert_data_kelurahan(id_kelurahan, nama_kelurahan)
        elif user_input == "3":
            id_kelurahan = input("Masukkan ID Kelurahan yang akan diupdate: ")
            nama_kelurahan = input("Masukkan Nama Kelurahan baru: ")
            update_data_kelurahan(id_kelurahan, nama_kelurahan)
        elif user_input == "4":
            id_kelurahan = input("Masukkan ID Kelurahan yang akan dihapus: ")
            delete_data_kelurahan(id_kelurahan)
        elif user_input == "5":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD kelurahan ################################################


################################### MENU CRUD Alamat ################################################
def menu_crud_alamat():
    os.system("cls")
    while True:
        print("1.Baca Data")
        print("2.Tambah Data")
        print("3.Edit Data")
        print("4.Hapus Data")
        print("5.Kembali")

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_alamat()
        elif user_input == "2":
            id_alamat = int(input("Masukkan ID Alamat: "))
            nama_jalan = input("Masukkan Nama Jalan: ")
            no_rumah = int(input("Masukkan Nomor Rumah: "))
            kecamatan_id_kecamatan = int(input("Masukkan ID Kecamatan: "))
            kelurahan_id_kelurahan = int(input("Masukkan ID Kelurahan: "))
            insert_data_alamat(
                id_alamat,
                nama_jalan,
                no_rumah,
                kecamatan_id_kecamatan,
                kelurahan_id_kelurahan,
            )
        elif user_input == "3":
            id_alamat = int(input("Masukkan ID Alamat yang akan diupdate: "))
            nama_jalan = input("Masukkan Nama Jalan baru: ")
            no_rumah = int(input("Masukkan Nomor Rumah baru: "))
            kecamatan_id_kecamatan = int(input("Masukkan ID Kecamatan baru: "))
            kelurahan_id_kelurahan = int(input("Masukkan ID Kelurahan baru: "))
            update_data_alamat(
                id_alamat,
                nama_jalan,
                no_rumah,
                kecamatan_id_kecamatan,
                kelurahan_id_kelurahan,
            )
        elif user_input == "4":
            id_alamat = int(input("Masukkan ID Alamat yang akan dihapus: "))
            delete_data_alamat(id_alamat)
        elif user_input == "5":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Alamat ################################################
# def backup():
#     print("Selamat datang di (Batik Karimata) Bataka Jember")
#     print("Silahkan pilih menu")

#     def header():
#         print(
#             """
#             MENU:
#             1. INSERT JENIS KELAMIN
#             2. DELETE JENIS KELAMIN
#             3. UPDATE JENIS KELAMIN
#             4. READ JENIS KELAMIN
#             5. INSERT ROLE
#             6. DELETE ROLE
#             7. UPDATE ROLE
#             8. READ ROLE
#             9. INSERT KECAMATAN
#             10. DELETE KECAMATAN
#             11. UPDATE KECAMATAN
#             12. READ KECAMATAN
#             13. INSERT KELURAHAN
#             14. DELETE KELURAHAN
#             15. UPDATE KELURAHAN
#             16. READ KELURAHAN
#             17. INSERT ALAMAT
#             18. DELETE ALAMAT
#             19. UPDATE ALAMAT
#             20. READ ALAMAT
#             21. INSERT AKUN
#             22. DELETE AKUN
#             23. UPDATE AKUN
#             24. READ AKUN
#             25. EXIT
#             """
#         )

#     while True:
#         header()
#         user_input = input("Masukkan opsi: ")

#         if user_input == "1":
#             id_jenis_kelamin = input("Masukkan ID Jenis Kelamin: ")
#             nama_jenis_kelamin = input("Masukkan Nama Jenis Kelamin: ")
#             insert_data_jenis_kelamin(id_jenis_kelamin, nama_jenis_kelamin)
#         elif user_input == "2":
#             id_jenis_kelamin = input("Masukkan ID Jenis Kelamin yang akan dihapus: ")
#             delete_data_jenis_kelamin(id_jenis_kelamin)
#         elif user_input == "3":
#             id_jenis_kelamin = input("Masukkan ID Jenis Kelamin yang akan diupdate: ")
#             nama_jenis_kelamin = input("Masukkan Nama Jenis Kelamin baru: ")
#             update_data_jenis_kelamin(id_jenis_kelamin, nama_jenis_kelamin)
#         elif user_input == "4":
#             read_data_jenis_kelamin()
#         elif user_input == "5":
#             id_role = input("Masukkan ID Role: ")
#             nama_role = input("Masukkan Nama Role: ")
#             deskripsi = input("Masukkan Deskripsi: ")
#             insert_data_role(id_role, nama_role, deskripsi)
#         elif user_input == "6":
#             id_role = input("Masukkan ID Role yang akan dihapus: ")
#             delete_data_role(id_role)
#         elif user_input == "7":
#             id_role = input("Masukkan ID Role yang akan diupdate: ")
#             nama_role = input("Masukkan Nama Role baru: ")
#             deskripsi = input("Masukkan Deskripsi baru: ")
#             update_data_role(id_role, nama_role, deskripsi)
#         elif user_input == "8":
#             read_data_role()
#         elif user_input == "9":
#             id_kecamatan = input("Masukkan ID Kecamatan: ")
#             nama_kecamatan = input("Masukkan Nama Kecamatan: ")
#             insert_data_kecamatan(id_kecamatan, nama_kecamatan)
#         elif user_input == "10":
#             id_kecamatan = input("Masukkan ID Kecamatan yang akan dihapus: ")
#             delete_data_kecamatan(id_kecamatan)
#         elif user_input == "11":
#             id_kecamatan = input("Masukkan ID Kecamatan yang akan diupdate: ")
#             nama_kecamatan = input("Masukkan Nama Kecamatan baru: ")
#             update_data_kecamatan(id_kecamatan, nama_kecamatan)
#         elif user_input == "12":
#             read_data_kecamatan()
#         elif user_input == "13":
#             id_kelurahan = input("Masukkan ID Kelurahan: ")
#             nama_kelurahan = input("Masukkan Nama Kelurahan: ")
#             insert_data_kelurahan(id_kelurahan, nama_kelurahan)
#         elif user_input == "14":
#             id_kelurahan = input("Masukkan ID Kelurahan yang akan dihapus: ")
#             delete_data_kelurahan(id_kelurahan)
#         elif user_input == "15":
#             id_kelurahan = input("Masukkan ID Kelurahan yang akan diupdate: ")
#             nama_kelurahan = input("Masukkan Nama Kelurahan baru: ")
#             update_data_kelurahan(id_kelurahan, nama_kelurahan)
#         elif user_input == "16":
#             read_data_kelurahan()
#         elif user_input == "17":
#             id_alamat = int(input("Masukkan ID Alamat: "))
#             nama_jalan = input("Masukkan Nama Jalan: ")
#             no_rumah = int(input("Masukkan Nomor Rumah: "))
#             kecamatan_id_kecamatan = int(input("Masukkan ID Kecamatan: "))
#             kelurahan_id_kelurahan = int(input("Masukkan ID Kelurahan: "))
#             insert_data_alamat(
#                 id_alamat,
#                 nama_jalan,
#                 no_rumah,
#                 kecamatan_id_kecamatan,
#                 kelurahan_id_kelurahan,
#             )
#         elif user_input == "18":
#             read_data_alamat()
#         elif user_input == "19":
#             id_alamat = int(input("Masukkan ID Alamat yang akan diupdate: "))
#             nama_jalan = input("Masukkan Nama Jalan baru: ")
#             no_rumah = int(input("Masukkan Nomor Rumah baru: "))
#             kecamatan_id_kecamatan = int(input("Masukkan ID Kecamatan baru: "))
#             kelurahan_id_kelurahan = int(input("Masukkan ID Kelurahan baru: "))
#             update_data_alamat(
#                 id_alamat,
#                 nama_jalan,
#                 no_rumah,
#                 kecamatan_id_kecamatan,
#                 kelurahan_id_kelurahan,
#             )
#         elif user_input == "20":
#             id_alamat = int(input("Masukkan ID Alamat yang akan dihapus: "))
#             delete_data_alamat(id_alamat)
#         elif user_input == "21":
#             id_akun = input("Masukkan ID Akun: ")
#             username = input("Masukkan Username: ")
#             password = input("Masukkan Password: ")
#             role_id_role = input("Masukkan Role ID Role: ")
#             jenis_kelamin_id_jenis_kelamin = input(
#                 "Masukkan Jenis Kelamin ID Jenis Kelamin: "
#             )
#             alamat_id_alamat = input("Masukkan Alamat ID Alamat: ")
#             nomor_telepon = input("Masukkan Nomor Telepon: ")
#             tanggal_masuk = input("Masukkan Tanggal Masuk: ")
#             insert_data_akun(
#                 id_akun,
#                 username,
#                 password,
#                 role_id_role,
#                 jenis_kelamin_id_jenis_kelamin,
#                 alamat_id_alamat,
#                 nomor_telepon,
#                 tanggal_masuk,
#             )
#         elif user_input == "22":
#             id_akun = input("Masukkan ID Akun yang akan dihapus: ")
#             delete_data_akun(id_akun)
#         elif user_input == "23":
#             id_akun = input("Masukkan ID Akun yang akan diupdate: ")
#             username = input("Masukkan Username baru: ")
#             password = input("Masukkan Password baru: ")
#             role_id_role = input("Masukkan Role ID Role baru: ")
#             jenis_kelamin_id_jenis_kelamin = input(
#                 "Masukkan Jenis Kelamin ID Jenis Kelamin baru: "
#             )
#             alamat_id_alamat = input("Masukkan Alamat ID Alamat baru: ")
#             nomor_telepon = input("Masukkan Nomor Telepon baru: ")
#             tanggal_masuk = input("Masukkan Tanggal Masuk baru: ")
#             update_data_akun(
#                 id_akun,
#                 username,
#                 password,
#                 role_id_role,
#                 jenis_kelamin_id_jenis_kelamin,
#                 alamat_id_alamat,
#                 nomor_telepon,
#                 tanggal_masuk,
#             )
#         elif user_input == "24":
#             read_data_akun()
#         elif user_input == "25":
#             username = input("Masukkan username: ")
#             password = input("Masukkan password: ")

#             login(username, password)
#         else:
#             print("Opsi tidak valid. Silahkan coba lagi.")


if __name__ == "__main__":
    main()
