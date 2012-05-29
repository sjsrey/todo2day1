"""
todo2day1.py

Post list of completed items from todo.txt to DayOne

"""

__version__ = "0.1"
__date__ = "2012-05-29"
__author__ = "Serge Rey <sjsrey@gmail.com>"
__copyright__ = "Copyright 2012, Sergio Rey"
__license__ = "GPL"
__history__ = """
0.1 - initial release 2012-05-29
"""

import datetime
import shlex, subprocess

TODAY = str(datetime.date.today())
TODO = "/Users/serge/Dropbox/todo/todo.txt"
DONE = "/Users/serge/Dropbox/todo/done.txt"
DAYONE = "/Applications/Day\ One.app/Contents/MacOS/dayone"

# Get completed items
fTodo = open(TODO,'r')
todoLines = fTodo.readlines()
fTodo.close()

fDone = open(DONE,'r')
doneLines = fDone.readlines()
fDone.close()

reportLines = []
for line in todoLines:
    if line[0] == 'x':
        reportLines.append(line)
for line in doneLines:
    if line[0] == 'x':
        reportLines.append(line)

# get only items completed TODAY
reportLines = [ line for line in reportLines if TODAY in line]

# Format for and post to DayOne
s = "todo.txt report for %s\n"%TODAY
ns = len(s)-1
s += "="*ns
s += "\n"
s = s + "\n".join(reportLines)

cmd = "echo \"%s\" | %s new"%(s,DAYONE)
out = subprocess.call(cmd, shell=True)
