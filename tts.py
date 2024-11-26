# tts.py
import nls
from rich.console import Console

console = Console()

# 阿里云语音合成配置
URL = "wss://nls-gateway-cn-shanghai.aliyuncs.com/ws/v1"

class AliyunTTS:
    def __init__(self, token: str, appkey: str):
        """
        初始化AliyunTTS实例
        :param token: 阿里云访问Token
        :param appkey: 阿里云AppKey
        """
        self.token = token
        self.appkey = appkey

    def synthesize(self, text: str, output_file: str, voice: str = "cally", sample_rate: int = 16000):
        """
        使用阿里云语音合成API将文本转换为音频文件
        :param text: 要合成的文本
        :param output_file: 输出的音频文件路径
        :param voice: 发音人
        :param sample_rate: 音频采样率，默认为16000
        """
        # 清空文件内容（如果存在）
        with open(output_file, "wb") as f:
            pass  # 清空文件内容

        def on_metainfo(message, *args):
            console.print(f"[cyan]Meta info received: {message}")

        def on_data(data, *args):
            with open(output_file, "ab") as f:
                f.write(data)

        def on_error(message, *args):
            console.print(f"[red]TTS Error: {message}")

        def on_close(*args):
            pass  # 可以选择不打印关闭信息

        def on_completed(message, *args):
            pass  # 可以选择不打印完成信息

        tts = nls.NlsSpeechSynthesizer(
            url=URL,
            token=self.token,
            appkey=self.appkey,
            on_metainfo=on_metainfo,
            on_data=on_data,
            on_completed=on_completed,
            on_error=on_error,
            on_close=on_close,
        )

        # 开始语音合成
        tts.start(
            text=text,
            voice=voice,
            aformat="wav",
            sample_rate=sample_rate,
        )