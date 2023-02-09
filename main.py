import PySimpleGUI as sg
import os
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

sg.theme("Dark Blue")
def criptografar(caminho_arquivo, senha):
    with open(caminho_arquivo, "rb") as arquivo:
        dados = arquivo.read()

    senha = senha.encode()

    salt = b'\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    chave = base64.urlsafe_b64encode(kdf.derive(senha))
    f = Fernet(chave)
    dados_criptografados = f.encrypt(dados)

    with open(caminho_arquivo, "wb") as arquivo:
        arquivo.write(dados_criptografados)

def descriptografar(caminho_arquivo, senha):
    with open(caminho_arquivo, "rb") as arquivo:
        dados_criptografados = arquivo.read()

    senha = senha.encode()

    salt = b'\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    chave = base64.urlsafe_b64encode(kdf.derive(senha))
    f = Fernet(chave)
    dados_descriptografados = f.decrypt(dados_criptografados)

    with open(caminho_arquivo, "wb") as arquivo:
        arquivo.write(dados_descriptografados)

def escolher_arquivo():
    layout = [[sg.Text('Selecione o arquivo:')],
              [sg.Input(), sg.FileBrowse()],
              [sg.OK(), sg.Cancel()]]

    janela = sg.Window('Selecionar arquivo').layout(layout)

    evento, valores = janela.read()
    janela.close()

    if evento == 'OK':
        return valores[0]
    else:
        return None
         
layout = [[sg.Text('Escolha a opção desejada:')],
          [sg.Button('Criptografar'), sg.Button('Descriptografar')],
          [sg.OK(), sg.Cancel()]]

janela = sg.Window('Criptografia de arquivos').layout(layout)

while True:
    evento, valores = janela.read()
    if evento in (None, 'Cancel'):
        break
    elif evento == 'Criptografar':
        caminho_arquivo = escolher_arquivo()
        if caminho_arquivo:
            senha = sg.popup_get_text('Insira a senha para criptografar o arquivo')
            criptografar(caminho_arquivo, senha)
            sg.popup('Arquivo criptografado com sucesso')
    elif evento == 'Descriptografar':
        caminho_arquivo = escolher_arquivo()
        if caminho_arquivo:
            senha = sg.popup_get_text('Insira a senha para descriptografar o arquivo')
            descriptografar(caminho_arquivo, senha)
            sg.popup('Arquivo descriptografado com sucesso')

janela.close()
