from setuptools import find_packages, setup

setup(
    name="ChatGPT_HTTP",
    version="0.0.1",
    description="能将ChatGPT的回复转发到本地端口8000，以供使用其他语言的开发者利用HTTP协议获取ChatGPT的回复",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SkyWither/ChatGPT_HTTP",
    author="SkyWither",
    license="GNU General Public License v2.0",
    packages=find_packages(),
    install_requires=[
        "OpenAIAuth==0.3.2",
        "requests[socks]",
        "httpx[socks]",
        "prompt-toolkit",
        "tiktoken",
    ],
    extras_require={
        "unofficial": [
            "requests",
            "undetected_chromedriver",
            "selenium",
            "tls_client",
        ],
        "official": [
            "openai",
            "tiktoken",
        ],
    },
)
