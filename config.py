def user_setup():
    username = raw_input('Gebruikersnaam:')
    teachername = raw_input('Naam BPV-docent:')
    bossname = raw_input('Naam praktijkbegeleider:')
    company = raw_input('BPV-bedrijf:')
    write_user_file(username, teachername, bossname, company)
    write_logs_file(username, teachername, bossname, company)


def write_user_file(username, teachername, bossname, company):
    f = open('uren.txt', 'a')
    f.write('+------------------------------------------------+' + '\n')
    f.write('| Gegevens: ' + '\n')
    f.write('|   Naam student: ' + username + '\n')
    f.write('|   Naamk BPV-docent: ' + teachername + '\n')
    f.write('|   Naam praktijkopleider: ' + bossname + '\n')
    f.write('|   BPV-bedrijf :' + company + '\n')
    f.write('+------------------------------------------------+' + '\n')
    f.close()


def write_logs_file(username, teachername, bossname, company):
    f = open('logs.txt', 'a')
    f.write('+------------------------------------------------+' + '\n')
    f.write('| Gegevens: ' + '\n')
    f.write('|   Naam student: ' + username + '\n')
    f.write('|   Naamk BPV-docent: ' + teachername + '\n')
    f.write('|   Naam praktijkopleider: ' + bossname + '\n')
    f.write('|   BPV-bedrijf :' + company + '\n')
    f.write('+------------------------------------------------+' + '\n')
    f.close()

user_setup()
