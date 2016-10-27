# Nativo de python
import sys      # leer argumentos
import urllib.request   # pedir url donde buscar

# No nativo de python
from bs4 import BeautifulSoup

# Comprobamos que han puesto el nombre
if len(sys.argv) < 2:
    print('falta el nombre de la peli')
    sys.exit(1)

name = sys.argv[1]


def request_url(url):
    response = urllib.request.urlopen(url) 
    if response.getcode() != 200:
        print('error de la web del proveedor: {}'.format(response.getcode()))
        sys.exit(1)
    return BeautifulSoup(response.read(), 'html.parser')
    

# Hacemos la busqueda en la pagina
#response = urllib.request.urlopen('http://www.mejortorrent.com/secciones.php?sec=buscador&valor=' + str.replace(name,' ','+'))

# Comprobamos que el proveedor nos contesta
#if response.getcode() != 200:
#    print('error de la web del proveedor: {}'.format(response.getcode()))
#    sys.exit(1)

# Damos respuesta a nuestro cliente
#soup = BeautifulSoup(response.read(), 'html.parser')

page = request_url('http://www.mejortorrent.com/secciones.php?sec=buscador&valor=' + str.replace(name,' ','+'))

films = []
series = []

for link in page.find_all('a'):
    href = link.get('href')
    
    if href is not None and href.startswith('/peli-'):
        films.append(link)

    elif href is not None and href.startswith('/serie-'):
        series.append(link)

def to_title(link):
    return ''.join([str(s) for s in link.contents]).replace('<font color="darkblue">', '').replace('</font>','')

if len(films) > 0:
    print('Peliculas encontradas:')
    for i, film in enumerate(films):
        print(' [f{}] {}'.format(i, to_title(film)))

if len(series) > 0:
    print('Series encontradas:')
    for i, serie in enumerate(series):
        print(' [s{}] {}'.format(i, to_title(serie)))

op = input('Seleccione una opcion: ')

try:
    op_type = op[0]
    op_index = int(op[1:])
except:
    print('Entrada no valida')
    sys.exit(1)

if op_type == 'f' and op_index < len(films) and op_index >=0:
    url = films[op_index].get('href')
elif op_type == 's'and op_index < len(series) and op_index >=0:
    url = series[op_index].get('href')
else:
    print('Opcion no valida')
    sys.exit(1)
    
page = request_url('http://www.mejortorrent.com' + url)
links = page.findAll('a', text='Descargar')

if len(links) == 0:
    print('Enlace no encontrado')
    sys.exit(1)

url = 'http://www.mejortorrent.com/' + links[0].get('href')

page = request_url(url)
links = page.findAll('a',text='aquí')
if len(links) == 0:
    print('Enlace no encontrado')
    sys.exit(1)

url = 'http://www.mejortorrent.com' + links[0].get('href')

urllib.request.urlretrieve(url, '/home/pi/Downloads/autopeli.torrent')

import ipdb; ipdb.set_trace()


    
