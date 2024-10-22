import qrcode.image.svg
a=qrcode.image.svg.SvgPathImage
simg=qrcode.make("https://www.linkedin.com/in/prateek-kv-613822281?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",image_factory=a)
simg.save("li.svg") 
