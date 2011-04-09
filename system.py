import subprocess

UN_RELEASE = subprocess.getoutput("uname -r")
UN_TZ = subprocess.getoutput("cat /etc/timezone")
UN_MODEL = subprocess.getoutput("cat /etc/issue")
UN_SERIAL = subprocess.getoutput("sudo /usr/sbin/dmidecode | grep UUID")
UN_CPUCOUNTS = subprocess.getoutput("cat /proc/cpuinfo | grep processor | wc -l")
UN_PHYCPUS = subprocess.getoutput("grep \"physical id\" /proc/cpuinfo | sort -u | wc -l")
PER_CORES = subprocess.getoutput("grep \"cores\" /proc/cpuinfo | sort -u | cut -d\':\' -f2")

print (UN_SERIAL)
print (UN_MODEL)
print (UN_TZ)
print (UN_RELEASE)
print (UN_CPUCOUNTS)
print (UN_PHYCPUS)
print (PER_CORES)
