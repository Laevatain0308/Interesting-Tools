import ffmpy
import os


print("请输入输入文件夹路径：" , end = "")
inputFileDir = input()

print("请输入输入文件格式：" , end = "")
inputFormat = input()

print("请输入待输出文件夹路径：" , end = "")
outputFileDir = input()

print("请输入待输出文件格式：" , end = "")
outputFormat = input()


# 获取 格式文件名 和 待输出的格式文件名
inputFiles = []
outputFiles = []
for i in os.listdir(inputFileDir):
    temp = -len(inputFormat)-1
    if i[temp:] == "." + inputFormat:
        inputFiles.append(inputFileDir + "\\" + i)
        outputFiles.append(outputFileDir + "\\" + i[:temp] + "." + outputFormat)


# 利用 ffmpeg 进行格式转换
for i in range(len(inputFiles)):
    ff = ffmpy.FFmpeg(
        inputs = { inputFiles[i] : None },
        outputs = { outputFiles[i] : None }
    )
    ff.run()


# print(inputFiles)
# print(outputFiles)