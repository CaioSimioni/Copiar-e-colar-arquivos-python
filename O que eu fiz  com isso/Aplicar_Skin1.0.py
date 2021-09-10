# by: zMango
import PySimpleGUI as sg
import os
import shutil
"""
    POR FAVOR, ACESSE OS LINKS E AJUDE NA DIVULGAÇÃO DESSES VÍDEOS, SÓ POR ELES QUE ESSE PROGRAMA SERIA POSSÍVEL ! <3
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
Como mover, copiar e apagar arquivos com Python - Aula 32 = https://www.youtube.com/watch?v=m8orGLxO03s
PySimpleGUI - Múltiplas Janelas SEM Complicação! = https://www.youtube.com/watch?v=K3ykFW-gxWw&t=40s
NOVO CS 1.6 ORIGINAL 2020 (Clássico v6.0) - Como Baixar e Instalar = https://www.youtube.com/watch?v=N64Ay8aYnsY&t=3s
Skins CS 1.6 = https://youtube.com/playlist?list=PLoA1ZBGEzMwF2G3Ih5oDVOj3BHhULcCfi
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=

    -=-=-=-=-= READ ME =-=-= READ ME -=-=-= READ ME =-=-= READ ME =-=-=-=-=-=-

      É necessário que o arquivo seja compilado em um .exe para que funcione, e para que
    possa ser executado com administrador, visto que o CS fica intalado entro dos arquivos windows.

    ** PRIMEIRAMENTE, substituia os caminhos das  pastas das skins. Se não o programa não funcionara.
    ** SEGUNDAMENTE, caso não tenha alguma das skins, Baixe elas ou não tente aplica-las no programa.
    ** TERCEIRAMENTE, é necessário compilar o arquivo.  Desculpe, mas sou um programador iniciante
      e ainda não tenhototal domínio do Python para criar programas muitos complexos.

    * Para compilar o programa, Abra o Terminal do Python, e coloque:
     cxfreeze <nome do arquivo> --target-dir <Pasta que será criada>

    * Se utilizar o VisualStudioCode:
    Com o arquivo aperto.
    (Ctrl + ") e digitar: ( cxfreeze <nome do arquivo> --target-dir <Pasta que será criada> )

    * No meu caso o nome do arquivo é (Aplicar_Skin.py) e a pasta é (AppSkin)

    * Depois espereo programa ser compilado, após isso é só Executalo como administrador.
"""

# Caminhos paras as Skins
CS_Skins_Path = r'C:\Program Files (x86)\MONSTERSKILL\CS Classic 2020\cstrike\models'
CS_Sounds_Path = r'C:\Program Files (x86)\MONSTERSKILL\CS Classic 2020\cstrike\sound\weapons'
CS_Skin_Knife_Path = r'C:\Program Files (x86)\MONSTERSKILL\CS Classic 2020\cstrike\models\v_knife.mdl'
Amphibious_Skin_path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Skin Pack\models'
SportGloveOmega_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Skin Pack\models'
CrimsonWeb_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Skin Pack\models'
Default_Skin_path = r'C:\Users\Caior\Desktop\SkinCS\SkinsOriginais\models'

# Métodos das Skins
skinAplicada = False  # Saber se a skin foi equipada com sucesso
nomeFaca=''

