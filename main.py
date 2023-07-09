def mostrar_menu():
    print("Menú:")
    print("1. Windows 10 Home")
    print("2. Windows 10 Pro")
    print("3. Windows 10 Home Single Language")
    print("4. Windows 10 Enterprise")
    print("5. Windows 10 Education")
    print("6. Windows 10 S")
    print("0. Salir")

def mostrar_claves_windows(version):
    if version == 1:
        print("Claves de Windows 10 Home:")
        print("TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        print("KTNPV-KTRK4-3RRR8-39X6W-W44T3")
        print("YTMG3-N6DKC-DKB77-7M9GH-8HVX7")
        print("4CPRK-NM3K3-X6XXQ-RXX86-WXCHW")
        print("AKJUS-WY2CT-JWBJ2-T68TQ-YBH2V")
        print("BT79Q-G7N6G-PGBYW-4YWX6-6F4BT")
    elif version == 2:
        print("Claves de Windows 10 Pro:")
        print("VK7JG-NPHTM-C97JM-9MPGT-3V66T")
        print("8N67H-M3CY9-QT7C4-2TR7M-TXYCV")
        print("2B87N-8KFHP-DKV6R-Y2C8J-PKCKT")
        print("DXG7C-N36C4-C4HTG-X4T3X-2YV77")
        print("WYPNQ-8C467-V2W6J-TX4WX-WT2RQ")
        print("AKSIU-WY2CT-JWBJ2-T68TQ-YBH2V")
        print("AJUYS-8C467-V2W6J-TX4WX-WT2RQ")
    elif version == 3:
        print("Claves de Windows 10 Home Single Language:")
        print("7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH")
        print("NKJFK-GPHP7-G8C3J-P6JXR-HQRJR")
    elif version == 4:
        print("Claves de Windows 10 Enterprise:")
        print("NPPR9-FWDCX-D2C8J-H872K-2YT43")
        print("CKFK9-QNGF2-D34FM-99QX2-8XC4K")
        print("DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4")
        print("WNMTR-4C88C-JK8YV-HQ7T2-76DF9")
        print("2F77B-TNFGY-69QQF-B8YKP-D69TJ")
        # Agrega más claves si es necesario
    elif version == 5:
        print("Claves de Windows 10 Education:")
        print("NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
        print("2WH4N-8QGBV-H22JP-CT43Q-MDWWJ")
        print("YNMGQ-8RYV3-4PGQ3-C8XTP-7CFBY")
        print("6TP4R-GNPTD-KYYHQ-7B7DP-J447Y")
        print("84NGF-MHBT6-FXBX8-QWJK7-DRR8H")
        # Agrega más claves si es necesario
    elif version == 6:
        print("Claves de Windows 10 S:")
        print("3NF4D-GF9GY-63VKH-QRC3V-7QW8P")
    else:
        print("Opción no válida")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = int(input("Selecciona una opción: "))

        if opcion == 0:
            break

        mostrar_claves_windows(opcion)
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
