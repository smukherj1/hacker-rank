from subprocess import Popen
import sys
import time

def cmd_line_help():
	print '''
This program expects exactly two arguments in the following order:-
<script name> <test name>

where <script name> is the name of a script file in code/
and <test name> is the name of a text file in testcase/
'''

if len(sys.argv) != 3:
	cmd_line_help()
	exit(-1)

script = sys.argv[1]
test = sys.argv[2]

try:
	open('code/' + script)
	script = 'code/' + script
except:
	try:
		open(script)
	except:
		print 'Error: script file', script, 'does not exist!'
		exit(-1)
tfh = None
try:
	tfh = open('testcase/' + test)
except:
	try:
		tfh = open(test)
	except:
		print 'Error: test file', test, 'does not exist!'
		exit(-1)

start = time.time()
p = Popen(['python', script], stdin=tfh, stdout=sys.stdout)
if p.wait() != 0:
	print 'EXECUTION FAILED'
print 'Elapsed time %d seconds'%(time.time() - start)
