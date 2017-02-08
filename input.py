import datetime

import BeautifulSoup

today = datetime.date.today()
print str(today)

standard_count_tr_tags = 4
every_new_entry_tr_tags = 1


def write_file(week, date, hours, u_hours, b_hours, gen_act):
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
    hours = raw_input('Gemaakte uren:')
    u_hours = raw_input('Onbegeleide uren:')
    b_hours = raw_input('Begeleide uren:')
    gen_act = raw_input('Algemene activiteit:')

    if not date:
        date = str(today)
    write_file(week, date, hours, u_hours, b_hours, gen_act)


def count_entries():
    with open("output.html") as inf:
        txt = inf.read()
        soup = BeautifulSoup.BeautifulSoup(txt)
        return len(soup.findAll('tr'))
print count_entries()

user_activity()
