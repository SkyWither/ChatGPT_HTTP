# ChatGPT_HTTP
 能将ChatGPT的回复转发到本地端口，以供使用其他语言的开发者利用HTTP协议获取ChatGPT的回复。此项目依赖于acheong08/ChatGPT的项目。

# 使用方法
1. 打开```Pycharm```
2. 使用```Pycharm```打开```setup.py```，进行配置，安装必要依赖。
3. 打开```main.py```修改```email```与```password```
4. 在```Pycharm```的侧边栏```Project```下右键```main.py```，选择run
5. 接下来，你向```127.0.0.1:8000```POST数据，就会发送到ChatGPT中
6. ChatGPT响应后，会返回一个```response```，对```response```进行解析即可获取ChatGPT的内容了

> Note
> 如果ChatGPT文件夹为空的，请手动下载ChatGPT文件夹的内容复制到ChatGPT下，
> 或使用git clone命令git本项目，以获取完整内容。

