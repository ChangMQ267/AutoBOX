import os


def float2int(num_str):
    num = float(num_str)
    num_s = num % 1
    if num_s >= 0.5:
        num_end = int(num) + 1
    else:
        num_end = int(num)
    return num_end


def setXML(filename, path, ObjectList, savePath):
    n = "\n"
    strXML = "<annotation>\n<folder>JPEGImages</folder>" + n
    strXML = strXML + "<filename>" + filename + "</filename>" + n
    strXML = strXML + "<path>" + path + "/" + filename + "</path>" + n
    strXML = strXML + "<source>\n<database>Unknown</database>\n</source>\n<size>\n<width>608</width>\n<height>608</height>\n<depth>3</depth>\n</size>\n<segmented>0</segmented>\n"
    for object in ObjectList:
        strXML = strXML + object
    strXML = strXML + "</annotation>\n"
    file_xml = str(filename).replace(".jpg", "")
    filesave = savePath + "/" + file_xml + ".xml"
    with open(filesave, "w+", encoding="UTF-8") as xml:
        xml.write(strXML)


def setObject(name, xmin, ymin, w, h):
    ymax = str(float2int(float(ymin) + float(h)))
    xmax = str(float2int(float(xmin) + float(w)))
    xmin = str(float2int(xmin))
    ymin = str(float2int(ymin))
    name = str(name)

    strObject = "<object>\n<name>" + name + "</name>\n<pose>Unspecified</pose>\n<truncated>0</truncated>\n<difficult>0</difficult>\n<bndbox>\n<xmin>"
    strObject = strObject + xmin + "</xmin>\n<ymin>"
    strObject = strObject + ymin + "</ymin>\n<xmax>"
    strObject = strObject + xmax + "</xmax>\n<ymax>"
    strObject = strObject + ymax + "</ymax>\n</bndbox>\n</object>\n"
    return strObject


def setMaxScore():
    pass


def loadresultList(Path, FileName, SavePath, resultList):
    ObjectList = []
    HLJ_b_max = 1
    HLJ_a_max = 1
    HCJ_c_max = 1
    HCJ_d_max = 1
    num = 1
    for result in resultList:
        # print(result)
        # if result.get('score') >= 0.5:
        # print(result)
        name = result.get('category')
        bbox = result.get('bbox')
        # print("No:%d" % num)
        # print(result)
        if name == '红龙睛-a' and HLJ_a_max == 1:
            # print(str(result) + '红龙睛-a')
            ObjectList.append(setObject(name, bbox[0], bbox[1], bbox[2], bbox[3]))
            HLJ_a_max = 0
            if result.get('score') < 0.5:
                print(FileName, "--", result.get('score'), "--", result)
        if name == '红龙睛-b' and HLJ_b_max == 1:
            # print(str(result) + '红龙睛-b')
            ObjectList.append(setObject(name, bbox[0], bbox[1], bbox[2], bbox[3]))
            HLJ_b_max = 0
            if result.get('score') < 0.5:
                print(FileName, "--", result.get('score'), "--", result)
        if name == '红草金-c' and HCJ_c_max == 1:
            # print(str(result) + '红草金-c')
            ObjectList.append(setObject(name, bbox[0], bbox[1], bbox[2], bbox[3]))
            HCJ_c_max = 0
            if result.get('score') < 0.5:
                print(FileName, "--", result.get('score'), "--", result)
        if name == '红草金-d' and HCJ_d_max == 1:
            # print(str(result) + '红草金-d')
            ObjectList.append(setObject(name, bbox[0], bbox[1], bbox[2], bbox[3]))
            HCJ_d_max = 0
            if result.get('score') < 0.5:
                print(FileName, "--", result.get('score'), "--", result)
        if name == 'head' and result.get('score') >= 0.5:
            ObjectList.append(setObject(name, bbox[0], bbox[1], bbox[2], bbox[3]))
        num += 1
    setXML(FileName, Path, ObjectList, SavePath)


if __name__ == '__main__':
    # print(setObject(0,1,2,3,4))
    setXML("demo.jpg", "", setObject(0, 1, 2, 3, 4), "D:/")
