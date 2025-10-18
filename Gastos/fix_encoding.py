import os
import sys

# Forzar codificación a nivel de sistema antes de importar psycopg2
if sys.platform == 'win32':
    # Cambiar la codificación de Windows temporalmente
    import ctypes
    kernel32 = ctypes.windll.kernel32
    # Guardar la codepage original
    original_cp = kernel32.GetConsoleOutputCP()
    # Cambiar a UTF-8
    kernel32.SetConsoleOutputCP(65001)
    
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    os.environ['PGCLIENTENCODING'] = 'UTF8'

print("Intentando conectar con codificación forzada...")

try:
    import psycopg2
    
    # Usar URI de conexión en lugar de parámetros separados
    conn = psycopg2.connect("dbname=gastosdb user=postgres password=kevinaso host=127.0.0.1 port=5432 client_encoding=utf8")
    print("✓ Conexión exitosa usando URI")
    
    cursor = conn.cursor()
    cursor.execute('SELECT version();')
    db_version = cursor.fetchone()
    print(f"✓ PostgreSQL version: {db_version[0]}")
    
    cursor.close()
    conn.close()
    print("✓ Todo funcionó correctamente")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()

finally:
    # Restaurar codepage original
    if sys.platform == 'win32':
        kernel32.SetConsoleOutputCP(original_cp)