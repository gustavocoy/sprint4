from psycopg2 import connect


HOST= 'ec2-3-219-19-205.compute-1.amazonaws.com'
PORT= 5432
BD='d91t7bh2o3rh73'
USUARIO='sppvthzlzgwcje'
PASSWORD='cd39e0a21c79d90008e57cef24554e24b4b078af920ef20910206bd0a65028dd'

# HOST= 'localhost'
# PORT= 8080
# BD='turismo'
# USUARIO='root'
# PASSWORD=''

def EstablecerConexion():
    try:
        conexion=connect(host=HOST, port=PORT, database=BD, user=USUARIO, password=PASSWORD)
        return conexion
    except Exception as e:
        print(e)
        return None
    
   