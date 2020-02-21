import time
import subprocess
import psutil

def get_cpu_temp():
    return int(subprocess.run(["cat", "/sys/class/thermal/thermal_zone0/temp"], capture_output=True).stdout)

def get_cpu_usage():
    return psutil.cpu_percent()

def get_next_int():
    return int(((get_cpu_temp()*get_cpu_usage()) * time.time()) % 100)
    
def main():
    while True:
        s = ''
        for i in range(100):
            ni = get_next_int()
            if ni > 0:
                s += str(ni) + ' '
        print(s)
        time.sleep(1)
        
main()