# ==================================================================================================================
def Amphibious(faca, m4a4):
    for root, dirs, files in os.walk(Amphibious_Skin_path):
        for file in files:
            skin_pack_path = os.path.join(root, file)
            skin_cs_path = os.path.join(CS_Skins_Path, file)
            if 'v_' in file:
                os.remove(skin_cs_path)
                shutil.copy(skin_pack_path, skin_cs_path)
    
    if faca == 1:
        Amphibious_Bayonet_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Knifes\Bayonet\models'
        for root, dirs, files in os.walk(Amphibious_Bayonet_Skin_Path):
            for file  in files:
                skin_knife_skin = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_skin, skin_cs_path)
        nomeFaca = 'Bayonet'

    elif faca == 2:
        Amphibious_Bowie_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Knifes\Bowie\models'
        for root, dirs, files in os.walk(Amphibious_Bowie_Skin_Path):
            for file  in files:
                skin_knife_skin = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_skin, skin_cs_path)
        nomeFaca = 'Bowie'

    elif faca == 3:
        Amphibious_ButterFly_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Knifes\ButterFly\models'
        for root, dirs, files in os.walk(Amphibious_ButterFly_Skin_Path):
            for file  in files:
                skin_knife_skin = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_skin, skin_cs_path)
        nomeFaca = 'ButterFly'

    elif faca == 4:
        Amphibious_Flip_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Knifes\Flip\models'
        for root, dirs, files in os.walk(Amphibious_Flip_Skin_Path):
            for file  in files:
                skin_knife_skin = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_skin, skin_cs_path)
        nomeFaca = 'Flip'
    
    elif faca == 5:
        Amphibious_Huntsman_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Knifes\Huntsman\models'
        for root, dirs, files in os.walk(Amphibious_Huntsman_Skin_Path):
            for file  in files:
                skin_knife_skin = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_skin, skin_cs_path)
        nomeFaca = 'Huntsman'

    elif faca == 6:
        Amphibious_Karambit_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Knifes\Karambit\models'
        for root, dirs, files in os.walk(Amphibious_Karambit_Skin_Path):
            for file  in files:
                skin_knife_skin = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_skin, skin_cs_path)
        nomeFaca = 'Karambit'

    elif faca == 7:
        Amphibious_M9Bayonet_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Knifes\M9 Bayonet\models'
        for root, dirs, files in os.walk(Amphibious_M9Bayonet_Skin_Path):
            for file  in files:
                skin_knife_skin = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_skin, skin_cs_path)
        nomeFaca = 'M9 Bayonet'

    elif faca == 8:
        Amphibious_Navaja_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Knifes\Navaja\models'
        for root, dirs, files in os.walk(Amphibious_Navaja_Skin_Path):
            for file  in files:
                skin_knife_skin = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_skin, skin_cs_path)
        nomeFaca = 'Navaja'

    elif faca == 9:
        Amphibious_Stiletto_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Knifes\Stiletto\models'
        for root, dirs, files in os.walk(Amphibious_Stiletto_Skin_Path):
            for file  in files:
                skin_knife_skin = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_skin, skin_cs_path)
        nomeFaca = 'Stilleto'

    elif faca == 10:
        Amphibious_Talon_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Knifes\Talon\models'
        for root, dirs, files in os.walk(Amphibious_Talon_Skin_Path):
            for file  in files:
                skin_knife_skin = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_skin, skin_cs_path)
        nomeFaca = 'Talon'

    elif faca == 11:
        Amphibious_Ursus_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Knifes\Ursus\models'
        for root, dirs, files in os.walk(Amphibious_Ursus_Skin_Path):
            for file  in files:
                skin_knife_skin = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_skin, skin_cs_path)
        nomeFaca = 'Ursus'

    if m4a4:
        Amphibious_M4A4_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\M4A4\models'
        for root, dirs, files in os.walk(Amphibious_M4A4_Skin_Path):
            for file in files:
                skin_m4a4_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_m4a1.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_m4a4_path, skin_cs_path)
        Amphibious_M4A4_Sounds_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\M4A4\sound\weapons'
        for root, dirs, files in os.walk(Amphibious_M4A4_Sounds_Path):
            for file in files:
                sound_m4a4_path = os.path.join(root, file)
                sound_default_path = os.path.join(CS_Sounds_Path, file)
                if 'm4a1' in file:
                    os.remove(sound_default_path)
                    shutil.copy(sound_m4a4_path, sound_default_path)
    else: # m4a1
        Amphibious_M4A1_Sounds_Path = r'C:\Users\Caior\Desktop\SkinCS\Amphibious Pack By Ardiyonaツ\Skin Pack\sound\weapons'
        for root, dirs, files in os.walk(Amphibious_M4A1_Sounds_Path):
            for file in files:
                sound_m4a1_path =  os.path.join(root, file)
                sound_default_path = os.path.join(CS_Sounds_Path, file)
                if 'm4a1' in file:
                    os.remove(sound_default_path)
                    shutil.copy(sound_m4a1_path, sound_default_path)
    skinAplicada = True

