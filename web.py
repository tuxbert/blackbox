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
    <link rel='stylesheet' type='text/css'
          href='static/css/main.css' />
    <link rel='stylesheet' type='text/css'
          href='static/css/print.css'
          media='print' />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name='description'
        content="Blackbox puzzle game">
    <meta name='keywords'
        content="puzzle, game, blackbox">
    </head>
    """.format(title)

def get_table(side_len):
    coordinates = core.get_coordinates(side_len)
    rows = ("\n    <tr><td class='inner_default'>" + "</td><td class='inner_default'>"*side_len + "</td></tr>")*side_len
    html = """
    <table>
    <tbody>
    {}
    
    </tbody>
    </table>
    """.format(rows)
    return html
