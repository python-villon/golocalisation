def ecrire_ligne():
    IM01.append_file(nom_fichier, "" + SN01.get_sat() + ",")
    IM01.append_file(nom_fichier, "" + SN01.get_date() + ",")
    IM01.append_file(nom_fichier, "" + SN01.get_time() + ",")
    IM01.append_file(nom_fichier,
        "" + SN01.get_speed(SN01.speed_format.KPH) + ",")
    IM01.append_file(nom_fichier, "" + SN01.get_alt() + ",")
    IM01.append_file(nom_fichier, "" + SN01.get_hdop() + ",")
    IM01.append_file(nom_fichier, "" + SN01.get_lon(SN01.format.DD) + ",")
    IM01.append_file_line(nom_fichier, SN01.get_lat(SN01.format.DD))

def on_button_pressed_a():
    global enregistrer, nb_fichiers, nom_fichier
    enregistrer = 1
    IM01.overwrite_file(nom_fichier, "")
    IM01.append_file_line(nom_fichier,
        "satellites,date,heure,vitesse,altitude,hdop,longitude,latitude")
    IM01.blink_blue_green_led(20, 20, 500)
    while enregistrer == 1:
        ecrire_ligne()
        basic.show_string(SN01.get_sat())
        basic.pause(1000)
        basic.clear_screen()
        basic.pause(4000)
    IM01.turn_off_blink()
    nb_fichiers += 1
    nom_fichier = "GLC_" + convert_to_text(nb_fichiers) + ".CSV"
    basic.show_string(convert_to_text(nb_fichiers))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global enregistrer
    enregistrer = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

enregistrer = 0
nom_fichier = ""
nb_fichiers = 0
nb_fichiers = 0
nom_fichier = "GLC_" + convert_to_text(nb_fichiers) + ".CSV"
while IM01.file_exists(nom_fichier):
    nb_fichiers += 1
    nom_fichier = "GLC_" + convert_to_text(nb_fichiers) + ".CSV"
basic.show_string(convert_to_text(nb_fichiers))