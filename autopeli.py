
import sys      # leer argumentos
import urllib2  # pedir url donde buscar

print sys.argv

if len(sys.argv) < 2:
    sys.exit ('falta el nombre de la peli')

       
name = sys.argv[1]
response = urllib2.urlopen('http://www.mejortorrent.com/secciones.php?sec=buscador&valor=' + name)

if response.getcode() == 200:
    print response.read()
else:
     print response.getcode()

