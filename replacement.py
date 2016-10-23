# -*- coding: utf-8 -*-

import os
import sys
import re

# define the dict which need to be replaced
trans = {

"<count>":"<section style=\"box-sizing: border-box\"><section style=\"box-sizing: border-box; margin-top: 10px; margin-bottom: 10px\"><section style=\"box-sizing: border-box; margin-top: 10px; margin-bottom: 10px; text-align: center\"><section style=\"display: inline-block vertical-align: top; padding: 5px;, width: 50%; box-sizing: border-box\"><section style=\"box-sizing: border-box; margin: auto; width: 120px; color: #666; font-size: 15px\"><strong><p>本篇字数约</p><span style=\"color: #00b893; font-size: 16px\">",

"</count>":"</span></strong></section></section></section></section></section><hr style=\"display: block; height: 1px; border: 0; border-top: 1px solid #eee; margin: 1em 50px; padding: 0\"/>",

"<h1>":"<h1 style=\" box-sizing: border-box; margin-top: 21px; margin-bottom: 10.5px; font-size: 30px\">",

"<h2>":"<h2 style=\" box-sizing: border-box ; margin-top: 16px; margin-bottom: 8px; font-size: 28px\">",

"<h3>":"<h3 style=\" color: #009ab8; border-bottom: 5px solid #009ab8; box-sizing: border-box ; margin-top: 23px; margin-bottom: 0px; margin-right: 10px; margin-left: 10px; font-size: 25px\">",

"<h4>":"<h4 style=\" color: #2AAAB7; border-bottom: 2px solid #2AAAB7; box-sizing: border-box ; margin-top: 12px; margin-bottom: 0px; margin-left: 10px; margin-right: 10px; font-size: 23px \">",

"<h5>":"<h5 style=\" box-sizing: border-box ; margin-top: 10px; margin-bottom: 5px; font-size: 20px\">",

"<h6>":"<h6 style=\" box-sizing: border-box ; margin-top: 8px; margin-bottom: 4px; font-size: 15px\">",

"<p>":"<p style=\" color: #666; margin: 9px 10px 20px 10px; line-height: 1.6; min-height: 1em; font-size: 17px\">",

"<ol>":"<ol style=\" color: #00b893; margin: 20px; line-height: 1.5; min-height:1em\">",

"<ul>":"<ul style=\" color: #00b893; margin: 20px; line-height: 1.5; min-height:1em\">",

"<li>":"<li><p style=\" color: #666; margin: 20px; line-height: 1.5; min-height: 1em; font-size: 17px\">",

"</li>":"</p></li>",

"<strong>":"<strong style=\" color: #444\">",

"<blockquote>":"<blockquote style=\"background: #f9f9f9; border-left: 10px solid #ccc; margin: 1.5em 10px; padding: 0.5em 10px\">"

}



# open the raw html file
src_file_name = sys.argv[1]
src_file = open(src_file_name, 'r')
# get the raw html file content
content = src_file.read()


# define a temp variable to make out the output file's name
temp_file = src_file_name.split('.')

# define the output file name
des_file_name = temp_file[0] + "_modified." + temp_file[1]
des_file = open(des_file_name, 'w')

for stext in trans:
    content = content.replace(stext, trans[stext])
    #print "The Source " + stext + " has been replaced by " + trans[stext]
    print stext
    #print "*" * 10

des_file.write(content)

src_file.close()
des_file.close()
