
import sys      # leer argumentos
import urllib2  # pedir url donde buscar

print sys.argv

# Comprobamos que han puesto el nombre
if len(sys.argv) < 2:
    print 'falta el nombre de la peli'
    sys.exit(1)

name = sys.argv[1]

# Hacemos la busqueda en la pagina
response = urllib2.urlopen('http://www.mejortorrent.com/secciones.php?sec=buscador&valor=' + str.replace(name,' ','+'))

# Comprobamos que el proveedor nos contesta
if response.getcode() != 200:
    print 'error de la web del proveedor: {}'.format(response.getcode())
    sys.exit(1)

# Damos respuesta a nuestro cliente
print response.read()
    
    
