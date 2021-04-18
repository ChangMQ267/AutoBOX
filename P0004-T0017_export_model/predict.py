# 脚本运行依赖paddlex
# pip install paddlex
import os
from datetime import datetime

import paddlex as pdx
import cv2
from setXML import loadresultList

Timestart = datetime.now()
# 模型加载, 请将path_to_model替换为你的模型导出路径
# 可使用 mode = pdx.load_model('path_to_model') 加载
# 而使用Predictor方式加载模型，会对模型计算图进行优化，预测速度会更快
print("Loading model...")
model = pdx.deploy.Predictor('inference_model', use_gpu=True, gpu_id=0, use_mkl=False, mkl_thread_num=4, use_trt=False,
                             use_glog=False, memory_optimize=True)
print("Model loaded.")

# 模型预测, 可以将图片替换为你需要替换的图片地址
# 使用Predictor时，刚开始速度会比较慢，参考此issue
# https://github.com/PaddlePaddle/PaddleX/issues/116

# E:\VOC\JPEGImages 图片资源地址
PATH = "E:/VOC/JPEGImages"
SAVEPATH = "E:/VOC/anno"
try:
    os.mkdir(SAVEPATH)
except:
    pass

for (dirpath, dirnames, filenames) in os.walk(PATH):
    dirpath = str(dirpath).replace("\\", "/")
    for file in filenames:
        img = dirpath + '/' + file
        im = cv2.imread(img)
        im = im.astype('float32')
        resultList = model.predict(im)
        loadresultList(dirpath, file, SAVEPATH, resultList)
        # 输出分类结果
        # if model.model_type == "classifier":
        #     print(result)
        #
        # # 可视化结果, 对于检测、实例分割务进行可视化
        # if model.model_type == "detector":
        #     # threshold用于过滤低置信度目标框
        #     # 可视化结果保存在当前目录
        #     pdx.det.visualize(im, result, threshold=0.5, save_dir='./')
        #
        # # 可视化结果, 对于语义分割务进行可视化
        # if model.model_type == "segmenter":
        #     # weight用于调整结果叠加时原图的权重
        #     # 可视化结果保存在当前目录
        #     pdx.seg.visualize(im, result, weight=0.0, save_dir='./')
time = datetime.now() - Timestart
print(time)
