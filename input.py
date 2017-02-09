import datetime
import json
import BeautifulSoup
import pdfkit
import os
import sys

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
    add_hours(hours)
    check_file()


def count_entries():
    with open("output.html") as inf:
        txt = inf.read()
        soup = BeautifulSoup.BeautifulSoup(txt)
        return len(soup.findAll('tr'))


def get_output_html():
    with open("output.html") as inf:
        txt = inf.read()
    return txt


def add_hours(hours):
    with open('data.json', 'r+') as f:
        data = json.load(f)
        data['Hours'] += hours
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()


def check_file():
    max_entries = (standard_count_tr_tags + 5)
    c = count_entries()
    if c >= max_entries:
        print 'You have your previous file filled out for one week, I\'ll create a new one'
        add_total_hours_bar()
        archive_file_name = get_week()
        path = sys.path[0]
        output_file_path = os.path.join(path, 'output.html')
        pdf_name = archive_file_name + 'pdf'
        pdfkit.from_url(output_file_path, pdf_name)
        new_file_location = os.path.join(path, '{0}.html').format(archive_file_name)

        full_file = get_output_html()
        with open(new_file_location, 'w') as inf:
            inf.write(full_file)
        print 'Archived everything!'

        print 'Generating a new file.'
        week = get_week()
        # deleting old file
        clear_output_file()
        # creating a new file
        generate_new_html_file()
        new_name = raw_input('New week is? (old week was: ' + week + ')')
        set_week(new_name)
        set_hours(0)
    print 'Entries: {0}'.format(c)


def get_hours():
    with open('data.json', 'r+') as f:
        data = json.load(f)
        hours = data['Hours']
        return hours


def get_week():
    with open('data.json', 'r+') as f:
        data = json.load(f)
        week = data['Week']
        return week


def set_week(week):
    with open('data.json', 'r+') as f:
        data = json.load(f)
        data['Week'] = week
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    return True


def set_hours(hours=0):
    with open('data.json', 'r+') as f:
        data = json.load(f)
        data['Hours'] = hours
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    return True


def add_total_hours_bar():
    hours = get_hours()
    with open("output.html") as inf:
        txt = inf.read()
        txt += '\r\n'
        new_entry = '</table><table><tr class="table table-bordered">' \
                    '<th class="heading">Totaal aantal gewerkt uren: {0} ' \
                    '</th></tr></table>'.format(hours)
        txt += new_entry
        with open("output.html", "w") as outf:
            outf.write(txt)


def generate_new_html_file():
    with open('output.html', 'w') as outf:
        html = get_static_output_file()
        outf.write(html)
    return True


def get_static_output_file():
    with open('staticHEADHTML.html') as inf:
        txt = inf.read()
        return txt


def clear_output_file():
    open('output.html', 'w').close()


check_file()
user_activity()
