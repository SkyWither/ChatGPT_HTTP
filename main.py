import os

from src.revChatGPT.V1 import Chatbot
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        if directory is None:
            directory = os.getcwd()
        self.directory = os.fspath(directory)
        self.chatbot = Chatbot(config={
            "email": "email",
            "password": "your password"
        })
        super().__init__(*args, **kwargs)

    def do_GET(self):
        # 解析 URL，获取参数
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        if parsed_url.path == '/chat' and 'msg' in query_params:
            # 获取 msg 参数的值
            msg = query_params['msg'][0]


            prev_text = ""
            for data in self.chatbot.ask(msg, ):
                prev_text = data["message"]
            print(prev_text)

            # prev_text = ''''''

            # 构造响应
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(prev_text.encode('utf-8'))
        else:
            # 处理其他请求
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Not found".encode('utf-8'))


if __name__ == '__main__':
    # 创建 HTTP 服务器，监听本地 8000 端口
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print('HTTP server running on %s:%d' % server_address)

    # 启动 HTTP 服务器
    httpd.serve_forever()
