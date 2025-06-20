import os 

#Função para limpar o terminal.
def clear_terminal():
    os.system ('cls' if os.name == 'nt' else 'clear')

#Função que cria a pasta de acordo com o que o usuario baixou.
def create_folder_for_save_video():
    if not os.path.exists("videoaudio", "audio", "video"):
        os.makedirs("videoaudio","audio", "video" )
