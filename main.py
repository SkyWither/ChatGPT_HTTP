import http
import os

from ChatGPT.src.revChatGPT.V1 import Chatbot
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        if directory is None:
            directory = os.getcwd()
        self.directory = os.fspath(directory)
        self.chatbot = Chatbot(config={
            "email": "email",
            "password": "password"
        })
        super().__init__(*args, **kwargs)

    def do_POST(self):
        # 获取请求内容的长度
        content_length = int(self.headers['Content-Length'])
        # 读取请求内容
        post_data = self.rfile.read(content_length)
        # 解析请求内容中的参数
        params = parse_qs(post_data.decode('utf-8'))
        # 输出解析后的参数
        # print(params)

        # 读取ChatGPT的回复
        prev_text = ""
        # 解析 POST 请求的内容，并提取出字符串数据
        for key in params.keys():
            # 这里只解析POST键值对的第0个数据
            my_string = params.get(key)[0]
            print(params.get(key)[0])
            for data in self.chatbot.ask(my_string, ):
                prev_text = data["message"]
            print(prev_text)

        # 修改ChatGPT回复的格式
        # prev_text = '''{"text":"''' + prev_text + '''"}'''

        # 响应请求
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(prev_text.encode('utf-8'))


if __name__ == '__main__':
    server_address = ('127.0.0.1', 8000)
    httpd = http.server.HTTPServer(server_address, HTTPRequestHandler)
    httpd.serve_forever()
