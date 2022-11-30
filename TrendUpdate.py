import time
import rrdtool
from getSNMP import consultaSNMP
rrdpath = '/home/erick/Documentos/Redes3/RRD/'
carga_CPU = 0
carga_RAM = 0
carga_RED = 0
oid_cpu1 = '1.3.6.1.2.1.25.3.3.1.2.196608'
oid_cpu2 = '1.3.6.1.2.1.25.3.3.1.2.196609'

oid_ram ="1.3.6.1.4.1.2021.4.6.0"#antes del 0 un 5 para ram total
oid_ram2 ="1.3.6.1.4.1.2021.4.5.0"
#entrada de trafico de red
oid_red= "1.3.6.1.2.1.2.2.1.16.2"
oid_red1 =".1"
oid_red2 =".2"
#salida de trafico de red
oid_red_s= "1.3.6.1.2.1.2.2.1.10.2"
oid_red1_s =".1"
oid_red2_s =".2"

def actualizar_todo(comunidad,localhost):
    while 1:
        carga_CPU1 = int(consultaSNMP(comunidad, localhost, oid_cpu1))
        carga_CPU2 = int(consultaSNMP(comunidad, localhost, oid_cpu2))
        

        suma = (carga_CPU1+carga_CPU2)/2

        carga_RAM = (int(consultaSNMP(comunidad, localhost, oid_ram2)) - int(
            consultaSNMP(comunidad, localhost, oid_ram))) * 100 / int(
            consultaSNMP(comunidad, localhost, oid_ram2))

        carga_RED_1 = int(int(consultaSNMP(comunidad,localhost,oid_red))  ) /1024
        carga_RED_2= int(consultaSNMP(comunidad,localhost,oid_red_s))/1024

        valor = "N:" + str(suma)+ ":" +str(carga_RAM)+":" +str(carga_RED_1)+":" +str(carga_RED_2)
        print (valor)
        rrdtool.update(rrdpath+'trend.rrd', valor)
        rrdtool.dump(rrdpath+'trend.rrd','trend.xml')
        time.sleep(5)

    if ret:
        print (rrdtool.error())
        time.sleep(300)

#actualizar_todo(comunidad="comunidadSNMP",localhost="Localhost")