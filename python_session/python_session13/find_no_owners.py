"""
uniq_uids1 = set()

with open("/etc/passwd")as f:
	for line in f.readlines():
		uniq_uids1.add(line.split(":")[2])
print "Unique IDs length:", len(uniq_uids1)
"""
import pwd
import os
uniq_uids2 = set()
for user in pwd.getpwall():
	uniq_uids2.add(user.pw_uid)

#print "Unique IDs length:", len(uniq_uids2)
home_path = os.getcwd()
for p, sd, fs in os.walk(home_path):
	for ef in fs:
		ef_wp = p+"/"+ef
		if os.path.islink(ef_wp):
			print "{0} is a symbolic link and skipping....".format(ef_wp)
			continue
		v = os.stat(ef_wp)
		if v.st_uid not in uniq_uids2:
			print "the file", ef_wp,"has no owner"


