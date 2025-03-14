from PIL import Image
from imgtools import *
from IPython.display import display

my_dir="C:/Users/Admin/projectDocker/ml/computervision/image_data"

# Đọc nhiều ảnh
img_list = get_image_list(my_dir)

# Hiển thị toàn bộ ảnh băng hàm display:
for img in img_list:
    display(img)

