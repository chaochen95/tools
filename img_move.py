# -*- coding: utf-8 -*-
import os,sys,shutil
#print(sys.path[0])
train_path = sys.path[0] + "/image_data/train_set"
test_path = sys.path[0] + "/image_data/test_set"
val_path = sys.path[0] + "/image_data/val_set"
for dirname in os.listdir(train_path):
    img_path = os.path.join(train_path, dirname)#图片文件夹路径
    img_path_test = os.path.join(test_path,dirname)
    img_path_val = os.path.join(val_path,dirname)
    
    img_list = os.listdir(img_path)#图片列表
    img_num = len(os.listdir(img_path))
    train_list = img_list[0:int(0.7*img_num)]
    test_list = img_list[int(0.7*img_num):int(0.9*img_num)]
    #移动20%到测试集
    for img_name in test_list:
        if not os.path.exists(img_path_test):
            os.makedirs(img_path_test) 
        shutil.move(img_path+"/"+img_name, img_path_test)
    
    val_list = img_list[int(0.9*img_num):]
    for img_name in val_list:
        if not os.path.exists(img_path_val):
            os.makedirs(img_path_val) 
        shutil.move(img_path+"/"+img_name, val_path)
print("done")
