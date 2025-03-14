from PIL import Image

image_dir="C:/Users/Admin/projectDocker/ml/computervision/image_data"

image_path = image_dir+"/1.JPG"
print(image_path)

# Sử dụng Image.open() đọc ảnh
img01 = Image.open(image_path)

# Hiển thị hình ảnh
img01.show()

# In một số thông tin
print("Định dạng ảnh: ", img01.format)

# In ra size
print("Kích thước ảnh: ", img01.size)

# Lưu ảnh
new_img_01_path = image_dir + "/new.JPG"
img01.save(new_img_01_path)

# Đóng tập tin
img01.close()