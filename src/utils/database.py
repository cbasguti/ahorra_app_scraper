from firebase import firebase

firebase_url = 'https://ahorrapp-79bef-default-rtdb.firebaseio.com/'
# Establece una conexión con la base de datos de Firebase
fb = firebase.FirebaseApplication(firebase_url, None)

def updateFirebase(productId, tienda, price):
    # Actualiza el precio del producto en la base de datos
    fb.put('/productos/Lacteos/' + productId + '/precios', tienda, int(price))