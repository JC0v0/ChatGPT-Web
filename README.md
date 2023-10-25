# JC-WebChat

![WechatIMG6489](https://github.com/JC0v0/JC-WebChat/assets/108552928/37412aab-9a34-4604-b3bf-64e3d088d220)

克隆项目代码：
```bash
git clone https://github.com/JC0v0/JC-WebChat.git
cd JC-WebChat/
```

安装核心依赖 (必选)：
```bash
pip install -r requirements.txt
```

## 配置

1.配置文件的模板在根目录的`config-template.py`中，需复制该模板创建最终生效的 `config.py` 文件：

```bash
  cp config-template.py config.py
```
然后在`config.py`中填入配置

2.配置.env文件，前往https://cloud.chainlit.io/
创建 Chainlit 项目
<img width="1142" alt="project" src="https://github.com/JC0v0/JC-WebChat/assets/108552928/d822f54b-5afc-41ae-b2ef-43c64d5e6bb7">
单击“创建 API 密钥”按钮创建新的 API 密钥。
<img width="1129" alt="apikey" src="https://github.com/JC0v0/JC-WebChat/assets/108552928/c06b5da6-5a0f-46f2-b17c-c820dce7eda7">


## 运行
运行根目录下的`web.py` 文件
```bash
chainlit run web.py
```
