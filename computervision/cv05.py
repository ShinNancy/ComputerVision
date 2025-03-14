from PIL import Image
from imgtools import *
from IPython.display import display

# thư mục chứa đường dẫn ảnh
image_dir="C:/Users/Admin/projectDocker/ml/computervision/image_data/1.JPG"

# đọc ảnh
img = load_image(image_dir)
display(img)

# Kích thước ban đầu
print(img.size)

# Thay đổi kích thước
new_size = (100, 100)
print(new_size)

# Ảnh mới 
new_image = img.resize(new_size)
display(new_image)