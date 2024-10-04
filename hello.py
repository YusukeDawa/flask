from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return f'''
    <h1><b>Avaliação contínua: Aula 030</b></h1>
    <ul>
        <li><a href="{url_for('home')}">Home</a></li>
        <li><a href="{url_for('identi', nome='Ana Moraes', pront='3026078', insti='IFSP')}">Identificação</a></li>
        <li><a href="{url_for('contexto')}">Contexto da requisição</a></li>
    </ul>
    '''

@app.route('/user/<nome>/<pront>/<insti>')
def identi(nome, pront, insti):
    return f'''
    <h1><b>Avaliação contínua: Aula 030</b></h1>
    <h2><b>Aluno: {nome}</b></h2>
    <h2><b>Prontuário: PT{pront}</b></h2>
    <h2><b>Instituição: {insti}</b></h2>
    <a href="{url_for('home')}">Voltar</a>
    '''

@app.route('/contextorequisicao')
def contexto():
    # Captura as informações desejadas
    navegador = request.user_agent.string  # Navegador do usuário
    ip = request.remote_addr  # IP do usuário
    host = request.host  # Nome do host

    return f"""
    <h1><b>Avaliação contínua: Aula 030</b></h1>
    <h2><b>Seu navegador é: {navegador}</b></h2>
    <h2><b>O IP do computador remoto é: {ip}</b></h2>
    <h2><b>O host da aplicação é: {host}</b></h2>
    <a href="{url_for('home')}">Voltar</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
