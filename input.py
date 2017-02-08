import datetime

import BeautifulSoup

today = datetime.date.today()
print str(today)

standard_count_tr_tags = 3
every_new_entry_tr_tags = 1


def write_file(week, date, hours, u_hours, gen_act):
    with open("output.html") as inf:
        txt = inf.read()
        txt += '\r\n'
        new_entry = '<tr> \r\n  <td>{4}</td>\r\n <td>{0}</td>\r\n <td>{1}</td>\r\n <td>{2}</td>\r\n <td>{3}</td>\r\n ' \
                    '</tr>\r\n'.format(date, hours, u_hours, gen_act, week)
        txt += new_entry
        with open("output.html", "w") as outf:
            outf.write(txt)


def user_activity():
    week = raw_input('Week:')
    date = raw_input('Datum: (leave empty if it is ' + str(today) + ')')
    hours = raw_input('Gemaakte uren (leave empty if it is 8):')
    b_hours = raw_input('PvB uren (leave empty if it is 2):')
    gen_act = raw_input('Algemene activiteit:')

    if not date:
        date = str(today)
    if not hours:
        hours = 8
    if not b_hours:
        b_hours = 2
    write_file(week, date, hours, b_hours, gen_act)


def count_entries():
    with open("output.html") as inf:
        txt = inf.read()
        soup = BeautifulSoup.BeautifulSoup(txt)
        return len(soup.findAll('tr'))


def check_file():
    max_entries = (standard_count_tr_tags + 5)
    c = count_entries()
    if c >= max_entries:
        print 'You have your previous file filled out for one week, I\'ll create a new one'

    print 'Entries: {0}'.format(c)

check_file()
user_activity()
