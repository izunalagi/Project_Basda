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
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM jenis_kelamin ORDER BY id_jenis_kelamin ASC"
        df = pd.read_sql_query(sql, conn)
        os.system("cls")
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_jenis_kelamin():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        nama_jenis_kelamin = input("Masukkan Nama Jenis Kelamin: ")

        cur = conn.cursor()
        cur.execute("SELECT COALESCE(MAX(id_jenis_kelamin), 0) FROM jenis_kelamin")
        max_id = cur.fetchone()[0]
        new_id = max_id + 1

        sql = """
        INSERT INTO jenis_kelamin (id_jenis_kelamin, nama_jenis_kelamin)
        VALUES (%s, %s)
        """
        cur.execute(sql, (new_id, nama_jenis_kelamin))
        conn.commit()
        cur.close()
        print(f"Data berhasil ditambahkan ke tabel jenis_kelamin dengan id: {new_id}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_jenis_kelamin():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_jenis_kelamin()
        id_jenis_kelamin = int(input("Masukkan Id Jenis Kelamin yang ingin dihapus: "))

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


def update_data_jenis_kelamin():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_jenis_kelamin()
        id_jenis_kelamin = int(
            input("Masukkan Id Jenis Kelamin yang ingin diperbarui: ")
        )
        nama_jenis_kelamin = input("Masukkan Nama Jenis Kelamin Baru: ")

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
def insert_data_role():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        nama_role = input("Masukkan Nama Role: ")
        deskripsi = input("Masukkan Deskripsi Role: ")

        cur = conn.cursor()
        cur.execute("SELECT COALESCE(MAX(id_role), 0) FROM role")
        max_id = cur.fetchone()[0]
        new_id = max_id + 1

        sql = """
        INSERT INTO role (id_role, nama_role, deskripsi)
        VALUES (%s, %s, %s)
        """
        cur.execute(sql, (new_id, nama_role, deskripsi))
        conn.commit()
        cur.close()
        print(f"Data berhasil ditambahkan ke tabel role dengan id: {new_id}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_role():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_role()
        id_role = input("Masukkan ID Role yang akan dihapus: ")

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


def update_data_role():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_role()
        id_role = input("Masukkan ID Role yang akan diupdate: ")
        nama_role = input("Masukkan Nama Role baru: ")
        deskripsi = input("Masukkan Deskripsi Role baru: ")

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
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM role ORDER BY id_role ASC"
        df = pd.read_sql_query(sql, conn)
        os.system("cls")
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
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM kecamatan ORDER BY id_kecamatan ASC"
        df = pd.read_sql_query(sql, conn)
        os.system("cls")
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_kecamatan():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        nama_kecamatan = input("Masukkan Nama Kecamatan: ")

        cur = conn.cursor()
        cur.execute("SELECT COALESCE(MAX(id_kecamatan), 0) FROM kecamatan")
        max_id = cur.fetchone()[0]
        new_id = max_id + 1

        sql = """
        INSERT INTO kecamatan (id_kecamatan, nama_kecamatan)
        VALUES (%s, %s)
        """
        cur.execute(sql, (new_id, nama_kecamatan))
        conn.commit()
        cur.close()
        print(f"Data berhasil ditambahkan ke tabel kecamatan dengan id: {new_id}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_kecamatan():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_kecamatan()
        id_kecamatan = input("Masukkan ID Kecamatan yang ingin dihapus: ")

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


def update_data_kecamatan():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_kecamatan()
        id_kecamatan = input("Masukkan ID Kecamatan yang ingin diupdate: ")
        nama_kecamatan = input("Masukkan Nama Kecamatan baru: ")

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


################################### AKUN ################################################
def read_data_akun():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = "SELECT * FROM Akun ORDER BY id_Akun ASC"
        df = pd.read_sql_query(sql, conn)
        os.system("cls")
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_akun():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute("SELECT COALESCE(MAX(id_Akun), 0) FROM Akun")
        max_id = cur.fetchone()[0]
        new_id = max_id + 1

        username = input("Enter Username: ")
        password = input("Enter Password: ")
        read_data_role()
        role_id_role = int(input("Enter Role_id_Role: "))
        read_data_jenis_kelamin()
        jenis_kelamin_id_jenis_kelamin = int(
            input("Enter Jenis_Kelamin_id_jenis_kelamin: ")
        )
        nama_jalan = input("Enter Nama_Jalan: ")
        no_rumah = int(input("Enter No_Rumah: "))
        read_data_kecamatan()
        kecamatan_id_kecamatan = int(input("Enter Kecamatan_id_kecamatan: "))
        nomor_telepon = input("Enter Nomor_Telepon: ")

        sql = """
        INSERT INTO Akun (id_Akun, Username, Password, Role_id_Role, Jenis_Kelamin_id_jenis_kelamin, Nama_Jalan, No_Rumah, Kecamatan_id_kecamatan, Nomor_Telepon, Tanggal_Masuk)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_DATE)
        """
        cur.execute(
            sql,
            (
                new_id,
                username,
                password,
                role_id_role,
                jenis_kelamin_id_jenis_kelamin,
                nama_jalan,
                no_rumah,
                kecamatan_id_kecamatan,
                nomor_telepon,
            ),
        )
        conn.commit()
        cur.close()
        print(f"Data akun berhasil ditambahkan dengan id: {new_id}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_akun():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_akun()
        id_akun = input("Enter ID Akun to delete: ")

        sql = "DELETE FROM Akun WHERE id_Akun = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_akun,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel Akun.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_akun():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_akun()
        id_akun = input("Enter ID Akun to update: ")
        username = input("Enter new Username: ")
        password = input("Enter new Password: ")
        read_data_role()
        role_id_role = int(input("Enter new Role_id_Role: "))
        read_data_jenis_kelamin()
        jenis_kelamin_id_jenis_kelamin = int(
            input("Enter new Jenis_Kelamin_id_jenis_kelamin: ")
        )
        nama_jalan = input("Enter new Nama_Jalan: ")
        no_rumah = int(input("Enter new No_Rumah: "))
        read_data_kecamatan()
        kecamatan_id_kecamatan = int(input("Enter new Kecamatan_id_kecamatan: "))
        nomor_telepon = input("Enter new Nomor_Telepon: ")

        sql = """
        UPDATE Akun
        SET Username = %s, Password = %s, Role_id_Role = %s, Jenis_Kelamin_id_jenis_kelamin = %s, Nama_Jalan = %s, No_Rumah = %s, Kecamatan_id_kecamatan = %s, Nomor_Telepon = %s
        WHERE id_Akun = %s
        """
        cur = conn.cursor()
        cur.execute(
            sql,
            (
                username,
                password,
                role_id_role,
                jenis_kelamin_id_jenis_kelamin,
                nama_jalan,
                no_rumah,
                kecamatan_id_kecamatan,
                nomor_telepon,
                id_akun,
            ),
        )
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel Akun.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### AKUN ################################################


################################### MERK ################################################
def read_data_merk():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM Merk ORDER BY Id_Merk ASC"
        df = pd.read_sql_query(sql, conn)
        os.system("cls")
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_merk():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        nama_merk = input("Masukkan Nama Merk: ")

        cur = conn.cursor()
        cur.execute("SELECT COALESCE(MAX(Id_Merk), 0) FROM Merk")
        max_id = cur.fetchone()[0]
        new_id = max_id + 1

        sql = """
        INSERT INTO Merk (Id_Merk, Nama_Merk)
        VALUES (%s, %s)
        """
        cur.execute(sql, (new_id, nama_merk))
        conn.commit()
        cur.close()
        print(f"Data berhasil ditambahkan ke tabel Merk dengan id: {new_id}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_merk():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_merk()
        id_merk = input("Masukkan ID Merk yang ingin dihapus: ")

        sql = "DELETE FROM Merk WHERE Id_Merk = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_merk,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel Merk.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_merk():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_merk()
        id_merk = input("Masukkan ID Merk yang ingin diupdate: ")
        nama_merk = input("Masukkan Nama Merk baru: ")

        sql = """
        UPDATE Merk
        SET Nama_Merk = %s
        WHERE Id_Merk = %s
        """
        cur = conn.cursor()
        cur.execute(sql, (nama_merk, id_merk))
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel Merk.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### MERK ################################################


################################### Supplier ################################################
def read_data_supplier():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM Supplier ORDER BY id_supplier ASC"
        df = pd.read_sql_query(sql, conn)
        os.system("cls")
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_supplier():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        nama_supplier = input("Masukkan Nama Supplier: ")

        cur = conn.cursor()
        cur.execute("SELECT COALESCE(MAX(id_supplier), 0) FROM Supplier")
        max_id = cur.fetchone()[0]
        new_id = max_id + 1

        sql = """
        INSERT INTO Supplier (id_supplier, nama_supplier)
        VALUES (%s, %s)
        """
        cur.execute(sql, (new_id, nama_supplier))
        conn.commit()
        cur.close()
        print(f"Data berhasil ditambahkan ke tabel Supplier dengan id: {new_id}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_supplier():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_supplier()
        id_supplier = input("Masukkan ID Supplier yang ingin dihapus: ")

        sql = "DELETE FROM Supplier WHERE id_supplier = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_supplier,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel Supplier.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_supplier():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_supplier()
        id_supplier = input("Masukkan ID Supplier yang ingin diupdate: ")
        nama_supplier = input("Masukkan Nama Supplier baru: ")

        sql = """
        UPDATE Supplier
        SET nama_supplier = %s
        WHERE id_supplier = %s
        """
        cur = conn.cursor()
        cur.execute(sql, (nama_supplier, id_supplier))
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel Supplier.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### Supplier ################################################


################################### Jenis Bahan ################################################
def insert_data_jenis_bahan():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        nama_jenis = input("Masukkan Nama Jenis Bahan: ")

        cur = conn.cursor()
        cur.execute("SELECT COALESCE(MAX(id_jenis_bahan), 0) FROM Jenis_Bahan")
        max_id = cur.fetchone()[0]
        new_id = max_id + 1

        sql = """
        INSERT INTO Jenis_Bahan (id_jenis_bahan, nama_jenis)
        VALUES (%s, %s)
        """
        cur.execute(sql, (new_id, nama_jenis))
        conn.commit()
        cur.close()
        print(f"Data berhasil ditambahkan ke tabel Jenis_Bahan dengan id: {new_id}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def read_data_jenis_bahan():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM Jenis_Bahan ORDER BY id_jenis_bahan"
        df = pd.read_sql_query(sql, conn)
        os.system("cls")
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_jenis_bahan():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_jenis_bahan()
        id_jenis_bahan = int(input("Masukkan ID Jenis Bahan yang ingin diupdate: "))
        nama_jenis = input("Masukkan Nama Jenis Bahan baru: ")

        sql = """
        UPDATE Jenis_Bahan
        SET nama_jenis = %s
        WHERE id_jenis_bahan = %s
        """
        cur = conn.cursor()
        cur.execute(sql, (nama_jenis, id_jenis_bahan))
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel Jenis_Bahan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_jenis_bahan():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_jenis_bahan()
        id_jenis_bahan = int(input("Masukkan ID Jenis Bahan yang ingin dihapus: "))

        sql = "DELETE FROM Jenis_Bahan WHERE id_jenis_bahan = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_jenis_bahan,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel Jenis_Bahan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### Jenis Bahan ################################################


################################### Ketersediaan Bahan ################################################
def read_data_ketersediaan_bahan():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM Ketersediaan_Bahan ORDER BY id_ketersediaan_bahan ASC"
        df = pd.read_sql_query(sql, conn)
        os.system("cls")
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_ketersediaan_bahan():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        nama_bahan = input("Masukkan Nama Bahan: ")
        stock = int(input("Masukkan Stock: "))
        deskripsi = input("Masukkan Deskripsi: ")
        read_data_jenis_bahan()
        jenis_bahan_id_jenis_bahan = int(input("Masukkan ID Jenis Bahan: "))
        read_data_merk()
        merk_id_merk = int(input("Masukkan ID Merk: "))

        cur = conn.cursor()
        cur.execute(
            "SELECT COALESCE(MAX(id_ketersediaan_bahan), 0) FROM Ketersediaan_Bahan"
        )
        max_id = cur.fetchone()[0]
        new_id = max_id + 1

        sql = """
        INSERT INTO Ketersediaan_Bahan (id_ketersediaan_bahan, nama_bahan, stock, deskripsi, jenis_bahan_id_jenis_bahan, merk_id_merk)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(
            sql,
            (
                new_id,
                nama_bahan,
                stock,
                deskripsi,
                jenis_bahan_id_jenis_bahan,
                merk_id_merk,
            ),
        )
        conn.commit()
        cur.close()
        print(
            f"Data berhasil ditambahkan ke tabel Ketersediaan_Bahan dengan id: {new_id}."
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_ketersediaan_bahan():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_ketersediaan_bahan()
        id_ketersediaan_bahan = int(
            input("Masukkan ID Ketersediaan Bahan yang ingin dihapus: ")
        )

        sql = "DELETE FROM Ketersediaan_Bahan WHERE id_ketersediaan_bahan = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_ketersediaan_bahan,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel Ketersediaan_Bahan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_ketersediaan_bahan():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_ketersediaan_bahan()
        id_ketersediaan_bahan = int(
            input("Masukkan ID Ketersediaan Bahan yang ingin diupdate: ")
        )
        nama_bahan = input("Masukkan Nama Bahan baru: ")
        stock = int(input("Masukkan Stock baru: "))
        deskripsi = input("Masukkan Deskripsi baru: ")
        read_data_jenis_bahan()
        jenis_bahan_id_jenis_bahan = int(input("Masukkan ID Jenis Bahan baru: "))
        read_data_merk()
        merk_id_merk = int(input("Masukkan ID Merk baru: "))

        sql = """
        UPDATE Ketersediaan_Bahan
        SET nama_bahan = %s,
            stock = %s,
            deskripsi = %s,
            jenis_bahan_id_jenis_bahan = %s,
            merk_id_merk = %s
        WHERE id_ketersediaan_bahan = %s
        """
        cur = conn.cursor()
        cur.execute(
            sql,
            (
                nama_bahan,
                stock,
                deskripsi,
                jenis_bahan_id_jenis_bahan,
                merk_id_merk,
                id_ketersediaan_bahan,
            ),
        )
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel Ketersediaan_Bahan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### Ketersediaan Bahan ################################################


################################### BAHAN MASUK ################################################
def read_data_bahan_masuk():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = "SELECT * FROM Bahan_Masuk ORDER BY id_bahan_masuk ASC"
        df = pd.read_sql_query(sql, conn)
        os.system("cls")
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_bahan_masuk(akun_id_akun):
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO bahan_masuk (akun_id_akun, tanggal)
        VALUES (%s, CURRENT_DATE)
        RETURNING id_bahan_masuk
        """
        cur = conn.cursor()
        cur.execute(sql, (akun_id_akun,))
        id_bahan_masuk_baru = cur.fetchone()[0]
        conn.commit()
        cur.close()
        print(
            f"Data bahan masuk berhasil ditambahkan dengan id: {id_bahan_masuk_baru}."
        )
        return id_bahan_masuk_baru
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_bahan_masuk(id_bahan_masuk):
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = "DELETE FROM Bahan_Masuk WHERE id_bahan_masuk = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_bahan_masuk,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel Bahan_Masuk.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_bahan_masuk():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_bahan_masuk()
        id_bahan_masuk = input("Masukkan ID Bahan Masuk yang ingin diperbarui: ")
        akun_id_akun = input("Masukkan ID Akun Baru: ")

        sql = """
        UPDATE Bahan_Masuk
        SET akun_id_akun = %s
        WHERE id_bahan_masuk = %s
        """
        cur = conn.cursor()
        cur.execute(sql, (akun_id_akun, id_bahan_masuk))
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel Bahan_Masuk.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def add_bahan_masuk_and_detail():
    os.system("cls")

    read_data_akun()
    akun_id_akun = int(input("Enter akun_id_akun: "))

    id_bahan_masuk_baru = insert_data_bahan_masuk(akun_id_akun)

    if id_bahan_masuk_baru is not None:
        while True:
            read_data_supplier()
            id_supplier = int(input("Enter id_supplier: "))
            read_data_ketersediaan_bahan()
            id_ketersediaan_bahan = int(input("Enter id_ketersediaan_bahan: "))
            quantity = int(input("Enter quantity: "))
            deskripsi = input("Enter deskripsi: ")

            insert_data_detail_bahan_masuk(
                id_bahan_masuk_baru,
                id_supplier,
                id_ketersediaan_bahan,
                quantity,
                deskripsi,
            )

            add_more = input(
                "Apakah mau menambahkan barang masuk lagi? (ya/tidak): "
            ).lower()
            if add_more != "ya":
                break
    else:
        print("Gagal membuat data bahan masuk baru.")


################################### BAHAN MASUK ################################################


################################### Detail BAHAN MASUK ################################################


def read_data_detail_bahan_masuk():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = "SELECT * FROM detail_bahan_masuk ORDER BY id_detail_bahan_masuk ASC"
        df = pd.read_sql_query(sql, conn)
        os.system("cls")
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_detail_bahan_masuk(
    id_bahan_masuk, id_supplier, id_ketersediaan_bahan, quantity, deskripsi
):
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO detail_bahan_masuk (id_bahan_masuk, id_supplier, id_ketersediaan_bahan, quantity, deskripsi)
        VALUES (%s, %s, %s, %s, %s)
        """
        cur = conn.cursor()
        cur.execute(
            sql,
            (id_bahan_masuk, id_supplier, id_ketersediaan_bahan, quantity, deskripsi),
        )
        conn.commit()
        cur.close()
        print("Data detail bahan masuk berhasil ditambahkan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_detail_bahan_masuk(id_detail_bahan_masuk):
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = "DELETE FROM detail_bahan_masuk WHERE id_detail_bahan_masuk = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_detail_bahan_masuk,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel detail_bahan_masuk.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_detail_bahan_masuk(
    id_detail_bahan_masuk,
    id_bahan_masuk,
    id_supplier,
    id_ketersediaan_bahan,
    quantity,
    deskripsi,
):
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = """
        UPDATE detail_bahan_masuk
        SET id_bahan_masuk = %s,
            id_supplier = %s,
            id_ketersediaan_bahan = %s,
            quantity = %s,
            deskripsi = %s
        WHERE id_detail_bahan_masuk = %s
        """
        cur = conn.cursor()
        cur.execute(
            sql,
            (
                id_bahan_masuk,
                id_supplier,
                id_ketersediaan_bahan,
                quantity,
                deskripsi,
                id_detail_bahan_masuk,
            ),
        )
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel detail_bahan_masuk.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### Detail BAHAN MASUK ################################################


################################### BAHAN Keluar ################################################
def read_data_bahan_keluar():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = "SELECT * FROM Bahan_Keluar ORDER BY id_bahan_keluar ASC"
        df = pd.read_sql_query(sql, conn)
        os.system("cls")
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_bahan_keluar(akun_id_akun):
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO bahan_keluar (akun_id_akun, tanggal)
        VALUES (%s, CURRENT_DATE)
        RETURNING id_bahan_keluar
        """
        cur = conn.cursor()
        cur.execute(sql, (akun_id_akun,))
        id_bahan_keluar_baru = cur.fetchone()[0]
        conn.commit()
        cur.close()
        print(
            f"Data bahan keluar berhasil ditambahkan dengan id: {id_bahan_keluar_baru}."
        )
        return id_bahan_keluar_baru
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_bahan_keluar(id_bahan_keluar):
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = "DELETE FROM Bahan_Keluar WHERE id_bahan_keluar = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_bahan_keluar,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel Bahan_Keluar.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_bahan_keluar():
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        read_data_bahan_keluar()
        id_bahan_keluar = input("Masukkan ID Bahan Keluar yang ingin diperbarui: ")
        read_data_akun()
        akun_id_akun = input("Masukkan ID Akun Baru: ")

        sql = """
        UPDATE Bahan_Keluar
        SET akun_id_akun = %s
        WHERE id_bahan_keluar = %s
        """
        cur = conn.cursor()
        cur.execute(sql, (akun_id_akun, id_bahan_keluar))
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel Bahan_Keluar.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def add_bahan_keluar_and_detail():
    os.system("cls")
    read_data_akun()
    akun_id_akun = int(input("Enter akun_id_akun: "))
    id_bahan_keluar_baru = insert_data_bahan_keluar(akun_id_akun)

    if id_bahan_keluar_baru is not None:
        while True:
            read_data_ketersediaan_bahan()
            id_ketersediaan_bahan = int(input("Enter id_ketersediaan_bahan: "))
            quantity = int(input("Enter quantity: "))
            deskripsi = input("Enter deskripsi: ")

            insert_data_detail_bahan_keluar(
                id_bahan_keluar_baru,
                id_ketersediaan_bahan,
                quantity,
                deskripsi,
            )

            add_more = input(
                "Apakah mau menambahkan barang keluar lagi? (ya/tidak): "
            ).lower()
            if add_more != "ya":
                break
    else:
        print("Gagal membuat data bahan keluar baru.")


################################### BAHAN Keluar ################################################


################################### Detail BAHAN KElUAR ################################################
def read_data_detail_bahan_keluar():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = "SELECT * FROM detail_bahan_keluar ORDER BY id_detail_bahan_keluar ASC"
        df = pd.read_sql_query(sql, conn)
        os.system("cls")
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_data_detail_bahan_keluar(
    id_bahan_keluar, id_ketersediaan_bahan, quantity, deskripsi
):
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO detail_bahan_keluar (id_bahan_keluar, id_ketersediaan_bahan, quantity, deskripsi)
        VALUES (%s, %s, %s, %s)
        """
        cur = conn.cursor()
        cur.execute(
            sql,
            (id_bahan_keluar, id_ketersediaan_bahan, quantity, deskripsi),
        )
        conn.commit()
        cur.close()
        print("Data detail bahan keluar berhasil ditambahkan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_detail_bahan_keluar(id_detail_bahan_keluar):
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = "DELETE FROM detail_bahan_keluar WHERE id_detail_bahan_keluar = %s"
        cur = conn.cursor()
        cur.execute(sql, (id_detail_bahan_keluar,))
        conn.commit()
        cur.close()
        print("Data berhasil dihapus dari tabel detail_bahan_keluar.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def update_data_detail_bahan_keluar(
    id_detail_bahan_keluar,
    id_bahan_keluar,
    id_ketersediaan_bahan,
    quantity,
    deskripsi,
):
    os.system("cls")
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = """
        UPDATE detail_bahan_keluar
        SET id_bahan_keluar = %s,
            id_ketersediaan_bahan = %s,
            quantity = %s,
            deskripsi = %s
        WHERE id_detail_bahan_keluar = %s
        """
        cur = conn.cursor()
        cur.execute(
            sql,
            (
                id_bahan_keluar,
                id_ketersediaan_bahan,
                quantity,
                deskripsi,
                id_detail_bahan_keluar,
            ),
        )
        conn.commit()
        cur.close()
        print("Data berhasil diupdate pada tabel detail_bahan_keluar.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### Detail BAHAN KELUAR ################################################


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
        namafile = "tampilan/login.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

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
        namafile = "tampilan/allfitur_owner.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("pilih opsi: ")
        if user_input == "1":
            menu_crud_bahan_masuk_owner()
        elif user_input == "2":
            menu_crud_bahan_keluar_owner()
        elif user_input == "3":
            menu_crud_ketersediaan_bahan_owner()
        elif user_input == "4":
            fiturpokok_owner()
        elif user_input == "5":
            daftar_Tambah_Data()
        elif user_input == "6":
            namatampilan = "tampilan/logout.txt"
            with open(namatampilan, "r") as file:
                core_file = file.read()
                print(core_file)
            sys.exit()
        elif user_input == "7":
            main()
        else:
            print("Pilihan invalid")


################################### ONLY FOR OWNER ################################################


################################### ONLY FOR STAFF ################################################
def allfitur_Staff():
    os.system("cls")
    while True:
        namafile = "tampilan/allfitur_staff.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("pilih opsi: ")
        if user_input == "1":
            menu_crud_bahan_masuk_staff()
        elif user_input == "2":
            menu_crud_bahan_keluar_staff()
        elif user_input == "3":
            menu_crud_ketersediaan_bahan_staff()
        elif user_input == "4":
            fiturpokok_staff()
        elif user_input == "5":
            namatampilan = "tampilan/logout.txt"
            with open(namatampilan, "r", encoding="utf-8") as file:
                core_file = file.read()
                print(core_file)
            sys.exit()
        elif user_input == "6":
            main()
        else:
            print("Pilihan invalid")


################################### ONLY FOR STAFF ################################################


################################### MENU CRUD AKUN ################################################
def daftar_Tambah_Data():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_no_hapus.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih opsi: ")
        if user_input == "1":
            read_data_akun()
        elif user_input == "2":
            insert_data_akun()
        elif user_input == "3":
            update_data_akun()
        elif user_input == "4":
            allfitur_Owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD AKUN ################################################


################################### Fitur Pokok For owner ################################################
def fiturpokok_owner():
    os.system("cls")
    while True:
        namafile = "tampilan/fitur_pokok_owner.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            menu_crud_role()
        elif user_input == "2":
            menu_crud_jenis_kelamin()
        elif user_input == "3":
            menu_crud_kecamatan()
        elif user_input == "4":
            menu_crud_merk()
        elif user_input == "5":
            menu_crud_supplier()
        elif user_input == "6":
            menu_crud_jenis_bahan()
        elif user_input == "7":
            allfitur_Owner()
        else:
            print("Opsi Tidak valid")


################################### Fitur Pokok For Owner ################################################


################################### Fitur Pokok For Staff ################################################
def fiturpokok_staff():
    os.system("cls")
    while True:
        namafile = "tampilan/fitur_pokok_staff.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_merk()
        elif user_input == "2":
            read_data_supplier()
        elif user_input == "3":
            read_data_jenis_bahan()
        elif user_input == "4":
            allfitur_Staff()
        else:
            print("Opsi Tidak valid")


################################### Fitur Pokok For Staff ################################################


################################### MENU CRUD ROLE ################################################
def menu_crud_role():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_no_hapus.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_role()
        elif user_input == "2":
            insert_data_role()
        elif user_input == "3":
            update_data_role()
        elif user_input == "4":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD ROLE ################################################


################################### MENU CRUD Jenis_Kelamin ################################################
def menu_crud_jenis_kelamin():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_no_hapus.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")
        if user_input == "1":
            read_data_jenis_kelamin()
        elif user_input == "2":
            insert_data_jenis_kelamin()
        elif user_input == "3":
            update_data_jenis_kelamin()
        elif user_input == "4":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Jenis_Kelamin ################################################


################################### MENU CRUD Kecamatan ################################################
def menu_crud_kecamatan():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_no_hapus.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")
        if user_input == "1":
            read_data_kecamatan()
        elif user_input == "2":
            insert_data_kecamatan()
        elif user_input == "3":
            update_data_kecamatan()
        elif user_input == "4":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Kecamatan ################################################


################################### MENU CRUD MERK ################################################
def menu_crud_merk():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_no_hapus.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_merk()
        elif user_input == "2":
            insert_data_merk()
        elif user_input == "3":
            update_data_merk()
        elif user_input == "4":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD MERK ################################################


################################### MENU CRUD Supplier ################################################
def menu_crud_supplier():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_supplier()
        elif user_input == "2":
            insert_data_supplier()
        elif user_input == "3":
            update_data_supplier()
        elif user_input == "4":
            delete_data_supplier()
        elif user_input == "5":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Supplier ################################################


################################### MENU CRUD Jenis Bahan ################################################
def menu_crud_jenis_bahan():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_no_hapus.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_jenis_bahan()
        elif user_input == "2":
            insert_data_jenis_bahan()
        elif user_input == "3":
            update_data_jenis_bahan()
        elif user_input == "4":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Jenis Bahan ################################################


################################### MENU CRUD Ketersediaan Bahan Owner ################################################
def menu_crud_ketersediaan_bahan_owner():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_ketersediaan_bahan()
        elif user_input == "2":
            insert_data_ketersediaan_bahan()
        elif user_input == "3":
            update_data_ketersediaan_bahan()
        elif user_input == "4":
            delete_data_ketersediaan_bahan()
        elif user_input == "5":
            allfitur_Owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Ketersediaan Bahan owner################################################


################################### MENU CRUD Ketersediaan Bahan staff ################################################
def menu_crud_ketersediaan_bahan_staff():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_ketersediaan_bahan()
        elif user_input == "2":
            insert_data_ketersediaan_bahan()
        elif user_input == "3":
            update_data_ketersediaan_bahan()
        elif user_input == "4":
            delete_data_ketersediaan_bahan()
        elif user_input == "5":
            allfitur_Staff()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Ketersediaan Bahan staff ################################################


################################### MENU CRUD Bahan Masuk Owner ################################################
def menu_crud_bahan_masuk_owner():
    os.system("cls")
    while True:
        namafile = "tampilan/spesial_crud_bahan_masuk.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_bahan_masuk()
        elif user_input == "2":
            add_bahan_masuk_and_detail()
        elif user_input == "3":
            update_data_bahan_masuk()
        elif user_input == "4":
            menu_crud_detail_bahan_masuk_owner()
        elif user_input == "5":
            allfitur_Owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Bahan Masuk owner################################################


################################### MENU CRUD Bahan Masuk staff ################################################
def menu_crud_bahan_masuk_staff():
    os.system("cls")
    while True:
        namafile = "tampilan/spesial_crud_bahan_masuk.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_bahan_masuk()
        elif user_input == "2":
            add_bahan_masuk_and_detail()
        elif user_input == "3":
            update_data_bahan_masuk()
        elif user_input == "4":
            menu_crud_detail_bahan_masuk_owner()
        elif user_input == "5":
            allfitur_Staff()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Bahan Masuk staff ################################################


################################### MENU CRUD Bahan Keluar Owner ################################################
def menu_crud_bahan_keluar_owner():
    os.system("cls")
    while True:
        namafile = "tampilan/spesial_crud_bahan_keluar.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_bahan_keluar()
        elif user_input == "2":
            add_bahan_keluar_and_detail()
        elif user_input == "3":
            update_data_bahan_keluar()
        elif user_input == "4":
            menu_crud_detail_bahan_keluar_owner()
        elif user_input == "5":
            allfitur_Owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Bahan Keluar staff ################################################


def menu_crud_bahan_keluar_staff():
    os.system("cls")
    while True:
        namafile = "tampilan/spesial_crud_bahan_keluar.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_bahan_keluar()
        elif user_input == "2":
            add_bahan_keluar_and_detail()
        elif user_input == "3":
            update_data_bahan_keluar()
        elif user_input == "4":
            menu_crud_detail_bahan_keluar_staff()
        elif user_input == "5":
            allfitur_Staff()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Bahan Keluar staff ################################################


################################### MENU CRUD Detail bahan masuk owner ################################################
def menu_crud_detail_bahan_masuk_owner():
    os.system("cls")
    while True:
        namafile = "tampilan/detail_bahan_masuk.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_detail_bahan_masuk()
        elif user_input == "2":
            menu_crud_bahan_masuk_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Detail bahan masuk owner ################################################


################################### MENU CRUD Detail bahan masuk staff ################################################
def menu_crud_detail_bahan_masuk_staff():
    os.system("cls")
    while True:
        namafile = "tampilan/detail_bahan_masuk.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_detail_bahan_masuk()
        elif user_input == "2":
            menu_crud_bahan_masuk_staff()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Detail bahan masuk staff ################################################


################################### MENU CRUD Detail bahan keluar owner ################################################
def menu_crud_detail_bahan_keluar_owner():
    os.system("cls")
    while True:
        namafile = "tampilan/detail_bahan_keluar.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_detail_bahan_keluar()
        elif user_input == "2":
            menu_crud_bahan_keluar_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Detail bahan keluar owner ################################################


################################### MENU CRUD Detail bahan keluar staff ################################################
def menu_crud_detail_bahan_keluar_staff():
    os.system("cls")
    while True:
        namafile = "tampilan/detail_bahan_keluar.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_detail_bahan_keluar()
        elif user_input == "2":
            menu_crud_bahan_keluar_staff()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Detail bahan keluar staff ################################################
if __name__ == "__main__":
    main()
