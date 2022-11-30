import rrdtool
ret = rrdtool.create("/home/erick/Documentos/Redes3/RRD/trend.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:CPUload:GAUGE:60:0:100",
                     "DS:RAMload:GAUGE:60:0:100",
                     "DS:IntOctets:COUNTER:30:U:U",
                     "DS:OutOctets:COUNTER:30:U:U",
                     "RRA:AVERAGE:0.5:1:24")
if ret:
    print (rrdtool.error())