import os
import glob
import shutil

root_dir = "./images"
output_dir = "./data"


os.makedirs(os.path.join(output_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "labels"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "images", "train"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "images", "val"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "labels", "train"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "labels", "val"), exist_ok=True)


files = glob.glob(f"{root_dir}/*/")
classes = [file.split('/')[2] for file in files]

class_to_id = {cls: i for i, cls in enumerate(classes)}


# for cls in classes:
#     class_dir = os.path.join(root_dir, cls)
#     if not os.path.exists(class_dir):
#         continue
#     #print (class_dir)
#     images = glob.glob(f"{class_dir}/*")

#     #print(images)
#     for i, img_file in enumerate(images):
#         if img_file.endswith((".jpg", ".png", ".jpeg")):
#             img_path = img_file
#             print(img_path)
#             if i % 5 == 0:
#                 output_img_path = os.path.join(output_dir, "images", "val", img_path.split('/')[-1])
#                 shutil.copyfile(img_path, output_img_path)
#             else:
#                 output_img_path = os.path.join(output_dir, "images", "train", img_path.split('/')[-1])
#                 shutil.copyfile(img_path, output_img_path)
#             #print(img_file)
#             label_file = os.path.splitext(img_file.split('/')[-1])[0] + ".txt"
#             #print(label_file)
#             if i % 5 == 0:
#                 label_path = os.path.join(output_dir, "labels", "val", label_file)
#             else:
#                 label_path = os.path.join(output_dir, "labels", "train", label_file)
#             with open(label_path, "w") as f:
#                 f.write(f"{class_to_id[cls]} 0.5 0.5 1.0 1.0\n")
        

yaml_file = os.path.join(output_dir, "data.yaml")
with open(yaml_file, "w") as f:
    l1 = 'path: ' + output_dir + '\n'
    l2 = 'train: images/train\n'
    l3 = 'val: images/val\n'
    l4 = 'name:\n'
    l5 = f"  0:{classes[0]}\n"
    l6 = f"  1:{classes[1]}\n"
    l7 = f"  2:{classes[2]}\n"
    l8 = f"  3:{classes[3]}\n"
    l9 = f"  4:{classes[4]}\n"
    l10 = f"  5:{classes[5]}\n"
    l11 = f"  6:{classes[6]}\n"
    f.writelines([l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11])
print('Done')
