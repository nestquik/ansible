#!/usr/bin/env python

from subprocess import call, PIPE, Popen

out = Popen(['authconfig', '--test'], stdout=PIPE)
out_list = out.communicate()[0].split('\n')


hash_ = [i for i, string in enumerate(out_list) if 'ALGORITHM' in string.upper()]


for i in hash_:
	hash = out_list[i].split(' ')[-1]
	with open("/tmp/restore_passhash.py", "w") as f:
		f.write("#!/usr/bin/env python")
		f.write('\n')
		f.write("from subprocess import call")
		f.write('\n')
                auth_str = "call([\"authconfig\", \"--passalgo="+hash+"\", \""+"--update\"])"
		f.write(auth_str)
