# JC-WebChat

![WX20230905-220045@2x](https://github.com/JC0v0/JC-WebChat/assets/108552928/ff8e837f-7a1c-4a0a-8dc2-4497d97154ac)

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

配置文件的模板在根目录的`config-template.py`中，需复制该模板创建最终生效的 `config.py` 文件：

```bash
  cp config-template.py config.py
```
然后在`config.py`中填入配置

## 运行
运行根目录下的`webapp.py` 文件就可以在终端对话
```bash
python webapp.py
```
