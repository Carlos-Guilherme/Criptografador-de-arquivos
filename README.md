# Criptografador-de-arquivos
Este programa é uma aplicação de criptografia de arquivos. Ele utiliza o módulo cryptography e o PySimpleGUI para criptografar e descriptografar arquivos. A interface do usuário é feita através do PySimpleGUI, que fornece uma janela para selecionar a opção de criptografia ou descriptografia e outra para selecionar o arquivo a ser criptografado ou descriptografado.

A criptografia é feita através do algoritmo Fernet, que é um tipo de cifra simétrica. Isso significa que a mesma chave é usada para criptografar e descriptografar o arquivo. A chave é gerada a partir da senha inserida pelo usuário, usando o algoritmo PBKDF2HMAC.

A função criptografar lê os dados do arquivo selecionado, criptografa os dados usando a chave gerada e escreve os dados criptografados de volta ao arquivo. A função descriptografar faz o processo oposto, lê os dados criptografados do arquivo, descriptografa os dados usando a chave e escreve os dados descriptografados de volta ao arquivo.

O programa é executado em loop, permitindo que o usuário escolha repetidamente a opção de criptografia ou descriptografia até fechar a janela. O programa é finalizado ao clicar no botão "Cancel".

Este programa pode ser utilizado para proteger informações confidenciais, como arquivos, dados financeiros, informações pessoais, entre outros. Ele permite que o usuário criptografe um arquivo usando uma senha forte, e também possibilita a descriptografia deste arquivo, caso seja necessário. Desta forma, é possível proteger a privacidade dos dados e garantir a segurança das informações armazenadas. Além disso, o uso de uma biblioteca de criptografia segura, como a cryptography, torna o processo mais seguro.
