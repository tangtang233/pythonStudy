import sys

print('================Python import mode==========================');
print('命令行参数为:')
# 打印命令行参数
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)
