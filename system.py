import subprocess

def exec_command(cmdList):
  p = subprocess.Popen(cmdList, stdout=subprocess.PIPE)
  output = p.stdout
  result = ''
  for line in output:
     if (line != ''):
        #print line.rstrip('\n')
        result = result + line
  return result;


def cleanup_str(str):
   if (str != ''):
      str = str.replace('\n','')
      str = str.replace('\l','')
   return str;

def find_uuid(str):
   if (str != ''):


UN_RELEASE_CMD = ["uname", "-r"]
UN_TZ_CMD = ["cat", "/etc/timezone"]
UN_MODEL_CMD = ["cat", "/etc/issue"]
UN_SERIAL_CMD = ["sudo", "/usr/sbin/dmidecode"]


result = exec_command(UN_RELEASE_CMD)
result = cleanup_str(result)
print result

result = exec_command(UN_TZ_CMD)
result = cleanup_str(result)
print result

result = exec_command(UN_MODEL_CMD)
result = cleanup_str(result)
print result

result = exec_command(UN_SERIAL_CMD)
print result


#UN_CPUCOUNTS = subprocess.getoutput("cat /proc/cpuinfo | grep processor | wc -l")
#UN_PHYCPUS = subprocess.getoutput("grep \"physical id\" /proc/cpuinfo | sort -u | wc -l")
#PER_CORES = subprocess.getoutput("grep \"cores\" /proc/cpuinfo | sort -u | cut -d\':\' -f2")
