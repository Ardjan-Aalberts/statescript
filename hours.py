def write_file(date, hours, u_hours, b_hours, gen_act):
    f = open('uren.txt', 'a')
    f.write('+------------------------------------------------+' + '\n')
    f.write('| Datum: ' + date + '\n')
    f.write('|   Uren: ' + hours + '\n')
    f.write('|   Onbegeleide uren: ' + u_hours + '\n')
    f.write('|   Begeleide uren: ' + b_hours + '\n')
    f.write('|   Activiteiten :' + gen_act + '\n')
    f.write('+------------------------------------------------+' + '\n')
    f.close()


def user_activity():
    date = raw_input('Datum:')
    hours = raw_input('Gemaakte uren:')
    u_hours = raw_input('Onbegeleide uren:')
    b_hours = raw_input('Begeleide uren:')
    gen_act = raw_input('Algemene activiteit:')
    write_file(date, hours, u_hours, b_hours, gen_act)

user_activity()
