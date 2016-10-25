# Nativo de python
import sys      # leer argumentos
import urllib.request  # pedir url donde buscar

# No nativo de python
from bs4 import BeautifulSoup

# Comprobamos que han puesto el nombre
if len(sys.argv) < 2:
    print('falta el nombre de la peli')
    sys.exit(1)

name = sys.argv[1]

# Hacemos la busqueda en la pagina
response = urllib.request.urlopen('http://www.mejortorrent.com/secciones.php?sec=buscador&valor=' + str.replace(name,' ','+'))

# Comprobamos que el proveedor nos contesta
if response.getcode() != 200:
    print('error de la web del proveedor: {}'.format(response.getcode()))
    sys.exit(1)

# Damos respuesta a nuestro cliente
soup = BeautifulSoup(response.read(), 'html.parser')

films = []
series = []

for link in soup.find_all('a'):
    href = link.get('href')
    
    if href is not None and href.startswith('/peli-'):
        films.append(link)

    elif href is not None and href.startswith('/serie-'):
        series.append(link)

def to_title(link):
    return ''.join([str(s) for s in link.contents]).replace('<font color="darkblue">', '').replace('</font>','')

print('peliculas encontradas')
for film in films:
    print(to_title(film))

print('series encontradas')
for serie in series:
    print(to_title(serie))
    
#print(soup.prettify())


    
