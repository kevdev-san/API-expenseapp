import os
import sys

# Forzar codificación
os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['PGCLIENTENCODING'] = 'UTF8'

print("Intentando conectar a PostgreSQL...")
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")

# Importar psycopg2 con manejo de errores
try:
    import psycopg2
    print(f"psycopg2 version: {psycopg2.__version__}")
    
    # Intenta conectar
    conn = psycopg2.connect(
        host='127.0.0.1',
        port='5432',
        database='gastosdb',
        user='postgres',
        password='kevinaso',  # Tu contraseña actual
        client_encoding='UTF8'
    )
    print("✓ Conexión exitosa a PostgreSQL")
    
    # Probar una consulta simple
    cursor = conn.cursor()
    cursor.execute('SELECT version();')
    db_version = cursor.fetchone()
    print(f"✓ PostgreSQL version: {db_version[0]}")
    
    cursor.close()
    conn.close()
    print("✓ Conexión cerrada correctamente")
    
except Exception as e:
    print(f"✗ Error: {e}")
    print(f"✗ Tipo de error: {type(e).__name__}")
    import traceback
    traceback.print_exc()