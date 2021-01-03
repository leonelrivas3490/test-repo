from netmiko import ConnectHandler
from pprint import pprint
import time
import os
import csv

def opc1_fun():
        os.system("cls")   
        pprint("------------------------------------------------")
        pprint("|                                              |")
        pprint("|            NETWORKS NIZAR                    |")
        pprint("|                                              |")
        pprint("------------------------------------------------") 
        pprint('')
        rt1 = input('type the name of the device to the connetion: ')
        ip1 = input('type the IP address of the device: ')
        ip_address = {rt1:ip1}
        log_name = rt1
        log_time = time.strftime("_%Y%m%d")
        log_file = log_name + log_time
        for y in ip_address.values():
            R1 = {"device_type":"cisco_ios",
                #"name":ip_address(),
                "host":y,
                "user":"pa_rival5",
                "pass":"~k@YafT6mTK,<u7r",
                }
            try:
                net_connect = ConnectHandler(ip=R1["host"],username=R1["user"],password=R1["pass"],device_type=R1["device_type"])
                interface_status = net_connect.send_command("show interface status")
                cdp_neighbor = net_connect.send_command("show cdp neighbor detail")
                for dev in ip_address.items():
                    log = open("%s.txt" %log_file , "w")
                    log.write("-------------------{}----------------\n".format(dev))
                    log.write("-------------------------------------\n")
                    log.write("                                     \n")
                    log.write("          INTERFACE STATUS(%)        \n")
                    log.write("                                     \n")
                    log.write("-------------------------------------\n")
                    log.write("-----show interface status---------\n")
                    log.write(interface_status)
                    log.write("\n")
                    log.write("-------------------------------------\n")
                    log.write("                                     \n")
                    log.write("           CDP NEIGHBOR              \n")
                    log.write("                                     \n")
                    log.write("-------------------------------------\n")
                    log.write("-----show cdp neighbor---------------\n")
                    log.write(cdp_neighbor)
                    log.write("\n")
                    log.close()
                    pprint(f'script collected for {rt1}!!!')
            except:
                print('-----------ERROR CONNECTION-----------')
                print(f'No fue posible conectar con {rt1}')


def opc2_fun():
        file = open('csvfile.csv')
        reader = csv.reader(file,delimiter=';')
        for line in reader:
            rt1 = line[0]
            ip1 = line[1]
            ip_address = {rt1:ip1}
            log_name = rt1
            log_time = time.strftime("_%Y%m%d")
            log_file = log_name + log_time
            for y in ip_address.values():
                R1 = {"device_type":"cisco_ios",
                    #"name":ip_address(),
                    "host":y,
                    "user":"pa_rival5",
                    "pass":"qn%uD1pB*0!mx-ZE",
                    }
                try:
                    net_connect = ConnectHandler(ip=R1["host"],username=R1["user"],password=R1["pass"],device_type=R1["device_type"])
                    interface_status = net_connect.send_command("show interface status")
                    cdp_neighbor = net_connect.send_command("show cdp neighbor detail")
                    for dev in ip_address.items():
                        log = open("%s.txt" %log_file , "w")
                        log.write("-------------------{}----------------\n".format(dev))
                        log.write("-------------------------------------\n")
                        log.write("                                     \n")
                        log.write("          INTERFACE STATUS(%)        \n")
                        log.write("                                     \n")
                        log.write("-------------------------------------\n")
                        log.write("-----show interface status---------\n")
                        log.write(interface_status)
                        log.write("\n")
                        log.write("-------------------------------------\n")
                        log.write("                                     \n")
                        log.write("           CDP NEIGHBOR              \n")
                        log.write("                                     \n")
                        log.write("-------------------------------------\n")
                        log.write("-----show cdp neighbor---------------\n")
                        log.write(cdp_neighbor)
                        log.write("\n")
                        log.close()
                        pprint(f'script collected for {rt1}!!!')
                except:
                    print('-----------ERROR CONNECTION-----------')
                    print(f'No fue posible conectar con {rt1}')

def get_intbrief():
    os.system("cls")  
    pprint("------------------------------------------------")
    pprint("|                                              |")
    pprint("|            NETWORKS BABYSITTING              |")
    pprint("|                                              |")
    pprint("------------------------------------------------") 
    pprint('')
    pprint('1.- Collect to a Specific Host?')
    pprint('')
    pprint('2.- Collect using a Bult of devices? (CSV_file)')
    pprint('')
    pprint('10. Go back')
    pprint('')  
    opc1 = input('select and option: ')
    if opc1 == "1":
        opc1_fun()
    elif opc1 == "2":
        opc2_fun()
    elif opc1 == "10":
        print('prueba')
    else:
        main()


def main():
    rep = ""
    while rep == "y" or "Y":
        pprint('------------------------------------------------')
        pprint('|                                              |')
        pprint('|            NETWORKS BABYSITTING              |')
        pprint('|                                              |')
        pprint('------------------------------------------------') 
        pprint('1.- Collect specific commands using SSH connection')
        pprint('')
        pprint('2.- Collect specific commands using Telnet connection')
        pprint('')
        pprint('10. Exit')
        pprint('')
        opc = input('type and option: ')
        if opc == "1":
            get_intbrief()
            rep = input('Do you wish to run the script to another device?(y/n): ')
            if rep == 'n' or 'no':
                continue
        elif opc == "2":
            print('conecta usando telnet')
            rep = input("Do you wish to run the script to another device?(y/n): ")
            if rep == "n" or "no":
                continue
        else:
            break 

if __name__ == "__main__":
    main()
