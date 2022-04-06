function ecrire_ligne () {
    IM01.appendFile(nom_fichier, "" + SN01.getSat() + ",")
    IM01.appendFile(nom_fichier, "" + SN01.getDate() + ",")
    IM01.appendFile(nom_fichier, "" + SN01.getTime() + ",")
    IM01.appendFile(nom_fichier, "" + SN01.getSpeed(SN01.speed_format.KPH) + ",")
    IM01.appendFile(nom_fichier, "" + SN01.getALT() + ",")
    IM01.appendFile(nom_fichier, "" + SN01.getHDOP() + ",")
    IM01.appendFile(nom_fichier, "" + SN01.getLon(SN01.format.DD) + ",")
    IM01.appendFileLine(nom_fichier, SN01.getLat(SN01.format.DD))
}
input.onButtonPressed(Button.A, function () {
    enregistrer = 1
    IM01.overwriteFile(nom_fichier, "")
    IM01.appendFileLine(nom_fichier, "satellites,date,heure,vitesse,altitude,hdop,longitude,latitude")
    IM01.blink_blue_green_led(20, 20, 500)
    while (enregistrer == 1) {
        ecrire_ligne()
        basic.showString(SN01.getSat())
        basic.pause(1000)
        basic.clearScreen()
        basic.pause(4000)
    }
    IM01.turn_off_blink()
    nb_fichiers += 1
    nom_fichier = "GLC_" + convertToText(nb_fichiers) + ".CSV"
    basic.showString(convertToText(nb_fichiers))
})
input.onButtonPressed(Button.B, function () {
    enregistrer = 0
})
let enregistrer = 0
let nom_fichier = ""
let nb_fichiers = 0
nb_fichiers = 0
nom_fichier = "GLC_" + convertToText(nb_fichiers) + ".CSV"
while (IM01.fileExists(nom_fichier)) {
    nb_fichiers += 1
    nom_fichier = "GLC_" + convertToText(nb_fichiers) + ".CSV"
}
basic.showString(convertToText(nb_fichiers))
