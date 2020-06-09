import csv
# write the file name of the csv you wnat to convert to html table
in_file= "How_many_people_have_read_from_the_genre_Young_Adult.csv"

# open the file
# set the separator (deliminter) to , but not to use if in double quotes (why?)
# counting rows
# start the html table string
# start each new row with a <tr>
# if it is the first row set table header  cells
# not, regular <td> cells
# close the row
with open(in_file, newline='') as csvfile:
    my_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    row_num = 0
    my_table = "<table>\n"
    for row in my_reader:
        my_table += "<tr>"
        for x in row:
            if row_num == 0:
                my_table +="<th>{}</th>".format(x)
            else:
                my_table +="<td>{}</td>".format(x)
        my_table +="</tr>\n"
        row_num += 1
    my_table+="</table>"
    print(my_table)
