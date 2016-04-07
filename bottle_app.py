#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 11 - bottle_app.py
# A simple web application built using the Bottle micro-framework.

import base64, bottle
import sqlite3
bottle.debug(True)
app = bottle.Bottle()

username=None

@app.route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='/path/to/your/static/files')

@app.route('/encode')
@bottle.view('chat.html')
def encode():
    username = bottle.request.GET.get('username')
    isi = bottle.request.GET.get('isi')
    if username is None:
        bottle.abort(400, 'This form requires a "username" parameter')
    else :
		conn = sqlite3.connect('chat.db')
		c = conn.cursor()
		c.execute("INSERT INTO lines (username,isi) VALUES (?,?)", (username,isi))
		new_id = c.lastrowid
		conn.commit()
		c.close()
		#simpan(username+';'+isi)
        #x = open("hasil.txt", "r")
        #semua = x.read()
        #x.close()
    return template('chat.html')

@app.route('/')
@bottle.view('chat.html')
def index():
    username = bottle.request.GET.get('username')
    isi = bottle.request.GET.get('isi')
    if username is not None:
        conn = sqlite3.connect('chat.db')
        c = conn.cursor()
        c.execute("INSERT INTO lines (username,isi) VALUES (?,?)", (username,isi))
        new_id = c.lastrowid
        conn.commit()
        c.close()
        print(username);
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute("SELECT username, isi FROM lines")
    result = c.fetchall()
    c.close()
    return dict(username=None, rows=result)

def simpan(data):
    file = open("hasil.txt", "a")
    tulis = data
    file.write(tulis)
    file.close()
    return
def load():
	conn = sqlite3.connect('chat.db')
	c = conn.cursor()
	c.execute("SELECT username, isi FROM chat")
	result = c.fetchall()
	c.close()
	return str(rows=result)
bottle.run(app=app, host='localhost', port=8080)
