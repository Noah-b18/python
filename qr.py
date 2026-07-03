import qrcode

url = input("enter url :")
nom = input("enter name :")

img = qrcode.make(url)
img.save(f"C:/Users/noaht/OneDrive/Dev/python/qr/{nom}.png")