def OmegaSkin(faca, AwpPhobos, Cz75, m4a4, Mag7, Negev, P2000, SawedOff, Tec9):
    for root, dirs, files in os.walk(SportGloveOmega_Skin_Path):
        for file in files:
            skin_pack_path = os.path.join(root, file)
            skin_cs_path = os.path.join(CS_Skins_Path, file)
            if 'v_' in file:
                os.remove(skin_cs_path)
                shutil.copy(skin_pack_path, skin_cs_path)
    
    if faca == 1:
        Omega_Bayonet_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Bayonet\models'
        for root, dirs, files in os.walk(Omega_Bayonet_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Bayonet'

    elif faca == 2:
        Omega_Bowie_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Bowie\models'
        for root, dirs, files in os.walk(Omega_Bowie_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Bowie'
    
    elif faca == 3:
        Omega_ButterFly_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\ButterFly\models'
        for root, dirs, files in os.walk(Omega_ButterFly_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'ButterFly'

    elif faca == 4:
        Omega_Classic_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Classic\models'
        for root, dirs, files in os.walk(Omega_Classic_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'ButterFly'

    elif faca == 5:
        Omega_Falchion_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Falchion\models'
        for root, dirs, files in os.walk(Omega_Falchion_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Falchion'

    elif faca == 6:
        Omega_Flip_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Flip\models'
        for root, dirs, files in os.walk(Omega_Flip_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Flip'

    elif faca == 7:
        Omega_Gut_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Gut\models'
        for root, dirs, files in os.walk(Omega_Gut_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Gut'

    elif faca == 8:
        Omega_Huntsman_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Huntsman\models'
        for root, dirs, files in os.walk(Omega_Huntsman_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Huntsman'

    elif faca == 9:
        Omega_Karambit_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Karambit\models'
        for root, dirs, files in os.walk(Omega_Karambit_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Karambit'

    elif faca == 10:
        Omega_M9_Bayonet_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\M9 Bayonet\models'
        for root, dirs, files in os.walk(Omega_M9_Bayonet_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'M9 Bayonet'

    elif faca == 11:
        Omega_Navaja_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Navaja\models'
        for root, dirs, files in os.walk(Omega_Navaja_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Navaja'

    elif faca == 12:
        Omega_Nomad_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Nomad\models'
        for root, dirs, files in os.walk(Omega_Nomad_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Nomad'

    elif faca == 13:
        Omega_Paracord_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Paracord\models'
        for root, dirs, files in os.walk(Omega_Paracord_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Paracord'

    elif faca == 14:
        Omega_Shadow_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Shadow\models'
        for root, dirs, files in os.walk(Omega_Shadow_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Shadow'

    elif faca == 15:
        Omega_Skeleton_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Skeleton\models'
        for root, dirs, files in os.walk(Omega_Skeleton_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Skeleton'

    elif faca == 16:
        Omega_Stiletto_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Stiletto\models'
        for root, dirs, files in os.walk(Omega_Stiletto_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Stiletto'

    elif faca == 17:
        Omega_Survival_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Survival\models'
        for root, dirs, files in os.walk(Omega_Survival_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Survival'

    elif faca == 18:
        Omega_Talon_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Talon\models'
        for root, dirs, files in os.walk(Omega_Talon_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Talon'

    elif faca == 19:
        Omega_Ursus_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Knives\Ursus\models'
        for root, dirs, files in os.walk(Omega_Ursus_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Ursus'

    if AwpPhobos:
        Omega_PhobosAwp_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Extra skins\AWP Phobos\models'
        for root, dirs, files in os.walk(Omega_PhobosAwp_Skin_Path):
            for file in files:
                skin_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_awp.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_path, skin_cs_path)

    if Cz75:
        Omega_Cz75_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Extra skins\Cz-75\models'
        for root, dirs, files in os.walk(Omega_Cz75_Skin_Path):
            for file in files:
                skin_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_tmp.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_path, skin_cs_path)

    if m4a4:
        Omega_M4A4_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Extra skins\M4a4\models'
        for root, dirs, files in os.walk(Omega_M4A4_Skin_Path):
            for file in files:
                skin_m4a4_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_m4a1.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_m4a4_path, skin_cs_path)
        Omega_M4A4_Sounds_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Extra skins\M4a4\sound\weapons'
        for root, dirs, files in os.walk(Omega_M4A4_Sounds_Path):
            for file in files:
                sound_m4a4_path = os.path.join(root, file)
                sound_default_path = os.path.join(CS_Sounds_Path, file)
                if 'm4a1' in file:
                    os.remove(sound_default_path)
                    shutil.copy(sound_m4a4_path, sound_default_path)
    else: # m4a1
        Omega_M4A1_Sounds_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Skin Pack\sound\weapons'
        for root, dirs, files in os.walk(Omega_M4A1_Sounds_Path):
            for file in files:
                sound_m4a1_path =  os.path.join(root, file)
                sound_default_path = os.path.join(CS_Sounds_Path, file)
                if 'm4a1' in file:
                    os.remove(sound_default_path)
                    shutil.copy(sound_m4a1_path, sound_default_path)

    if Mag7:
        Omega_Mag7_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Extra skins\Mag-7\models'
        for root, dirs, files in os.walk(Omega_Mag7_Skin_Path):
            for file in files:
                skin_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_xm1014.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_path, skin_cs_path)

    if Negev:
        Omega_Negev_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Extra skins\Negev\models'
        for root, dirs, files in os.walk(Omega_Negev_Skin_Path):
            for file in files:
                skin_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_m249.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_path, skin_cs_path)

    if P2000:
        Omega_P2000_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Extra skins\P200\models'
        for root, dirs, files in os.walk(Omega_P2000_Skin_Path):
            for file in files:
                skin_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_usp.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_path, skin_cs_path)
    
    if SawedOff:
        Omega_Sawed_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Extra skins\Sawed-off\models'
        for root, dirs, files in os.walk(Omega_Sawed_Skin_Path):
            for file in files:
                skin_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_m3.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_path, skin_cs_path)

    if Tec9:
        Omega_Tec9_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\CS GO Sport Glove Omega Skin Pack\Extra skins\Tec-9\models'
        for root, dirs, files in os.walk(Omega_Tec9_Skin_Path):
            for file in files:
                skin_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_p228.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_path, skin_cs_path)
    
    skinAplicada=True

def CrimsonWeb(faca, ak47, awp, deagle, m4a4, p2000):
    for root, dirs, files in os.walk(CrimsonWeb_Skin_Path):
        for file in files:
            skin_pack_path = os.path.join(root, file)
            skin_cs_path = os.path.join(CS_Skins_Path, file)
            if 'v_' in file:
                os.remove(skin_cs_path)
                shutil.copy(skin_pack_path, skin_cs_path)
    
    if faca == 1:
        Crimson_Bayonet_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Bayonet\models'
        for root, dirs, files in os.walk(Crimson_Bayonet_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Bayonet'

    elif faca == 2:
        Crimson_Bowie_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Bowie\models'
        for root, dirs, files in os.walk(Crimson_Bowie_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Bowie'
    
    elif faca == 3:
        Crimson_ButterFly_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\ButterFly\models'
        for root, dirs, files in os.walk(Crimson_ButterFly_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'ButterFly'

    elif faca == 4:
        Crimson_Classic_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Classic\models'
        for root, dirs, files in os.walk(Crimson_Classic_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'ButterFly'

    elif faca == 5:
        Crimson_Falchion_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Falchion\models'
        for root, dirs, files in os.walk(Crimson_Falchion_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Falchion'

    elif faca == 6:
        Crimson_Flip_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Flip\models'
        for root, dirs, files in os.walk(Crimson_Flip_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Flip'

    elif faca == 7:
        Crimson_Gut_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Gut\models'
        for root, dirs, files in os.walk(Crimson_Gut_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Gut'

    elif faca == 8:
        Crimson_Huntsman_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Huntsman\models'
        for root, dirs, files in os.walk(Crimson_Huntsman_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Huntsman'

    elif faca == 9:
        Crimson_Karambit_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Karambit\models'
        for root, dirs, files in os.walk(Crimson_Karambit_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Karambit'

    elif faca == 10:
        Crimson_M9_Bayonet_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\M9 Bayonet\models'
        for root, dirs, files in os.walk(Crimson_M9_Bayonet_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'M9 Bayonet'

    elif faca == 11:
        Crimson_Navaja_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Navaja\models'
        for root, dirs, files in os.walk(Crimson_Navaja_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Navaja'

    elif faca == 12:
        Crimson_Nomad_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Nomad\models'
        for root, dirs, files in os.walk(Crimson_Nomad_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Nomad'

    elif faca == 13:
        Crimson_Paracord_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Paracord\models'
        for root, dirs, files in os.walk(Crimson_Paracord_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Paracord'

    elif faca == 14:
        Crimson_Shadow_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\ShadowDaggers\models'
        for root, dirs, files in os.walk(Crimson_Shadow_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Shadow'

    elif faca == 15:
        Crimson_Skeleton_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Skeleton\models'
        for root, dirs, files in os.walk(Crimson_Skeleton_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Skeleton'

    elif faca == 16:
        Crimson_Stiletto_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Stiletto\models'
        for root, dirs, files in os.walk(Crimson_Stiletto_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Stiletto'

    elif faca == 17:
        Crimson_Survival_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Survival\models'
        for root, dirs, files in os.walk(Crimson_Survival_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Survival'

    elif faca == 18:
        Crimson_Talon_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Talon\models'
        for root, dirs, files in os.walk(Crimson_Talon_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Talon'

    elif faca == 19:
        Crimson_Ursus_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Knives\Ursus\models'
        for root, dirs, files in os.walk(Crimson_Ursus_Skin_Path):
            for file in files:
                skin_knife_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_knife.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_knife_path, skin_cs_path)
        nomeFaca = 'Ursus'

    if ak47:
        Ak47RedLine_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\AK47 - Redline\models'
        for root, dirs, files in os.walk(Ak47RedLine_Skin_Path):
            for file in files:
                skin_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if '.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_path, skin_cs_path)
                    print('Ak47 RedLine -equipada-')

    if awp:
        AwpGungir_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\AWP - Gungnir\models'
        for root, dirs, files in os.walk(AwpGungir_Skin_Path):
            for file in files:
                skin_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if '.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_path, skin_cs_path)
                    print('Awp Gungir -equipada-')
    
    if deagle:
        DeagleCodeRed_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\Deagle - CodeRed'
        for root, dirs, files in os.walk(DeagleCodeRed_Skin_Path):
            for file in files:
                skin_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if '.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_path, skin_cs_path)
                    print('Deagle Code Red -equipada-')

    if p2000:
        P2000Obisidien_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\P2000 - Obsidien'
        for root, dirs, files in os.walk(P2000Obisidien_Skin_Path):
            for file in files:
                skin_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if '.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_path, skin_cs_path)
                    print('Deagle Code Red -equipada-')

    if m4a4:
        Crimson_M4A4_Skin_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\M4a4 - Howl\models'
        for root, dirs, files in os.walk(Crimson_M4A4_Skin_Path):
            for file in files:
                skin_m4a4_path = os.path.join(root, file)
                skin_cs_path = os.path.join(CS_Skins_Path, file)
                if 'v_m4a1.mdl' in file:
                    os.remove(skin_cs_path)
                    shutil.copy(skin_m4a4_path, skin_cs_path)
        Crimson_M4A4_Sounds_Path = r'C:\Users\Caior\Desktop\SkinCS\Specialist Crimson Web Gloves Skin Pack ByArdiyona\Extra\M4a4 - Howl\sound\weapons'
        for root, dirs, files in os.walk(Crimson_M4A4_Sounds_Path):
            for file in files:
                sound_m4a4_path = os.path.join(root, file)
                sound_default_path = os.path.join(CS_Sounds_Path, file)
                if 'm4a1' in file:
                    os.remove(sound_default_path)
                    shutil.copy(sound_m4a4_path, sound_default_path)

def defaultSkin():
    for root, dirs, files in os.walk(Default_Skin_path):
        for file in files:
            skin_pack_path = os.path.join(root, file)
            skin_cs_path = os.path.join(CS_Skins_Path, file)
            if 'v_' in file:
                os.remove(skin_cs_path)
                shutil.copy(skin_pack_path, skin_cs_path)
    skinAplicada = True

# ==================================================================================================================

# Criar Janeleas e Estilos(Layouts)
def janela_skin():
    sg.theme('Black')
    layout = [
        [sg.Text('-=-= Skins Counter Strike 1.6 =-=-')],
        [sg.Radio(' Amphibous', 'g01', key='Key_Amphibuos', size=(20, 20), text_color='sky blue')],
        [sg.Radio(' Omega', 'g01', key='Key_Omega', size=(20, 20), text_color='yellow')],
        [sg.Radio(' Crimson Web', 'g01', key='Key_Crimson', size=(20, 20), text_color='red')],
        [sg.Radio(' Default Skin', "g01", key='Key_DefaultSkin', size=(20, 20), default=True)],
        [sg.Button('Escolher Skin', key='Skin_Escolha'), sg.Button('Sair', key='Skin_Sair')]
    ]
    return sg.Window('Skin 1.6', layout=layout, finalize=True)

def janela_Amphibious():
    sg.theme('Black')
    layout = [
        [sg.Text('-=-= Amphibuos =-=-', text_color='sky blue')],
        [sg.Text('- Facas -', text_color='sky blue')],
        [sg.Radio('Bayonet', 'gfAmph', key='Key_Amph_Bayonet', size=(10, 30), default=True), sg.Radio('Karambit', 'gfAmph', key='Key_Amph_Karambit', size=(10, 30))],
        [sg.Radio('Bowie', 'gfAmph', key='Key_Amph_Bowie', size=(10, 30)), sg.Radio('M9 Bayonet', 'gfAmph', key='Key_Amph_M9', size=(10, 30))],
        [sg.Radio('ButterFly', 'gfAmph', key='Key_Amph_ButterFly', size=(10, 30)), sg.Radio('Navaja', 'gfAmph', key='Key_Amph_Navaja', size=(10, 30))],
        [sg.Radio('Flip', 'gfAmph', key='Key_Amph_Flip', size=(10, 30)), sg.Radio('Stiletto', 'gfAmph', key='Key_Amph_Stiletto', size=(10, 30))],
        [sg.Radio('Huntsman', 'gfAmph', key='Key_Amph_Huntsman', size=(10, 30)), sg.Radio('Talon', 'gfAmph', key='Key_Amph_Talon', size=(10, 30))],
        [sg.Radio('Ursus', 'gfAmph', key='Key_Amph_Ursus', size=(10, 30))],
        [sg.Text('- Opcional -', text_color='sky blue')],
        [sg.Checkbox('M4A4', key='Key_Amph_M4A4')],
        [sg.Button('Apicar Skin', key='Key_Aplicar_Amph'), sg.Button('Voltar', key='Key_Voltar_Skin')]
    ]
    return sg.Window('Skin 1.6', layout=layout, finalize=True)

def janela_Omega():
    sg.theme('Black')
    layout = [
        [sg.Text('-=-= Omega =-=-', text_color='yellow')],
        [sg.Text('- Facas -', text_color='yellow')],
        [sg.Radio('Bayonet', 'gfOmega', key='Key_Omega_Bayonet', size=(10, 30), default=True), sg.Radio('Navaja', 'gfOmega', key='Key_Omega_Navaja', size=(10, 30))],
        [sg.Radio('Bowie', 'gfOmega', key='Key_Omega_Bowie', size=(10, 30)), sg.Radio('Nomad', 'gfOmega', key='Key_Omega_Nomad', size=(10, 30))],
        [sg.Radio('ButterFly', 'gfOmega', key='Key_Omega_ButterFly', size=(10, 30)), sg.Radio('Paracord', 'gfOmega', key='Key_Omega_Paracord', size=(10, 30))],
        [sg.Radio('Classic', 'gfOmega', key='Key_Omega_Classic', size=(10, 30)), sg.Radio('Shadow', 'gfOmega', key='Key_Omega_Shadow', size=(10, 30))],
        [sg.Radio('Falchion', 'gfOmega', key='Key_Omega_Falchion', size=(10, 30)), sg.Radio('Skeleton', 'gfOmega', key='Key_Omega_Skeleton', size=(10, 30))],
        [sg.Radio('Flip', 'gfOmega', key='Key_Omega_Flip', size=(10, 30)), sg.Radio('Stiletto', 'gfOmega', key='Key_Omega_Stiletto', size=(10, 30))],
        [sg.Radio('Gut', 'gfOmega', key='Key_Omega_Gut', size=(10, 30)), sg.Radio('Survival', 'gfOmega', key='Key_Omega_Survival', size=(10, 30))],
        [sg.Radio('Huntsman', 'gfOmega', key='Key_Omega_Huntsman', size=(10, 30)), sg.Radio('Talon', 'gfOmega', key='Key_Omega_Talon', size=(10, 30))],
        [sg.Radio('Karambit', 'gfOmega', key='Key_Omega_Karambit', size=(10, 30)), sg.Radio('Ursus', 'gfOmega', key='Key_Omega_Ursus', size=(10, 30))],
        [sg.Radio('M9 Bayonet', 'gfOmega', key='Key_Omega_M9', size=(10, 30))],
        [sg.Text('- Opcional -', text_color='yellow')],
        [sg.Checkbox('Awp Phobos', key='Key_Omega_awpphobos', size=(10, 30)), sg.Checkbox('Negev', key='Key_Omega_negev', size=(10, 30))],
        [sg.Checkbox('Cz-75', key='Key_Omega_cz75', size=(10, 30)), sg.Checkbox('P2000', key='Key_Omega_p2000', size=(10, 30))],
        [sg.Checkbox('M4A4', key='Key_Omega_m4a4', size=(10, 30)), sg.Checkbox('Sawed-off', key='Key_Omega_sawedoff', size=(10, 30))],
        [sg.Checkbox('Mag-7', key='Key_Omega_mag7', size=(10, 30)), sg.Checkbox('Tec-9', key='Key_Omega_tec9', size=(10, 30))],
        [sg.Button('Apicar Skin', key='Key_Aplicar_Omega'), sg.Button('Voltar', key='Key_Voltar_Skin')]
    ]
    return sg.Window('Skin 1.6', layout=layout, finalize=True)

def janela_Crimson():
    sg.theme('Black')
    layout = [
        [sg.Text('-=-= Crimson Web =-=-', text_color='red')],
        [sg.Text('- Facas -', text_color='red')],
        [sg.Radio('Bayonet', 'gfCrimson', key='Key_Crimson_Bayonet', size=(15, 30), default=True), sg.Radio('Navaja', 'gfCrimson', key='Key_Crimson_Navaja', size=(10, 30))],
        [sg.Radio('Bowie', 'gfCrimson', key='Key_Crimson_Bowie', size=(15, 30)), sg.Radio('Nomad', 'gfCrimson', key='Key_Crimson_Nomad', size=(10, 30))],
        [sg.Radio('ButterFly', 'gfCrimson', key='Key_Crimson_ButterFly', size=(15, 30)), sg.Radio('Paracord', 'gfCrimson', key='Key_Crimson_Paracord', size=(10, 30))],
        [sg.Radio('Classic', 'gfCrimson', key='Key_Crimson_Classic', size=(15, 30)), sg.Radio('Shadow', 'gfCrimson', key='Key_Crimson_Shadow', size=(10, 30))],
        [sg.Radio('Falchion', 'gfCrimson', key='Key_Crimson_Falchion', size=(15, 30)), sg.Radio('Skeleton', 'gfCrimson', key='Key_Crimson_Skeleton', size=(10, 30))],
        [sg.Radio('Flip', 'gfCrimson', key='Key_Crimson_Flip', size=(15, 30)), sg.Radio('Stiletto', 'gfCrimson', key='Key_Crimson_Stiletto', size=(10, 30))],
        [sg.Radio('Gut', 'gfCrimson', key='Key_Crimson_Gut', size=(15, 30)), sg.Radio('Survival', 'gfCrimson', key='Key_Crimson_Survival', size=(10, 30))],
        [sg.Radio('Huntsman', 'gfCrimson', key='Key_Crimson_Huntsman', size=(15, 30)), sg.Radio('Talon', 'gfCrimson', key='Key_Crimson_Talon', size=(10, 30))],
        [sg.Radio('Karambit', 'gfCrimson', key='Key_Crimson_Karambit', size=(15, 30)), sg.Radio('Ursus', 'gfCrimson', key='Key_Crimson_Ursus', size=(10, 30))],
        [sg.Radio('M9 Bayonet', 'gfCrimson', key='Key_Crimson_M9', size=(15, 30))],
        [sg.Text('- Opcional -', text_color='red')],
        [sg.Checkbox('Ak-47 RedLine', key='Key_Crimson_ak47redline', size=(15, 35)), sg.Checkbox('AWP Gungnir', key='Key_Crimson_awpgungnir', size=(15, 35))],
        [sg.Checkbox('Deagle CodeRed',  key='Key_Crimson_deaglecodered', size=(15, 35)), sg.Checkbox('P2000 Obisidien', key='Key_Crimson_p2000obisidien', size=(15, 35))],
        [sg.Checkbox('M4A4 Howl', key='Key_Crimson_m4a4howl', size=(10, 35))],
        [sg.Button('Apicar Skin', key='Key_Aplicar_Crimson'), sg.Button('Voltar', key='Key_Voltar_Skin')]
    ]
    return sg.Window('Skin 1.6', layout=layout, finalize=True)

# Criar Janelas Inicias
janela_Skin, janela_Modif_Skin = janela_skin(), None

# Criar um loop de Leitura de eventos
while True:
    window, events, values = sg.read_all_windows()

    # Quando a janela for fechada
    if window == janela_Skin and events == sg.WINDOW_CLOSED:
        break
    if window == janela_Modif_Skin and events == sg.WINDOW_CLOSED:
        break

    # Quando queremos ir para proxima janela
    if window == janela_Skin and events == 'Skin_Escolha':
        if values['Key_Amphibuos']:
            janela_Modif_Skin = janela_Amphibious()
            janela_Skin.hide()
        if values['Key_Omega']:
            janela_Modif_Skin = janela_Omega()
            janela_Skin.hide()
        if values['Key_Crimson']:
            janela_Modif_Skin = janela_Crimson()
            janela_Skin.hide()
        if values['Key_DefaultSkin']:
            defaultSkin()
            sg.popup(' Aplicada com Sucesso! \n Default Skin')
            break
    
    if window == janela_Skin and events == 'Skin_Sair':
        break

    # Quando queremos voltar para a janela anterior
    if window == janela_Modif_Skin and events == 'Key_Voltar_Skin':
        janela_Modif_Skin.close()
        janela_Skin.un_hide()

# Lógica dos Botões
    if window == janela_Modif_Skin and events == 'Key_Aplicar_Amph':
        facaAmph=0
        m4a4Amph=False
        if values['Key_Amph_Bayonet']:
            facaAmph=1
        elif values['Key_Amph_Bowie']:
            facaAmph=2
        elif values['Key_Amph_ButterFly']:
            facaAmph=3
        elif values['Key_Amph_Flip']:
            facaAmph=4
        elif values['Key_Amph_Huntsman']:
            facaAmph=5
        elif values['Key_Amph_Karambit']:
            facaAmph=6
        elif values['Key_Amph_M9']:
            facaAmph=7
        elif values['Key_Amph_Navaja']:
            facaAmph=8
        elif values['Key_Amph_Stiletto']:
            facaAmph=9
        elif values['Key_Amph_Talon']:
            facaAmph=10
        elif values['Key_Amph_Ursus']:
            facaAmph=11
        else:
            pass
        if values['Key_Amph_M4A4']:
            m4a4Amph=True
        Amphibious(facaAmph, m4a4Amph)
        sg.popup(f' Aplicada com Sucesso! \n Amphbiuos - {nomeFaca}', text_color='sky blue')
        break

    if window == janela_Modif_Skin and events == 'Key_Aplicar_Omega':
        facaOmega=0
        awpOmega=False
        cz75=False
        m4a4Omega=False
        mag7Omega=False
        nevegOmega=False
        p2000Omega=False
        sawedoffOmega=False
        tec9Omega=False
        if values['Key_Omega_Bayonet']:
            facaOmega=1
        if values['Key_Omega_Bowie']:
            facaOmega=2
        if values['Key_Omega_ButterFly']:
            facaOmega=3
        if values['Key_Omega_Classic']:
            facaOmega=4
        if values['Key_Omega_Falchion']:
            facaOmega=5
        if values['Key_Omega_Flip']:
            facaOmega=6
        if values['Key_Omega_Gut']:
            facaOmega=7
        if values['Key_Omega_Huntsman']:
            facaOmega=8
        if  values['Key_Omega_Karambit']:
            facaOmega=9
        if values['Key_Omega_M9']:
            facaOmega=10
        if values['Key_Omega_Navaja']:
            facaOmega=11
        if values['Key_Omega_Nomad']:
            facaOmega=12
        if values['Key_Omega_Paracord']:
            facaOmega=13
        if values['Key_Omega_Shadow']:
            facaOmega=14
        if values['Key_Omega_Skeleton']:
            facaOmega=15
        if values['Key_Omega_Stiletto']:
            facaOmega=16
        if values['Key_Omega_Survival']:
            facaOmega=17
        if values['Key_Omega_Talon']:
            facaOmega=18
        if values['Key_Omega_Ursus']:
            facaOmega=19
        if values['Key_Omega_awpphobos']:
            awpOmega=True
        if values['Key_Omega_cz75']:
            cz75=True
        if values['Key_Omega_m4a4']:
            m4a4Omega=True
        if values['Key_Omega_negev']:
            negevOmega=True
        if values['Key_Omega_p2000']:
            p2000Omega=True
        if values['Key_Omega_sawedoff']:
            sawedoffOmega=True
        if values['Key_Omega_tec9']:
            tec9Omega=True
        
        OmegaSkin(facaOmega, awpOmega, cz75, m4a4Omega, mag7Omega, nevegOmega, p2000Omega, sawedoffOmega, tec9Omega)
        sg.popup(f' Aplicada com Sucesso! \n   Omega - {nomeFaca}', text_color='yellow')
        break

    if window == janela_Modif_Skin and events == 'Key_Aplicar_Crimson':
        facaCrimson=0
        ak47redline = False
        awpgungnir = False
        deaglecodered = False
        m4a4howl = False
        p2000obisidien = False
        if values['Key_Crimson_Bayonet']:
            facaCrimson=1
        if values['Key_Crimson_Bowie']:
            facaCrimson=2
        if values['Key_Crimson_ButterFly']:
            facaCrimson=3
        if values['Key_Crimson_Classic']:
            facaCrimson=4
        if values['Key_Crimson_Falchion']:
            facaCrimson=5
        if values['Key_Crimson_Flip']:
            facaCrimson=6
        if values['Key_Crimson_Gut']:
            facaCrimson=7
        if values['Key_Crimson_Huntsman']:
            facaCrimson=8
        if  values['Key_Crimson_Karambit']:
            facaCrimson=9
        if values['Key_Crimson_M9']:
            facaCrimson=10
        if values['Key_Crimson_Navaja']:
            facaCrimson=11
        if values['Key_Crimson_Nomad']:
            facaCrimson=12
        if values['Key_Crimson_Paracord']:
            facaCrimson=13
        if values['Key_Crimson_Shadow']:
            facaCrimson=14
        if values['Key_Crimson_Skeleton']:
            facaCrimson=15
        if values['Key_Crimson_Stiletto']:
            facaCrimson=16
        if values['Key_Crimson_Survival']:
            facaCrimson=17
        if values['Key_Crimson_Talon']:
            facaCrimson=18
        if values['Key_Crimson_Ursus']:
            facaCrimson=19
        if values['Key_Crimson_ak47redline']:
            ak47redline=True
        if values['Key_Crimson_awpgungnir']:
            awpgungnir=True
        if values['Key_Crimson_deaglecodered']:
            deaglecodered=True
        if values['Key_Crimson_m4a4howl']:
            m4a4howl=True
        if values['Key_Crimson_p2000obisidien']:
            p2000obisidien=True
        

        CrimsonWeb(facaCrimson, ak47redline, awpgungnir, deaglecodered, m4a4howl, p2000obisidien)

        sg.popup('Aplicada com sucesso!\n{:^22}'.format('Crimson Web'), text_color='red')
        break
