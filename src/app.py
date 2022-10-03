from flask import Flask, render_template, url_for , flash, request, redirect, session
from psycopg2 import connect
from config import *
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required


app = Flask(__name__)

app.secret_key='12345'

con_db = EstablecerConexion()




#rutas de la pagina principal
@app.route("/")
def index():
    cursor=con_db.cursor()
    sql= "SELECT*FROM atractivos"
    cursor.execute(sql)
    atractivosRegistradas=cursor.fetchall()
    print("inicio de la página")
    return render_template('index.html',atractivos=atractivosRegistradas)

@app.route("/contacto")
def contacto():
    cursor=con_db.cursor()
    sql= "SELECT*FROM integrantes"
    cursor.execute(sql)
    integrantesRegistrados=cursor.fetchall()
    print("este es el contacto")
    return render_template('contacto.html',integrantes=integrantesRegistrados)

@app.route("/atractivos")
def atractivos():
	print("Llegamos a atractivos")
	return render_template("atractivos.html")

@app.route("/ingreso")
def ingreso():
	print("Llegamos a ingreso")
	return render_template("ingreso.html") 

@app.route("/registro")
def registro():
	print("Llegamos a registro")
	return render_template("registro.html")

@app.route("/agregaratractivos")
def agregaratractivos():
	print("estamos agregando atractivos")
	return render_template("agregaratractivos.html")

@app.route("/admin")
def admin():
	print("estamos en la de admin")
	return render_template("admin.html")

# metodos

@app.route("/registrar", methods=['POST'])
def registrarse():
	if request.method == 'POST':
		nombre = request.form['nombre']
		correo = request.form['correo']
		contraseña1 = request.form['contraseña1']
		contraseña2 = request.form['contraseña2']
		if (contraseña1==contraseña2):
			create_table_registro()
			cur = con_db.cursor()
			cur.execute("INSERT INTO registros (nombre, correo, contraseña) VALUES (%s, %s, %s)", (nombre, correo, contraseña1))
			con_db.commit()
			flash("registro de usuarios")
			return redirect(url_for('registro'))
  		
		else:
			flash("Las contraseñas no coinciden")
			return redirect(url_for('registro'))

# def test_modify_session(client):
#     with client.session_transaction() as session:
#         # set a user id without going through the login route
#         session["admin"] = 1

#     # session is saved now

#     response = client.get("/users/me")
#     assert response.json["username"] == "flask"

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         # print(request.form['username'])
#         # print(request.form['password'])
#         user = User(0, request.form['username'], request.form['password'])
#         logged_user = ModelUser.login(db, user)
#         if logged_user != None:
#             if logged_user.password:
#                 login_user(logged_user)
#                 return redirect(url_for('home'))
#             else:
#                 flash("Invalid password...")
#                 return render_template('auth/login.html')
#         else:
#             flash("User not found...")
#             return render_template('auth/login.html')
#     else:
#         return render_template('auth/login.html')

@app.route("/ingresar", methods=['GET', 'POST'])
def ingresars():
	if request.method == 'POST':
		nombref = request.form['nombre']
		contraseñaf = request.form['contraseña']
		cur = con_db.cursor()
		cur.execute("SELECT * FROM registros WHERE nombre = %s AND contraseña = %s", (nombref, contraseñaf))
		data = cur.fetchall()
		print("_-----------------------------------")
		print(data)
		if len(data) > 0:
			print("si hay datos")
			return redirect(url_for('admin'))
		else:
			flash("Datos no encontrados")
			return redirect(url_for('ingreso'))
        #  if (admin==1):
        #      flash("ingresa")
        #      print(sql)
        #      return redirect(url_for('agregaratractivos'))
         
        #  if nombref and contraseñaf:
        #     FROM registros
        #      	sql="""SELECT correo 
        #      		WHERE nombre AND contraseña ='{}'"""
        #      	cursor.execute(sql)
        #      	row=cursor.fetchone()
        #      if row != 0:
        #          print(cursor)
        #          print()
        #          print()
        #          return redirect(url_for('admin'))
            
#              return "error, los datos ingresados no son válidos"
#             else:
#         else:
#     	    return "error en la consulta"

@app.route("/guardar_atractivo", methods=['POST'])
def guardar_atractivos():
	if request.method == 'POST':
		nombre = request.form['nombre']
		municipio = request.form['municipio']
		descripcion = request.form['descripcion']
		# create_table()
		cur = con_db.cursor()
		cur.execute("INSERT INTO atractivos (nombre, municipio, descripcion) VALUES (%s, %s, %s)", (nombre, municipio, descripcion))
		con_db.commit()
		flash("Solicitud enviada con éxito atractivos")
		return redirect(url_for('agregaratractivos'))
	

@app.route("/guardar_peticion", methods=['POST'])
def guardar_peticiones():
	if request.method == 'POST':
		nombre = request.form['nombre']
		apellido = request.form['apellido']
		edad = request.form['edad']
		correo = request.form['correo']
		peticion=request.form['peticion']
		# create_table()
		cur = con_db.cursor()
		cur.execute("INSERT INTO peticion (nombre, apellido, edad, peticion,correo) VALUES (%s, %s, %s,%s,%s)", (nombre, apellido, edad, peticion,correo))
		con_db.commit()
		flash("Solicitud enviada con éxito")
		return redirect(url_for('contacto'))

@app.route('/eliminar_atractivo/<int:id_atractivo>')
def eliminar(id_atractivo):
    cursor=con_db.cursor()
    sql="DELETE FROM atractivos WHERE id ={0}".format(id_atractivo)
    cursor.execute(sql)
    con_db.commit()
    return redirect(url_for('index'))
    
@app.route('/editar_atractivo/<int:id_atractivo>', methods=['POST'])
def editar(id_atractivo):
    cursor = con_db.cursor()
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    if nombre and apellido and edad:
        sql="UPDATE atractivos SET nombre=%s, apellido=%s, edad=%s WHERE id=%s"
        cursor.execute(sql,(nombre,apellido,edad,id_atractivo))
        con_db.commit()
        return redirect(url_for('index'))
    else:
    	return "error en la consulta" 
    
    
@app.route("/listar_atractivos")
def listar_atractivos():
	cur = con_db.cursor()
	cur.execute("SELECT * FROM atractivos")
	data = cur.fetchall()
	print(data)
	return render_template("ver.html", atractivos=data)



#ruta de error 404
@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html'), 404

# funciones
def create_table_registro():
    cur = con_db.cursor()
    cur.execute("""
 			CREATE TABLE IF NOT EXISTS registros(
 				id serial  NOT NULL,
 				nombre VARCHAR(50),
 				correo VARCHAR(30),
 				contraseña VARCHAR(20),
				CONSTRAINT pk_atractivos_id PRIMARY KEY (id));
 		""")
con_db.commit()



if __name__ == '__main__':
	app.run(debug=True, port=8080)