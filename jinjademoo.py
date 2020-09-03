# SCRIPT:jinjademo.py
# AUTHOR: Himanshu Upadhyay
# DATE:   03/09/2020
# REV:    1.1.A (Valid are A, B, D, T and P)
#          (For Alpha, Beta, Dev, Test and Production)
#
#
# PLATFORM: Ubuntu
#
# PURPOSE: Using Jinja with Dictionary
# REV LIST:
#    DATE        : Date of revision
#    BY          : AUTHOR OF MODIFICATION
#    MODIFICATION: Describe the chages made. What do they enhance.
#
# set -n   # Uncomment to check script syntax, without execution.
#          # Note: Do forget comment it back as it won't allow the
#          # the script to execute.
#
# set -x   # Uncomment this for debugging this shell script.
#
#
################################################################
#          Imports Here                                        #
from jinja2 import Template
################################################################
################################################################
#          Define Files and Variables here                     #

from jinja import Template
data1 ={'Name':'Himanshu','Role':'Intern','Organization':Knoldus,'eid':101}
data2={'Name':'pratik','Role':'Intern','Organization':Knoldus,'eid':102}
data3={'Name':'Vidushi','Role':'Intern','Organization':Knoldus,'eid':103}
dictionary={'peer1':data1,'peer2':data2,'peer3':data3}

def funct():
    for i in dictionary:

        temp=Template("Hello My Name is {{i['Name']}} ,My Role is {{i['Role]'}} in {{i['Organization']}}  and My employee id  is{{i['eid']}}")

        final=temp.render(i=dictionary[i])
        print(final)

################################################################
################################################################
################################################################
################################################################

#          Beginning of Main                                   #
funct()
################################################################
################################################################
################################################################

