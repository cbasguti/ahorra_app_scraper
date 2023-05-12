from scrape import scrapeCarulla, scrapeEuro, scrapeExito, scrapeJumbo

# Ejecuta las funciones de scraping de la tienda Éxito

# Lacteos
scrapeExito('https://www.exito.com/leche-entera-en-bolsa-x-1-litro-125079/p', 'Lacteos', '0')
scrapeExito('https://www.exito.com/mantequilla-c-sal-barra-496847/p', 'Lacteos', '1')

# Ejecuta las funciones de scraping de la tienda Euro

# Lacteos
scrapeEuro('https://www.eurosupermercados.com.co/leche-colanta-entera-1000ml.html', 'Lacteos','0')
scrapeEuro('https://www.eurosupermercados.com.co/mantequilla-c-sal-250gr-colanta.html', 'Lacteos', '1')

# Ejecuta las funciones de scraping de la tienda Carulla

# Lacteos
scrapeCarulla('https://www.carulla.com/leche-entera-en-bolsa-x-1-litro-125079/p', 'Lacteos', '0')
scrapeCarulla('https://www.carulla.com/mantequilla-sin-sal-barra-x-250-gr-61169/p', 'Lacteos', '1')

# Ejecuta las funciones de scraping de la tienda Jumbo

# Lacteos
scrapeJumbo('https://www.tiendasjumbo.co/leche-entera-liquida-x-1000cm3-colanta/p', 'Lacteos','0')
scrapeJumbo('https://www.tiendasjumbo.co/mantequilla-con-sal-x-250-g-colanta/p', 'Lacteos','1')