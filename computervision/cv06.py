from PIL import Image
from imgtools import *
from IPython.display import display

# Đường dẫn ảnh
image_dir="C:/Users/Admin/projectDocker/ml/computervision/image_data"

# Đọc ảnh
img = load_image(image_dir)
display(img)

# Định vị khu vực cắt
region = (100, 100, 250, 250)

# Cắt vùng ảnh
cropped_image = img.crop(region)
display(cropped_image)

# Dán

paste_position = (250,250)
img.paste(cropped_image, paste_position)
display(img)