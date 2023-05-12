from formatters import formatPriceEuro
from scrape import scrapeCarulla, scrapeEuro, scrapeExito, scrapeJumbo

# Ejecuta las funciones de scraping de la tienda Euro

# Lacteos
scrapeEuro('https://www.eurosupermercados.com.co/leche-colanta-entera-1000ml.html', 'Lacteos','0')
scrapeEuro('https://www.eurosupermercados.com.co/mantequilla-c-sal-250gr-colanta.html', 'Lacteos', '1')
scrapeEuro('https://www.eurosupermercados.com.co/queso-crema-colanta-400gr.html', 'Lacteos', '2')
scrapeEuro('https://www.eurosupermercados.com.co/queso-parmesano-rallado-x-250gr-alpina.html', 'Lacteos', '3')
scrapeEuro('https://www.eurosupermercados.com.co/queso-mozarella-taj-500gr-colanta.html', 'Lacteos', '4')

# Ejecuta las funciones de scraping de la tienda Éxito

# Lacteos
scrapeExito('https://www.exito.com/leche-entera-en-bolsa-x-1-litro-125079/p', 'Lacteos', '0')
scrapeExito('https://www.exito.com/mantequilla-c-sal-barra-496847/p', 'Lacteos', '1')
scrapeExito('https://www.exito.com/queso-crema-x-400g-101497/p', 'Lacteos', '2')
scrapeExito('https://www.exito.com/queso-parmesano-x-250g-61417/p', 'Lacteos', '3')
scrapeExito('https://www.exito.com/queso-mozzarella-x-30-tajadas-500-gr-31320/p', 'Lacteos', '4')

# Ejecuta las funciones de scraping de la tienda Carulla

# Lacteos
scrapeCarulla('https://www.carulla.com/leche-entera-en-bolsa-x-1-litro-125079/p', 'Lacteos', '0')
scrapeCarulla('https://www.carulla.com/mantequilla-sin-sal-barra-x-250-gr-61169/p', 'Lacteos', '1')
scrapeCarulla('https://www.carulla.com/queso-crema-x-400g-101497/p', 'Lacteos', '2')
scrapeCarulla('https://www.carulla.com/queso-parmesano-x-250g-61417/p', 'Lacteos', '3')
scrapeCarulla('https://www.carulla.com/queso-mozzarella-x-30-tajadas-500-gr-31320/p', 'Lacteos', '4')

# Ejecuta las funciones de scraping de la tienda Jumbo

# Lacteos
scrapeJumbo('https://www.tiendasjumbo.co/leche-entera-liquida-x-1000cm3-colanta/p', 'Lacteos','0')
scrapeJumbo('https://www.tiendasjumbo.co/mantequilla-con-sal-x-250-g-colanta/p', 'Lacteos','1')
scrapeJumbo('https://www.tiendasjumbo.co/queso-crema-colanta-x-400g/p', 'Lacteos','2')
scrapeJumbo('https://www.tiendasjumbo.co/queso-parmesano-bolsa-x-250g-alpina/p', 'Lacteos','3')
scrapeJumbo('https://www.tiendasjumbo.co/queso-mozzarella-tajado-x-500-g-colanta/p', 'Lacteos','4')
