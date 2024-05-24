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

        sql = "SELECT * FROM role ORDER BY id_role ASC"
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

        sql = "SELECT * FROM alamat ORDER BY Id_Alamat"
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


################################### MERK ################################################
def insert_data_merk(id_merk, nama_merk):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO Merk (Id_Merk, Nama_Merk)
        VALUES (%s, %s)
        """
        cur = conn.cursor()
        cur.execute(sql, (id_merk, nama_merk))
        conn.commit()
        cur.close()
        print("Data berhasil ditambahkan ke tabel Merk.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def delete_data_merk(id_merk):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

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


def update_data_merk(id_merk, nama_merk):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

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


def read_data_merk():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM Merk ORDER BY Id_Merk"
        df = pd.read_sql_query(sql, conn)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


################################### MERK ################################################


################################### Supplier ################################################
def insert_data_supplier(id_supplier, nama_supplier):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO Supplier (id_supplier, nama_supplier)
        VALUES (%s, %s)
        """
        cur = conn.cursor()
        cur.execute(sql, (id_supplier, nama_supplier))
        conn.commit()
        cur.close()
        print("Data berhasil ditambahkan ke tabel Supplier.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


# Fungsi untuk membaca data supplier
def read_data_supplier():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM Supplier ORDER BY id_supplier"
        df = pd.read_sql_query(sql, conn)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


# Fungsi untuk memperbarui data supplier
def update_data_supplier(id_supplier, nama_supplier):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

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


# Fungsi untuk menghapus data supplier
def delete_data_supplier(id_supplier):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

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


################################### Supplier ################################################


################################### Jenis Bahan ################################################
def insert_data_jenis_bahan(id_jenis_bahan, nama_jenis):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO Jenis_Bahan (id_jenis_bahan, nama_jenis)
        VALUES (%s, %s)
        """
        cur = conn.cursor()
        cur.execute(sql, (id_jenis_bahan, nama_jenis))
        conn.commit()
        cur.close()
        print("Data berhasil ditambahkan ke tabel Jenis_Bahan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


# Fungsi untuk membaca data jenis bahan
def read_data_jenis_bahan():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM Jenis_Bahan ORDER BY id_jenis_bahan"
        df = pd.read_sql_query(sql, conn)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


# Fungsi untuk memperbarui data jenis bahan
def update_data_jenis_bahan(id_jenis_bahan, nama_jenis):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

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


# Fungsi untuk menghapus data jenis bahan
def delete_data_jenis_bahan(id_jenis_bahan):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

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
# Fungsi untuk membaca data dari tabel Ketersediaan_Bahan
def read_data_ketersediaan_bahan():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM Ketersediaan_Bahan ORDER BY id_ketersediaan_bahan ASC"
        df = pd.read_sql_query(sql, conn)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


# Fungsi untuk menambahkan data ke tabel Ketersediaan_Bahan
def insert_data_ketersediaan_bahan(
    id_ketersediaan_bahan,
    nama_bahan,
    stock,
    deskripsi,
    jenis_bahan_id_jenis_bahan,
    merk_id_merk,
):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO Ketersediaan_Bahan (id_ketersediaan_bahan, nama_bahan, stock, deskripsi, jenis_bahan_id_jenis_bahan, merk_id_merk)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur = conn.cursor()
        cur.execute(
            sql,
            (
                id_ketersediaan_bahan,
                nama_bahan,
                stock,
                deskripsi,
                jenis_bahan_id_jenis_bahan,
                merk_id_merk,
            ),
        )
        conn.commit()
        cur.close()
        print("Data berhasil ditambahkan ke tabel Ketersediaan_Bahan.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


# Fungsi untuk menghapus data dari tabel Ketersediaan_Bahan
def delete_data_ketersediaan_bahan(id_ketersediaan_bahan):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

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


# Fungsi untuk memperbarui data pada tabel Ketersediaan_Bahan
def update_data_ketersediaan_bahan(
    id_ketersediaan_bahan,
    nama_bahan,
    stock,
    deskripsi,
    jenis_bahan_id_jenis_bahan,
    merk_id_merk,
):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

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
# Fungsi untuk membaca data dari tabel Bahan_Masuk
def read_data_bahan_masuk():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM Bahan_Masuk ORDER BY id_bahan_masuk ASC"
        df = pd.read_sql_query(sql, conn)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


# Fungsi untuk menambahkan data ke tabel Bahan_Masuk
def insert_data_bahan_masuk(id_bahan_masuk, akun_id_akun):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        # Mendapatkan tanggal saat ini
        tanggal = datetime.now().date()

        sql = """
        INSERT INTO Bahan_Masuk (id_bahan_masuk, akun_id_akun, tanggal)
        VALUES (%s, %s, %s)
        """
        cur = conn.cursor()
        cur.execute(sql, (id_bahan_masuk, akun_id_akun, tanggal))
        conn.commit()
        cur.close()
        print("Data berhasil ditambahkan ke tabel Bahan_Masuk.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


# Fungsi untuk menghapus data dari tabel Bahan_Masuk
def delete_data_bahan_masuk(id_bahan_masuk):
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


# Fungsi untuk memperbarui data pada tabel Bahan_Masuk
def update_data_bahan_masuk(id_bahan_masuk, akun_id_akun):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

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


################################### BAHAN MASUK ################################################


################################### Detail BAHAN MASUK ################################################
def read_data_detail_bahan_masuk():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = "SELECT * FROM detail_bahan_masuk ORDER BY id_detail_bahan_masuk ASC"
        df = pd.read_sql_query(sql, conn)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


# Fungsi untuk menambahkan data ke tabel detail_bahan_masuk
def insert_data_detail_bahan_masuk(
    id_detail_bahan_masuk,
    id_bahan_masuk,
    id_supplier,
    id_ketersediaan_bahan,
    quantity,
    deskripsi,
):
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)

        sql = """
        INSERT INTO detail_bahan_masuk (id_detail_bahan_masuk, id_bahan_masuk, id_supplier, id_ketersediaan_bahan, quantity, deskripsi)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur = conn.cursor()
        cur.execute(
            sql,
            (
                id_detail_bahan_masuk,
                id_bahan_masuk,
                id_supplier,
                id_ketersediaan_bahan,
                quantity,
                deskripsi,
            ),
        )
        conn.commit()
        cur.close()
        print(
            f"Data berhasil ditambahkan ke tabel detail_bahan_masuk dengan ID: {id_detail_bahan_masuk}"
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


# Fungsi untuk menghapus data dari tabel detail_bahan_masuk
def delete_data_detail_bahan_masuk(id_detail_bahan_masuk):
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


# Fungsi untuk memperbarui data pada tabel detail_bahan_masuk
def update_data_detail_bahan_masuk(
    id_detail_bahan_masuk,
    id_bahan_masuk,
    id_supplier,
    id_ketersediaan_bahan,
    quantity,
    deskripsi,
):
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
            print("belum ada fitur")
        elif user_input == "3":
            menu_crud_ketersediaan_bahan_owner()
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
        namafile = "tampilan/allfitur_staff.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("pilih opsi: ")
        if user_input == "1":
            menu_crud_bahan_masuk_staff()
        elif user_input == "2":
            print("belum ada fitur")
        elif user_input == "3":
            menu_crud_ketersediaan_bahan_staff()
        elif user_input == "4":
            fiturpokok_staff()
        elif user_input == "5":
            sys.exit()
        else:
            print("Pilihan invalid")


################################### ONLY FOR STAFF ################################################


################################### MENU CRUD AKUN ################################################
def daftar_Tambah_Data():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

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
            menu_crud_kelurahan()
        elif user_input == "5":
            menu_crud_alamat()
        elif user_input == "6":
            menu_crud_merk()
        elif user_input == "7":
            menu_crud_supplier()
        elif user_input == "8":
            menu_crud_jenis_bahan()
        elif user_input == "9":
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
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

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
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

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
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

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
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

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
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

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


################################### MENU CRUD MERK ################################################
def menu_crud_merk():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_merk()
        elif user_input == "2":
            id_merk = input("Masukkan Id Merk: ")
            nama_merk = input("Masukkan Nama Merk: ")
            insert_data_merk(id_merk, nama_merk)
        elif user_input == "3":
            id_merk = input("Masukkan Id Merk yang ingin diperbarui: ")
            nama_merk = input("Masukkan Nama Merk Baru: ")
            update_data_merk(id_merk, nama_merk)
        elif user_input == "4":
            id_merk = input("Masukkan Id Merk yang ingin dihapus: ")
            delete_data_merk(id_merk)
        elif user_input == "5":
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
            id_supplier = input("Masukkan ID Supplier: ")
            nama_supplier = input("Masukkan Nama Supplier: ")
            insert_data_supplier(id_supplier, nama_supplier)
        elif user_input == "3":
            id_supplier = input("Masukkan ID Supplier yang ingin diperbarui: ")
            nama_supplier = input("Masukkan Nama Supplier Baru: ")
            update_data_supplier(id_supplier, nama_supplier)
        elif user_input == "4":
            id_supplier = input("Masukkan ID Supplier yang ingin dihapus: ")
            delete_data_supplier(id_supplier)
        elif user_input == "5":
            fiturpokok_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Supplier ################################################


################################### MENU CRUD Jenis Bahan ################################################
def menu_crud_jenis_bahan():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_jenis_bahan()
        elif user_input == "2":
            id_jenis_bahan = input("Masukkan ID Jenis Bahan: ")
            nama_jenis = input("Masukkan Nama Jenis Bahan: ")
            insert_data_jenis_bahan(id_jenis_bahan, nama_jenis)
        elif user_input == "3":
            id_jenis_bahan = input("Masukkan ID Jenis Bahan yang ingin diperbarui: ")
            nama_jenis = input("Masukkan Nama Jenis Bahan Baru: ")
            update_data_jenis_bahan(id_jenis_bahan, nama_jenis)
        elif user_input == "4":
            id_jenis_bahan = input("Masukkan ID Jenis Bahan yang ingin dihapus: ")
            delete_data_jenis_bahan(id_jenis_bahan)
        elif user_input == "5":
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
            id_ketersediaan_bahan = input("Masukkan ID Ketersediaan Bahan: ")
            nama_bahan = input("Masukkan Nama Bahan: ")
            stock = input("Masukkan Stock: ")
            deskripsi = input("Masukkan Deskripsi: ")
            jenis_bahan_id_jenis_bahan = input("Masukkan ID Jenis Bahan: ")
            merk_id_merk = input("Masukkan ID Merk: ")
            insert_data_ketersediaan_bahan(
                id_ketersediaan_bahan,
                nama_bahan,
                stock,
                deskripsi,
                jenis_bahan_id_jenis_bahan,
                merk_id_merk,
            )
        elif user_input == "3":
            id_ketersediaan_bahan = input(
                "Masukkan ID Ketersediaan Bahan yang ingin diperbarui: "
            )
            nama_bahan = input("Masukkan Nama Bahan Baru: ")
            stock = input("Masukkan Stock Baru: ")
            deskripsi = input("Masukkan Deskripsi Baru: ")
            jenis_bahan_id_jenis_bahan = input("Masukkan ID Jenis Bahan Baru: ")
            merk_id_merk = input("Masukkan ID Merk Baru: ")
            update_data_ketersediaan_bahan(
                id_ketersediaan_bahan,
                nama_bahan,
                stock,
                deskripsi,
                jenis_bahan_id_jenis_bahan,
                merk_id_merk,
            )
        elif user_input == "4":
            id_ketersediaan_bahan = input(
                "Masukkan ID Ketersediaan Bahan yang ingin dihapus: "
            )
            delete_data_ketersediaan_bahan(id_ketersediaan_bahan)
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
            id_ketersediaan_bahan = input("Masukkan ID Ketersediaan Bahan: ")
            nama_bahan = input("Masukkan Nama Bahan: ")
            stock = input("Masukkan Stock: ")
            deskripsi = input("Masukkan Deskripsi: ")
            jenis_bahan_id_jenis_bahan = input("Masukkan ID Jenis Bahan: ")
            merk_id_merk = input("Masukkan ID Merk: ")
            insert_data_ketersediaan_bahan(
                id_ketersediaan_bahan,
                nama_bahan,
                stock,
                deskripsi,
                jenis_bahan_id_jenis_bahan,
                merk_id_merk,
            )
        elif user_input == "3":
            id_ketersediaan_bahan = input(
                "Masukkan ID Ketersediaan Bahan yang ingin diperbarui: "
            )
            nama_bahan = input("Masukkan Nama Bahan Baru: ")
            stock = input("Masukkan Stock Baru: ")
            deskripsi = input("Masukkan Deskripsi Baru: ")
            jenis_bahan_id_jenis_bahan = input("Masukkan ID Jenis Bahan Baru: ")
            merk_id_merk = input("Masukkan ID Merk Baru: ")
            update_data_ketersediaan_bahan(
                id_ketersediaan_bahan,
                nama_bahan,
                stock,
                deskripsi,
                jenis_bahan_id_jenis_bahan,
                merk_id_merk,
            )
        elif user_input == "4":
            id_ketersediaan_bahan = input(
                "Masukkan ID Ketersediaan Bahan yang ingin dihapus: "
            )
            delete_data_ketersediaan_bahan(id_ketersediaan_bahan)
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
            id_bahan_masuk = input("Masukkan ID Bahan Masuk: ")
            akun_id_akun = input("Masukkan ID Akun: ")
            insert_data_bahan_masuk(id_bahan_masuk, akun_id_akun)
        elif user_input == "3":
            id_bahan_masuk = input("Masukkan ID Bahan Masuk yang ingin diperbarui: ")
            akun_id_akun = input("Masukkan ID Akun Baru: ")
            update_data_bahan_masuk(id_bahan_masuk, akun_id_akun)
        elif user_input == "4":
            id_bahan_masuk = input("Masukkan ID Bahan Masuk yang ingin dihapus: ")
            delete_data_bahan_masuk(id_bahan_masuk)
        elif user_input == "5":
            menu_crud_detail_bahan_masuk_owner()
        elif user_input == "6":
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
            id_bahan_masuk = input("Masukkan ID Bahan Masuk: ")
            akun_id_akun = input("Masukkan ID Akun: ")
            insert_data_bahan_masuk(id_bahan_masuk, akun_id_akun)
        elif user_input == "3":
            id_bahan_masuk = input("Masukkan ID Bahan Masuk yang ingin diperbarui: ")
            akun_id_akun = input("Masukkan ID Akun Baru: ")
            update_data_bahan_masuk(id_bahan_masuk, akun_id_akun)
        elif user_input == "4":
            id_bahan_masuk = input("Masukkan ID Bahan Masuk yang ingin dihapus: ")
            delete_data_bahan_masuk(id_bahan_masuk)
        elif user_input == "5":
            menu_crud_detail_bahan_masuk_owner()
        elif user_input == "6":
            allfitur_Staff()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Bahan Masuk staff ################################################


################################### MENU CRUD Detail bahan masuk owner ################################################
def menu_crud_detail_bahan_masuk_owner():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_detail_bahan_masuk()
        elif user_input == "2":
            id_detail_bahan_masuk = input("Masukkan ID Detail Bahan Masuk: ")
            id_bahan_masuk = input("Masukkan ID Bahan Masuk: ")
            id_supplier = input("Masukkan ID Supplier: ")
            id_ketersediaan_bahan = input("Masukkan ID Ketersediaan Bahan: ")
            quantity = input("Masukkan Quantity: ")
            deskripsi = input("Masukkan Deskripsi (opsional): ")
            insert_data_detail_bahan_masuk(
                id_detail_bahan_masuk,
                id_bahan_masuk,
                id_supplier,
                id_ketersediaan_bahan,
                quantity,
                deskripsi,
            )
        elif user_input == "3":
            id_detail_bahan_masuk = input(
                "Masukkan ID Detail Bahan Masuk yang ingin diperbarui: "
            )
            id_bahan_masuk = input("Masukkan ID Bahan Masuk Baru: ")
            id_supplier = input("Masukkan ID Supplier Baru: ")
            id_ketersediaan_bahan = input("Masukkan ID Ketersediaan Bahan Baru: ")
            quantity = input("Masukkan Quantity Baru: ")
            deskripsi = input("Masukkan Deskripsi Baru (opsional): ")
            update_data_detail_bahan_masuk(
                id_detail_bahan_masuk,
                id_bahan_masuk,
                id_supplier,
                id_ketersediaan_bahan,
                quantity,
                deskripsi,
            )
        elif user_input == "4":
            id_detail_bahan_masuk = input(
                "Masukkan ID Detail Bahan Masuk yang ingin dihapus: "
            )
            delete_data_detail_bahan_masuk(id_detail_bahan_masuk)
        elif user_input == "5":
            menu_crud_bahan_masuk_owner()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Detail bahan masuk owner ################################################


################################### MENU CRUD Detail bahan keluar owner ################################################
def menu_crud_detail_bahan_masuk_keluar():
    os.system("cls")
    while True:
        namafile = "tampilan/all_menu_crud.txt"
        with open(namafile, "r") as file:
            isi_file = file.read()
            print(isi_file)

        user_input = input("Pilih Opsi: ")

        if user_input == "1":
            read_data_detail_bahan_masuk()
        elif user_input == "2":
            id_detail_bahan_masuk = input("Masukkan ID Detail Bahan Masuk: ")
            id_bahan_masuk = input("Masukkan ID Bahan Masuk: ")
            id_supplier = input("Masukkan ID Supplier: ")
            id_ketersediaan_bahan = input("Masukkan ID Ketersediaan Bahan: ")
            quantity = input("Masukkan Quantity: ")
            deskripsi = input("Masukkan Deskripsi (opsional): ")
            insert_data_detail_bahan_masuk(
                id_detail_bahan_masuk,
                id_bahan_masuk,
                id_supplier,
                id_ketersediaan_bahan,
                quantity,
                deskripsi,
            )
        elif user_input == "3":
            id_detail_bahan_masuk = input(
                "Masukkan ID Detail Bahan Masuk yang ingin diperbarui: "
            )
            id_bahan_masuk = input("Masukkan ID Bahan Masuk Baru: ")
            id_supplier = input("Masukkan ID Supplier Baru: ")
            id_ketersediaan_bahan = input("Masukkan ID Ketersediaan Bahan Baru: ")
            quantity = input("Masukkan Quantity Baru: ")
            deskripsi = input("Masukkan Deskripsi Baru (opsional): ")
            update_data_detail_bahan_masuk(
                id_detail_bahan_masuk,
                id_bahan_masuk,
                id_supplier,
                id_ketersediaan_bahan,
                quantity,
                deskripsi,
            )
        elif user_input == "4":
            id_detail_bahan_masuk = input(
                "Masukkan ID Detail Bahan Masuk yang ingin dihapus: "
            )
            delete_data_detail_bahan_masuk(id_detail_bahan_masuk)
        elif user_input == "5":
            menu_crud_bahan_masuk_staff()
        else:
            print("Opsi Tidak valid")


################################### MENU CRUD Detail bahan keluar owner ################################################

if __name__ == "__main__":
    main()
