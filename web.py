#! /usr/bin/python3.4

"""
Web interface code
"""

import core

def get_header(title):
    return """
    <!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01 Transitional//EN'
    'http://www.w3.org/TR/html4/loose.dtd'>
    <html>
    <head>
    <title>{}</title>
    <link rel="stylesheet" type="text/css"
        media="all" href="http://fonts.googleapis.com/css?family=PT%20Sans" />
    <link rel='stylesheet' type='text/css'
          href='static/css/jquery-ui.min.css' />
    <link rel='stylesheet' type='text/css'
          href='static/css/main.css' />
    <script type="text/javascript" src="static/js/underscore-min.js"></script>
    <script type="text/javascript" src="static/js/jquery.min.js"></script>
    <script type="text/javascript" src="static/js/jquery-ui.min.js"></script>
    <script type="text/javascript" src="static/js/blackbox.js"></script>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name='description'
        content="Blackbox puzzle game">
    <meta name='keywords'
        content="puzzle, game, blackbox">
    </head>
    """.format(title)

def get_table(side_len):
    """
    Number outer, non-corner cells from bottom left as 1 going around
    anti-clockwise.
    """
    coordinates = core.get_atom_coords(side_len)
    # top row
    top_cells = []
    for i in range(3*side_len-1, 2*side_len-1, -1):
        top_cells.append("<td class='numbered' id='{num}'>{num}</td>"
            .format(num=i+1))
    top_cells_html = "".join(top_cells)
    top_row_html = ("<tr><td class='corner'></td>" + top_cells_html
        + "<td class='corner'></td></tr>")
    # middle
    right_entry_nums = range(2*side_len, side_len, -1)
    left_entry_nums = range(3*side_len+1, 4*side_len+1)
    entry_num_pairs = zip(left_entry_nums, right_entry_nums)
    mid_rows = []
    for y, entry_num_pair in enumerate(entry_num_pairs,1):
        left_entry_num, right_entry_num = entry_num_pair
        inside_mid_row_list = []
        for x in range(1,side_len+1):
            coord_id = "{},{}".format(x,y)
            inside_mid_row_list.append("<td align=center class='middle' "
                "id='{coord_id}'></td>".format(coord_id=coord_id))
        inside_mid_row = "\n".join(inside_mid_row_list)
        mid_row = ("<tr><td class='numbered' id='{num}'>{num}</td>\n"
                .format(num=left_entry_num)
            + inside_mid_row + "\n<td class='numbered' "
                "id='{num}'>{num}</td></tr>".format(num=right_entry_num))
        mid_rows.append(mid_row)
    mid_rows_html = "\n".join(mid_rows)
    # bottom row
    bottom_cells = []
    for i in range(side_len):
        bottom_cells.append("<td class='numbered' id='{num}'>{num}</td>"
            .format(num=i+1))
    bottom_cells_html = "".join(bottom_cells)
    bottom_row_html = ("<tr><td class='corner'></td>" + bottom_cells_html
        + "<td class='corner'></td></tr>")
    # assemble
    rows_html = top_row_html + "\n" + mid_rows_html + "\n" + bottom_row_html
    html = """
    <table>
    <tbody>
    {}
    
    </tbody>
    </table>
    """.format(rows_html)
    return html
