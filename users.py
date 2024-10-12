from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necesario para gestionar la sesión

# Base de datos simulada de usuarios
usuarios = {
    "usuario1": {"password": "1234", "degree": "Ingeniería"},
    "usuario2": {"password": "abcd", "degree": "Matemáticas"},
    "usuario3": {"password": "5678", "degree": "Derecho"}
}

@app.route('/')
def home():
    if 'username' in session:
        return f"Bienvenido {session['username']}! Tu grado es {session['degree']}."
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        degree = request.form['degree']

        # Verificación de credenciales
        if username in usuarios and usuarios[username]['password'] == password and usuarios[username]['degree'] == degree:
            session['username'] = username
            session['degree'] = degree
            return redirect(url_for('home'))
        else:
            return "Nombre de usuario, contraseña o grado incorrecto. Inténtalo de nuevo."

    return '''
        <form method="post">
            Nombre: <input type="text" name="username"><br>
            Contraseña: <input type="password" name="password"><br>
            Grado: <input type="text" name="degree"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('degree', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
