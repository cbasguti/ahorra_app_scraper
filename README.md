# WebScraper for Ahorrapp
WebScraping functionality for Firebase Database

Para actualizar los precios en la base de datos, actualmente soporta scraping para estas tiendas: Exito, Carulla, Jumbo, Euro. Para añadir un producto de una tienda pueden ir al archivo main.py y ahi llamar alguno de los metodos. Se reciba la URL que lleva al producto, la categoría, y el ID. Para el ejemplo, está el producto Lacteos > 0 > Leche 

Para ejecutarlo, primero se mueven a la carpeta src:

```bash
cd src
```

Y luego pueden ejecutar el script de python:

```bash
python main.py
```

Sí no tienen algunos de los paquetes, pueden instalarlos con pip:

```bash
pip install selenium
pip install firebase
```

Si no lo quieren ejecutar no hay problema, me avisan que subieron nuevos productos y yo lo ejecuto.