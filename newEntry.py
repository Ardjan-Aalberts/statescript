import bs4
from bs4 import *
import BeautifulSoup
from BeautifulSoup import *

with open("test.html") as inf:
    txt = inf.read()
    soup = BeautifulSoup(txt)
    mem_attr = ['Dag', 'Uren', 'PVB uren', 'Werkzaamheden']
    em_attr = ['Maandag', '6', '2', 'Documentatie']
    html = Tag(soup, "html")
    table = Tag(soup, "table")
    tr = Tag(soup, "tr")
    td = Tag(soup, "td")
    soup.append(html)
    html.append(table)
    table.append(tr)
    for attr in mem_attr:
        th = Tag(soup, "th")
        tr.append(th)
        th.append(attr)

    tr = Tag(soup, "tr")
    table.append(tr)

    for em in em_attr:
        td = Tag(soup, "td")
        tr.append(td)
        td.append(em)


print soup.prettify()
with open("test.html", "w") as outf:
    outf.write(str(soup))




# load the file
# with open("test.html") as inf:
#     txt = inf.read()
#     soup = bs4.BeautifulSoup(txt, 'html.parser')
#
# # create new link
# new_link = soup.encode("<tr>"
#                            "<td>Maandag</td>"
#                            "<td>8</td> <td>5</td>"
#                            "<td>Documentatie schrijven</td>"
#                            "</tr>")
# # insert it into the document
# soup.head.append(new_link)

# save the file again
# with open("test.html", "w") as outf:
    # outf.write(str(soup))